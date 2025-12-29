"""
MCP Resources for the Fabric MCP Server.

This module contains resource handlers for:
- Research documents in markdown format
- Research documents in PDF format
- Dynamic resource discovery from the resources folders
- Resource subscription for change notifications (markdown only)
"""

import asyncio
import logging
from pathlib import Path
from typing import List, Set, Callable, Awaitable, Optional
from urllib.parse import urlparse

from pydantic import AnyUrl
import mcp.types as types

from helpers import get_available_researches, ResourceType
from helpers.config import MD_RESOURCES_DIR

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

    # urlparse treats "markdown://researches/title" as:
    #   scheme="markdown", netloc="researches", path="/title"
    if parsed.netloc != "researches":
        return None

    slug = parsed.path.strip("/")
    if not slug or "/" in slug:
        return None

    researches = get_available_researches()
    if slug in researches:
        return researches[slug]["path"]
    return None


def _path_to_uri(path: Path) -> Optional[str]:
    """Convert a file path to its resource URI."""
    slug = path.stem.lower().replace("_", "-").replace(" ", "-")
    return f"markdown://researches/{slug}"


async def _invoke_callback(callback: Callable[[str], Awaitable[None]], uri: str) -> None:
    """Invoke the notification callback."""
    await callback(uri)


async def _process_file_change(path: Path, change_type) -> None:
    """Process a single file change and notify if subscribed."""
    # Only watch markdown files
    if path.suffix != ".md":
        return

    uri = _path_to_uri(path)
    if not uri or uri not in _subscribed_uris:
        return

    callback = _notification_callback
    if callback is None:
        return

    logger.info(f"Resource changed: {uri} ({change_type.name})")
    await _invoke_callback(callback, uri)


async def _watch_resources():
    """Watch the resources directory for changes and notify subscribers."""
    try:
        from watchfiles import awatch

        logger.info(f"Starting file watcher for: {MD_RESOURCES_DIR}")

        async for changes in awatch(MD_RESOURCES_DIR):
            for change_type, path_str in changes:
                await _process_file_change(Path(path_str), change_type)

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
    List all available research documents (markdown and PDF).
    This allows clients to discover available resources before using the template.
    """
    resources = []

    # Add markdown resources
    for slug, info in get_available_researches("markdown").items():
        resources.append(
            types.Resource(
                uri=AnyUrl(f"markdown://researches/{slug}"),
                name=f"{info['human_name']} (Markdown)",
                description=f"Research paper (Markdown): {info['human_name']}",
                mimeType="text/markdown"
            )
        )

    # Add PDF resources
    for slug, info in get_available_researches("pdf").items():
        resources.append(
            types.Resource(
                uri=AnyUrl(f"pdf://researches/{slug}"),
                name=f"{info['human_name']} (PDF)",
                description=f"Research paper (PDF): {info['human_name']}",
                mimeType="application/pdf"
            )
        )

    return resources


def list_resource_templates() -> List[types.ResourceTemplate]:
    """
    Expose the custom URI patterns to clients.
    """
    # Build list of available titles for markdown
    md_researches = get_available_researches("markdown")
    available_md_titles = ", ".join(md_researches.keys()) if md_researches else "none available"

    # Build list of available titles for PDF
    pdf_researches = get_available_researches("pdf")
    available_pdf_titles = ", ".join(pdf_researches.keys()) if pdf_researches else "none available"

    return [
        types.ResourceTemplate(
            uriTemplate="markdown://researches/{title}",
            name="Markdown Researches",
            description=f"Access markdown researches by title. Available titles: {available_md_titles}",
            mimeType="text/markdown"
        ),
        types.ResourceTemplate(
            uriTemplate="pdf://researches/{title}",
            name="PDF Researches",
            description=f"Access PDF researches by title. Available titles: {available_pdf_titles}",
            mimeType="application/pdf"
        )
    ]


def _read_research_resource(paper_name: str, resource_type: ResourceType) -> str | bytes:
    """
    Read a research document by name and type.

    Args:
        paper_name: The slug name of the paper
        resource_type: Type of resource ("markdown" or "pdf")

    Returns:
        Text content for markdown, bytes for PDF.
    """
    file_map = get_available_researches(resource_type)

    if paper_name not in file_map:
        available = ", ".join(file_map.keys()) if file_map else "none"
        raise ValueError(f"{resource_type.capitalize()} paper '{paper_name}' not found. Available: {available}")

    file_path = file_map[paper_name]["path"]
    try:
        if resource_type == "markdown":
            return file_path.read_text(encoding="utf-8")
        else:
            return file_path.read_bytes()
    except OSError:
        raise ValueError(f"Failed to read {resource_type} file for '{paper_name}'.")


def read_resource(uri: str) -> str | bytes:
    """
    Handle requests for markdown and PDF resources.
    Returns text for markdown, bytes for PDF.
    """
    parsed = urlparse(str(uri))

    # Validate the scheme
    if parsed.scheme not in ("markdown", "pdf"):
        raise ValueError(f"Unsupported scheme: {parsed.scheme}")

    # urlparse treats "markdown://researches/title" as:
    #   scheme="markdown", netloc="researches", path="/title"
    # So we need to check netloc for "researches" and get title from path
    if parsed.netloc != "researches":
        raise ValueError(f"Invalid URI format. Expected {parsed.scheme}://researches/{{title}}")

    paper_name = parsed.path.strip("/")
    if not paper_name or "/" in paper_name:
        raise ValueError(f"Invalid URI format. Expected {parsed.scheme}://researches/{{title}}")

    resource_type: ResourceType = "markdown" if parsed.scheme == "markdown" else "pdf"

    return _read_research_resource(paper_name, resource_type)

