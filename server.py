"""
Fabric MCP Server

A Model Context Protocol server that exposes Fabric patterns and strategies
as MCP prompts and tools.
"""

import asyncio
import logging
import subprocess
from typing import List, Optional, cast, Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
import mcp.types as types

from helpers import sync_repo
from mcp_handlers.tools import get_tools, call_tool
from mcp_handlers.prompts import list_prompts, get_prompt
from mcp_handlers.resources import (
    list_resources,
    list_resource_templates,
    read_resource,
    subscribe,
    unsubscribe,
    set_notification_callback,
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("fabric-mcp-server")

# Initialize MCP server
server = Server("fabric-mcp-server", version="0.1.0")


# =============================================================================
# MCP Tools
# =============================================================================

@server.list_tools()
async def handle_list_tools() -> List[types.Tool]:
    """List available tools."""
    return get_tools()


@server.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> List[types.TextContent]:
    """Handle tool invocations."""
    return call_tool(name, arguments)


# =============================================================================
# MCP Resources
# =============================================================================

@server.list_resources()
async def handle_list_resources() -> List[types.Resource]:
    """List all available research documents."""
    return list_resources()


@server.list_resource_templates()
async def handle_list_resource_templates() -> List[types.ResourceTemplate]:
    """Expose the custom URI pattern to clients."""
    return list_resource_templates()


@server.read_resource()
async def handle_read_resource(uri: str) -> str:
    """Handle requests for the custom URI."""
    return read_resource(uri)


@server.subscribe_resource()
async def handle_subscribe_resource(uri: str) -> None:
    """Subscribe to resource changes."""
    subscribe(uri)


@server.unsubscribe_resource()
async def handle_unsubscribe_resource(uri: str) -> None:
    """Unsubscribe from resource changes."""
    unsubscribe(uri)


# =============================================================================
# MCP Prompts
# =============================================================================

@server.list_prompts()
async def handle_list_prompts() -> List[types.Prompt]:
    """List all available Fabric patterns as prompts."""
    return list_prompts()


@server.get_prompt()
async def handle_get_prompt(name: str, arguments: Optional[dict[str, str]]) -> types.GetPromptResult:
    """Get a specific prompt by name with optional strategy and input."""
    return get_prompt(name, arguments)


# =============================================================================
# Resource Change Notification
# =============================================================================

def create_resource_notification_callback(mcp_server: Server):
    """
    Create a callback function for resource change notifications.

    Args:
        mcp_server: The MCP Server instance to use for sending notifications.

    Returns:
        An async callback function that sends resource updated notifications.
    """
    async def notify_resource_changed(uri: str) -> None:
        """Send a resource changed notification to the client."""
        logger.info(f"Sending resource changed notification for: {uri}")
        try:
            from pydantic import AnyUrl
            notification = types.ResourceUpdatedNotification(
                params=types.ResourceUpdatedNotificationParams(
                    uri=AnyUrl(uri)
                )
            )
            if mcp_server.request_context and mcp_server.request_context.session:
                # Cast to ServerNotification as ResourceUpdatedNotification is a valid server notification
                # Use Any as intermediate type to avoid type checker warnings
                await mcp_server.request_context.session.send_notification(
                    cast(types.ServerNotification, cast(Any, notification))
                )
        except asyncio.CancelledError:
            raise  # Re-raise to properly propagate cancellation
        except (ValueError, OSError) as e:
            logger.error(f"Failed to send resource update notification: {e}")

    return notify_resource_changed


# =============================================================================
# Main Entry Point
# =============================================================================

async def main():
    """Initialize and run the MCP server."""
    # Sync repo on startup
    try:
        sync_repo()
    except (subprocess.CalledProcessError, OSError) as e:
        logger.error(f"Failed to sync repo: {e}")
        # Continue anyway - prompts will be empty if repo fails

    async with stdio_server() as (read_stream, write_stream):
        # Set up the notification callback for resource changes
        set_notification_callback(create_resource_notification_callback(server))

        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())

