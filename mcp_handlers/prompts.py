"""
MCP Prompts for the Fabric MCP Server.

This module contains prompt handlers for:
- Listing all Fabric patterns as prompts
- Getting specific prompts with optional strategy and input
"""

from typing import List, Optional

import mcp.types as types

from helpers import (
    get_strategy_content,
    get_pattern_content,
    list_all_patterns,
    list_all_strategies,
)


def list_prompts() -> List[types.Prompt]:
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


def get_prompt(name: str, arguments: Optional[dict[str, str]]) -> types.GetPromptResult:
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

