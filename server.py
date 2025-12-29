"""
Fabric MCP Server

A Model Context Protocol server that exposes Fabric patterns and strategies
as MCP prompts and tools.
"""

import asyncio
import logging
from typing import List

from mcp.server import Server
from mcp.server.stdio import stdio_server
import mcp.types as types

from helpers import (
    sync_repo,
    get_strategy_content,
    get_pattern_content,
    list_all_patterns,
    list_all_strategies,
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
        )
    ]


@server.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> List[types.TextContent]:
    """Handle tool invocations."""
    if name == "list_strategies":
        strategies = list_all_strategies()
        if not strategies:
            return [types.TextContent(type="text", text="No strategies found")]
        result = [
            f"- **{s['name']}**: {s['description']}"
            for s in strategies
        ]
        return [types.TextContent(type="text", text="\n".join(result))]

    if name == "list_patterns":
        patterns = list_all_patterns()
        if not patterns:
            return [types.TextContent(type="text", text="No patterns found")]
        result = [
            f"- **{p['name']}**: {p['description']}"
            for p in patterns
        ]
        return [types.TextContent(type="text", text="\n".join(result))]

    raise ValueError(f"Unknown tool: {name}")


# =============================================================================
# MCP Prompts
# =============================================================================

@server.list_prompts()
async def handle_list_prompts() -> List[types.Prompt]:
    """List all available Fabric patterns as prompts."""
    patterns = list_all_patterns()
    strategies = list_all_strategies()

    # Build a list of available strategy names for the description
    strategy_names = [s["name"] for s in strategies]
    strategy_list = ", ".join(strategy_names[:5])  # Show first 5
    if len(strategy_names) > 5:
        strategy_list += f", ... ({len(strategy_names)} total)"

    strategy_description = (
        f"Thinking strategy to enhance the analysis. "
        f"Available strategies: {strategy_list}. "
        f"Common strategies: 'cot' (chain-of-thought), 'tot' (tree-of-thought). "
        f"When user says 'use strategy X', 'with strategy X', or 'using X strategy', set this to X."
    )

    return [
        types.Prompt(
            name=pattern["name"],
            description=pattern["description"],
            arguments=[
                types.PromptArgument(
                    name="strategy",
                    description=strategy_description,
                    required=False
                ),
                types.PromptArgument(
                    name="input",
                    description="The content to process: text, URL (YouTube, article, etc.), or any input the pattern should analyze.",
                    required=True
                )
            ]
        )
        for pattern in patterns
    ]


@server.get_prompt()
async def handle_get_prompt(name: str, arguments: dict[str, str] | None) -> types.GetPromptResult:
    """Get a specific prompt by name with optional strategy and input."""
    content = get_pattern_content(name)

    if content is None:
        raise ValueError(f"Pattern '{name}' not found")

    # Prepend strategy if provided
    if arguments and arguments.get("strategy"):
        strategy_name = arguments["strategy"]
        strategy = get_strategy_content(strategy_name)
        if not strategy:
            raise ValueError(f"Strategy '{strategy_name}' not found")
        content = f"{strategy.get('prompt')}\n\n{content}"

    # Append user input if provided
    if arguments and arguments.get("input"):
        user_input = arguments["input"]
        content += f"\n{user_input}"

    return types.GetPromptResult(
        messages=[
            types.PromptMessage(
                role="user",
                content=types.TextContent(
                    type="text",
                    text=content
                )
            )
        ]
    )


# =============================================================================
# Main Entry Point
# =============================================================================

async def main():
    """Initialize and run the MCP server."""
    # Sync repo on startup
    try:
        sync_repo()
    except Exception as e:
        logger.error(f"Failed to sync repo: {e}")
        # Continue anyway - prompts will be empty if repo fails

    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())

