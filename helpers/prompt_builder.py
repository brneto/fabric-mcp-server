"""
Prompt building utilities for the Fabric MCP Server.

This module consolidates the logic for:
- Building prompts from patterns with optional strategy
- Appending user input to prompts
"""

from .patterns import get_pattern_content
from .strategies import get_strategy_content


def build_prompt(
    pattern_name: str,
    user_input: str | None = None,
    strategy_name: str | None = None,
) -> str:
    """
    Build a complete prompt from a pattern with optional strategy and user input.

    Args:
        pattern_name: The name of the pattern to use
        user_input: Optional user input to append
        strategy_name: Optional strategy name to prepend

    Returns:
        The complete prompt string

    Raises:
        ValueError: If pattern or strategy is not found
    """
    content = get_pattern_content(pattern_name)
    if content is None:
        raise ValueError(f"Pattern '{pattern_name}' not found")
    
    # Append user input if provided
    if user_input:
        content += f"{user_input}"

    # Append strategy if provided
    if strategy_name:
        strategy = get_strategy_content(strategy_name)
        if not strategy:
            raise ValueError(f"Strategy '{strategy_name}' not found")
        content += f"\n\n{strategy.get('prompt')}"

    return content

