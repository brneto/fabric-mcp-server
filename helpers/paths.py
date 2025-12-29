"""
Directory and path utility functions for the Fabric MCP Server.

This module contains functions for:
- Finding directories within the repository
- Discovering available resources
"""

from pathlib import Path
from typing import List

from ._types import ResearchInfo

from .config import REPO_PATH, PATTERNS_DIRS, STRATEGIES_DIRS, RESOURCES_DIR


def get_dir_content(base_path: Path, possible_dirs: List[str]) -> Path:
    """Find the first existing directory from a list of possible paths."""
    for d in possible_dirs:
        path = base_path / d
        if path.exists() and path.is_dir():
            return path
    return base_path / possible_dirs[0]


def get_patterns_dir() -> Path:
    """Get the patterns directory path."""
    return get_dir_content(REPO_PATH, PATTERNS_DIRS)


def get_strategies_dir() -> Path:
    """Get the strategies directory path."""
    return get_dir_content(REPO_PATH, STRATEGIES_DIRS)


def get_available_researches() -> dict[str, ResearchInfo]:
    """
    Dynamically discover all markdown files in the researches folder.
    Returns a dict mapping slug (e.g., 'the-prompt-report') to a dict with 'path' and 'human_name'.
    """
    file_map = {}
    if RESOURCES_DIR.exists():
        for md_file in RESOURCES_DIR.glob("*.md"):
            # Convert filename to URL-friendly slug
            # e.g., 'The_Prompt_Report.md' -> 'the-prompt-report'
            slug = md_file.stem.lower().replace("_", "-").replace(" ", "-")
            # Create a human-readable name from the filename
            human_name = md_file.stem.replace("_", " ").replace("-", " ").title()
            file_map[slug] = ResearchInfo(
                path=md_file,
                human_name=human_name
            )
    return file_map

