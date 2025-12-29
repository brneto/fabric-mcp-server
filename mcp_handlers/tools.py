"""
MCP Tools for the Fabric MCP Server.

This module contains tool handlers for:
- list_strategies: List all available strategies
- list_patterns: List all available Fabric patterns
- execute_pattern: Execute a Fabric pattern with content
"""

from typing import List

import mcp.types as types

from helpers import (
    get_strategy_content,
    get_pattern_content,
    list_all_patterns,
    list_all_strategies,
)


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
        )
    ]


def call_tool(name: str, arguments: dict) -> List[types.TextContent]:
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

    if name == "execute_pattern":
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

    raise ValueError(f"Unknown tool: {name}")

