"""
MCP Prompts for the Fabric MCP Server.

This module contains prompt handlers for:
- Listing all Fabric patterns as prompts
- Getting specific prompts with optional strategy and input
"""

import mcp.types as types

from helpers import (
    list_all_patterns,
    list_all_strategies,
    build_prompt,
)


def list_prompts() -> list[types.Prompt]:
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
            title=pattern["human_name"],
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


def get_prompt(name: str, arguments: dict[str, str] | None) -> types.GetPromptResult:
    """Get a specific prompt by name with optional strategy and input."""
    strategy_name = arguments.get("strategy") if arguments else None
    user_input = arguments.get("input") if arguments else None

    try:
        content = build_prompt(name, user_input, strategy_name)
    except ValueError as e:
        raise ValueError(str(e))

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

