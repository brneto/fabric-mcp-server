"""
MCP Resources for the Fabric MCP Server.

This module contains resource handlers for:
- Research documents in markdown format
- Dynamic resource discovery from the resources folder
- Resource subscription for change notifications
"""

import asyncio
import logging
from pathlib import Path
from typing import List, Set, Callable, Awaitable, Optional
from urllib.parse import urlparse

from pydantic import AnyUrl
import mcp.types as types

from helpers import get_available_researches
from helpers.config import RESOURCES_DIR

# Configure logging
logger = logging.getLogger("fabric-mcp-server")

# Track active subscriptions
_subscribed_uris: Set[str] = set()
_watch_task: Optional[asyncio.Task] = None
_notification_callback: Optional[Callable[[str], Awaitable[None]]] = None


def _uri_to_path(uri: str) -> Optional[Path]:
    """Convert a resource URI to its file path."""
    parsed = urlparse(str(uri))
    if parsed.scheme != "markdown":
        return None

    path_parts = parsed.path.strip("/").split("/")
    if len(path_parts) != 2 or path_parts[0] != "researches":
        return None

    slug = path_parts[1]
    researches = get_available_researches()
    if slug in researches:
        return researches[slug]["path"]
    return None


def _path_to_uri(path: Path) -> Optional[str]:
    """Convert a file path to its resource URI."""
    slug = path.stem.lower().replace("_", "-").replace(" ", "-")
    return f"markdown://researches/{slug}"


async def _watch_resources():
    """Watch the resources directory for changes and notify subscribers."""
    try:
        from watchfiles import awatch, Change

        logger.info(f"Starting file watcher for: {RESOURCES_DIR}")

        async for changes in awatch(RESOURCES_DIR):
            for change_type, path_str in changes:
                path = Path(path_str)

                # Only watch markdown files
                if path.suffix != ".md":
                    continue

                uri = _path_to_uri(path)
                if uri and uri in _subscribed_uris and _notification_callback:
                    logger.info(f"Resource changed: {uri} ({change_type.name})")
                    await _notification_callback(uri)

    except asyncio.CancelledError:
        logger.info("File watcher stopped")
        raise  # Re-raise to properly propagate cancellation
    except ImportError as e:
        logger.error(f"watchfiles package not installed: {e}")
    except OSError as e:
        logger.error(f"File watcher filesystem error: {e}")


def set_notification_callback(callback: Callable[[str], Awaitable[None]]) -> None:
    """Set the callback function for resource change notifications."""
    global _notification_callback
    _notification_callback = callback


def subscribe(uri: str) -> None:
    """
    Subscribe to changes for a specific resource URI.
    """
    global _watch_task

    # Validate the URI
    parsed = urlparse(str(uri))
    if parsed.scheme != "markdown":
        raise ValueError(f"Unsupported scheme for subscription: {parsed.scheme}")

    path_parts = parsed.path.strip("/").split("/")
    if len(path_parts) != 2 or path_parts[0] != "researches":
        raise ValueError("Invalid URI format for subscription")

    # Add to subscriptions
    _subscribed_uris.add(str(uri))
    logger.info(f"Subscribed to resource: {uri}")

    # Start the watcher if not already running
    if _watch_task is None or _watch_task.done():
        _watch_task = asyncio.create_task(_watch_resources())


def unsubscribe(uri: str) -> None:
    """
    Unsubscribe from changes for a specific resource URI.
    """
    global _watch_task

    uri_str = str(uri)
    if uri_str in _subscribed_uris:
        _subscribed_uris.discard(uri_str)
        logger.info(f"Unsubscribed from resource: {uri}")

    # Stop the watcher if no more subscriptions
    if not _subscribed_uris and _watch_task and not _watch_task.done():
        _watch_task.cancel()


def list_resources() -> List[types.Resource]:
    """
    List all available research documents.
    This allows clients to discover available resources before using the template.
    """
    researches = get_available_researches()
    resources = []

    for slug, info in researches.items():
        resources.append(
            types.Resource(
                uri=AnyUrl(f"markdown://researches/{slug}"),
                name=info["human_name"],
                description=f"Research paper: {info['human_name']}",
                mimeType="text/markdown"
            )
        )

    return resources


def list_resource_templates() -> List[types.ResourceTemplate]:
    """
    Expose the custom URI pattern to clients.
    """
    # Build list of available titles for the description
    researches = get_available_researches()
    available_titles = ", ".join(researches.keys()) if researches else "none available"

    return [
        types.ResourceTemplate(
            uriTemplate="markdown://researches/{title}",
            name="Markdown Researches",
            description=f"Access markdown researches by title. Available titles: {available_titles}",
            mimeType="text/markdown"
        )
    ]


def read_resource(uri: str) -> str:
    """
    Handle requests for the custom URI.
    """
    parsed = urlparse(str(uri))

    # 1. Validate the scheme and path structure
    if parsed.scheme != "markdown":
        raise ValueError(f"Unsupported scheme: {parsed.scheme}")

    path_parts = parsed.path.strip("/").split("/")
    if len(path_parts) != 2 or path_parts[0] != "researches":
        raise ValueError("Invalid URI format. Expected markdown://researches/{title}")

    paper_name = path_parts[1]

    # 2. Dynamically get available researches
    file_map = get_available_researches()

    if paper_name not in file_map:
        available = ", ".join(file_map.keys()) if file_map else "none"
        raise ValueError(f"Paper '{paper_name}' not found. Available: {available}")

    # 3. Read and return the content
    file_path = file_map[paper_name]["path"]
    try:
        return file_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise ValueError(f"File for '{paper_name}' not found.")
