"""
MCP feature handlers for the Fabric MCP Server.

This package contains MCP protocol handlers organized into modules:
- tools: Tool handlers (get_tools, call_tool)
- resources: Resource handlers (list_resources, read_resource, subscribe, unsubscribe)
- prompts: Prompt handlers (list_prompts, get_prompt)
"""

from .tools import (
    get_tools,
    call_tool,
)

from .resources import (
    list_resources,
    list_resource_templates,
    read_resource,
    subscribe,
    unsubscribe,
    set_notification_callback,
)

from .prompts import (
    list_prompts,
    get_prompt,
)

__all__ = [
    # Tools
    "get_tools",
    "call_tool",
    # Resources
    "list_resources",
    "list_resource_templates",
    "read_resource",
    "subscribe",
    "unsubscribe",
    "set_notification_callback",
    # Prompts
    "list_prompts",
    "get_prompt",
]


