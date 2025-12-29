"""
Type definitions for the helpers package.

This module contains TypedDict classes for structured dictionary types
used by helper functions.

Note: The underscore prefix indicates this is an internal module,
and avoids conflict with Python's built-in 'types' module.
"""

from pathlib import Path
from typing import TypedDict


class ResearchInfo(TypedDict):
    """Type definition for research document metadata."""
    path: Path
    human_name: str


class StrategyContent(TypedDict):
    """Type definition for strategy content."""
    description: str
    prompt: str


class PatternInfo(TypedDict):
    """Type definition for pattern metadata."""
    name: str
    human_name: str
    description: str
    system_md_path: Path


class StrategyInfo(TypedDict):
    """Type definition for strategy metadata."""
    name: str
    description: str

