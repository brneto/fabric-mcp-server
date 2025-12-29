"""
Strategy operations for the Fabric MCP Server.

This module contains functions for:
- Reading strategy content
- Listing all available strategies
"""

import json
from typing import List, Optional

from ._types import StrategyContent, StrategyInfo

from .paths import get_strategies_dir


def get_strategy_content(name: str) -> Optional[StrategyContent]:
    """Load a strategy JSON file and return its content."""
    strategies_dir = get_strategies_dir()
    strategy_file = strategies_dir / f"{name}.json"

    if not strategy_file.exists():
        return None

    try:
        with open(strategy_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            return StrategyContent(
                description=data.get("description", ""),
                prompt=data.get("prompt", "") or data.get("content", "")
            )
    except (OSError, json.JSONDecodeError):
        return None


def list_all_strategies() -> List[StrategyInfo]:
    """
    List all available strategies with their metadata.

    Returns:
        List of StrategyInfo dicts with 'name' and 'description'
    """
    strategies_dir = get_strategies_dir()
    if not strategies_dir.exists():
        return []

    strategies = []
    for item in sorted(strategies_dir.glob("*.json")):
        strategy = get_strategy_content(item.stem)
        if strategy:
            strategies.append(StrategyInfo(
                name=item.stem,
                description=strategy.get("description", "No description")
            ))

    return strategies

