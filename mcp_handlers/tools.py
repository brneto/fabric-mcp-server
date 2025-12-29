"""
MCP Tools for the Fabric MCP Server.

This module contains tool handlers for:
- list_strategies: List all available strategies
- list_patterns: List all available Fabric patterns
- execute_pattern: Execute a Fabric pattern with content
- list_research_resources: List all available research documents
- read_research_resource: Read a specific research document
"""

from typing import List

import mcp.types as types

from helpers import (
    get_strategy_content,
    get_pattern_content,
    list_all_patterns,
    list_all_strategies,
    get_available_researches,
    slugify,
)
from mcp_handlers.resources import read_resource


def get_tools() -> List[types.Tool]:
    """Return the list of available tools."""
    return [
        types.Tool(
            name="list_strategies",
            description="List all available strategies (used as argument of Fabric patterns prompts) with their descriptions",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        types.Tool(
            name="list_patterns",
            description="List all available Fabric patterns (prompts) that can be used for content analysis",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        types.Tool(
            name="execute_pattern",
            description="Execute a Fabric pattern to analyze content. Use list_patterns to discover available patterns and list_strategies for available strategies.",
            inputSchema={
                "type": "object",
                "properties": {
                    "pattern": {
                        "type": "string",
                        "description": "Pattern name to execute (e.g., 'create_micro_summary', 'extract_wisdom', 'summarize')"
                    },
                    "input": {
                        "type": "string",
                        "description": "Content to analyze: text, URL (YouTube, article, etc.), or any input for the pattern"
                    },
                    "strategy": {
                        "type": "string",
                        "description": "Optional thinking strategy to enhance analysis (e.g., 'cot' for chain-of-thought, 'tot' for tree-of-thought)"
                    }
                },
                "required": ["pattern", "input"]
            }
        ),
        types.Tool(
            name="list_research_resources",
            description="List all available research documents (papers, articles) that can be read and analyzed. Returns both markdown and PDF resources.",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        types.Tool(
            name="read_research_resource",
            description="Read a research document by name. Use list_research_resources to discover available documents. Returns the full content of the document for analysis.",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "The slug name of the research document (e.g., 'the-prompt-report')"
                    },
                    "format": {
                        "type": "string",
                        "enum": ["markdown", "pdf"],
                        "description": "Format of the document to read. Defaults to 'markdown' if not specified."
                    }
                },
                "required": ["name"]
            }
        )
    ]


def _handle_list_strategies() -> List[types.TextContent]:
    """Handle the list_strategies tool."""
    strategies = list_all_strategies()
    if not strategies:
        return [types.TextContent(type="text", text="No strategies found")]
    result = [
        f"- **{s['name']}**: {s['description']}"
        for s in strategies
    ]
    return [types.TextContent(type="text", text="\n".join(result))]


def _handle_list_patterns() -> List[types.TextContent]:
    """Handle the list_patterns tool."""
    patterns = list_all_patterns()
    if not patterns:
        return [types.TextContent(type="text", text="No patterns found")]
    result = [
        f"- **{p['name']}**: {p['description']}"
        for p in patterns
    ]
    return [types.TextContent(type="text", text="\n".join(result))]


def _handle_execute_pattern(arguments: dict) -> List[types.TextContent]:
    """Handle the execute_pattern tool."""
    pattern_name = arguments.get("pattern")
    user_input = arguments.get("input")
    strategy_name = arguments.get("strategy")

    if not pattern_name:
        raise ValueError("Pattern name is required")
    if not user_input:
        raise ValueError("Input is required")

    content = get_pattern_content(pattern_name)
    if content is None:
        raise ValueError(f"Pattern '{pattern_name}' not found. Use list_patterns to see available patterns.")

    # Prepend strategy if provided
    if strategy_name:
        strategy = get_strategy_content(strategy_name)
        if not strategy:
            raise ValueError(f"Strategy '{strategy_name}' not found. Use list_strategies to see available strategies.")
        content = f"{strategy.get('prompt')}\n\n{content}"

    # Append user input
    content += f"{user_input}"

    return [types.TextContent(type="text", text=content)]


def _handle_list_research_resources() -> List[types.TextContent]:
    """Handle the list_research_resources tool."""
    resources = []

    # Get markdown resources
    md_researches = get_available_researches("markdown")
    for slug, info in md_researches.items():
        resources.append(f"- **{slug}** (markdown): {info['human_name']}")

    # Get PDF resources
    pdf_researches = get_available_researches("pdf")
    for slug, info in pdf_researches.items():
        resources.append(f"- **{slug}** (pdf): {info['human_name']}")

    if not resources:
        return [types.TextContent(type="text", text="No research resources found")]

    result = "Available research documents:\n" + "\n".join(resources)
    return [types.TextContent(type="text", text=result)]


def _handle_read_research_resource(arguments: dict) -> List[types.TextContent]:
    """Handle the read_research_resource tool."""
    resource_name = arguments.get("name")
    resource_format = arguments.get("format", "markdown")

    if not resource_name:
        raise ValueError("Resource name is required")

    if resource_format not in ("markdown", "pdf"):
        raise ValueError("Format must be 'markdown' or 'pdf'")

    # Normalize the resource name to a slug (handles both "The Prompt Report" and "the-prompt-report")
    resource_slug = slugify(resource_name)
    uri = f"{resource_format}://researches/{resource_slug}"

    try:
        content = read_resource(uri)
        if isinstance(content, bytes):
            # For PDF, return a message since we can't display binary
            return [types.TextContent(
                type="text",
                text=f"PDF document '{resource_name}' loaded ({len(content)} bytes). Note: PDF binary content cannot be displayed as text. Use markdown format for readable content."
            )]
        return [types.TextContent(type="text", text=content)]
    except ValueError as e:
        raise ValueError(str(e))


# Tool handler registry
_TOOL_HANDLERS = {
    "list_strategies": lambda args: _handle_list_strategies(),
    "list_patterns": lambda args: _handle_list_patterns(),
    "execute_pattern": _handle_execute_pattern,
    "list_research_resources": lambda args: _handle_list_research_resources(),
    "read_research_resource": _handle_read_research_resource,
}


def call_tool(name: str, arguments: dict) -> List[types.TextContent]:
    """Handle tool invocations."""
    handler = _TOOL_HANDLERS.get(name)
    if handler is None:
        raise ValueError(f"Unknown tool: {name}")
    return handler(arguments)

