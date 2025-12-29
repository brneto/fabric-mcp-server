"""
Directory and path utility functions for the Fabric MCP Server.

This module contains functions for:
- Finding directories within the repository
- Discovering available resources
"""

from pathlib import Path
from typing import List, Literal

from ._types import ResearchInfo

from .config import REPO_PATH, PATTERNS_DIRS, STRATEGIES_DIRS, MD_RESOURCES_DIR, PDF_RESOURCES_DIR

# Type alias for resource types
ResourceType = Literal["markdown", "pdf"]

# Mapping of resource types to their configurations
_RESOURCE_CONFIG = {
    "markdown": {"dir": MD_RESOURCES_DIR, "extension": "*.md"},
    "pdf": {"dir": PDF_RESOURCES_DIR, "extension": "*.pdf"},
}


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


def get_available_researches(resource_type: ResourceType = "markdown") -> dict[str, ResearchInfo]:
    """
    Dynamically discover research files in the specified resources folder.

    Args:
        resource_type: Type of resource to discover ("markdown" or "pdf")

    Returns:
        Dict mapping slug (e.g., 'the-prompt-report') to ResearchInfo with 'path' and 'human_name'.
    """
    config = _RESOURCE_CONFIG[resource_type]
    resources_dir = config["dir"]
    extension = config["extension"]

    file_map = {}
    if resources_dir.exists():
        for resource_file in resources_dir.glob(extension):
            # Convert filename to URL-friendly slug
            # e.g., 'The_Prompt_Report.md' -> 'the-prompt-report'
            slug = resource_file.stem.lower().replace("_", "-").replace(" ", "-")
            # Create a human-readable name from the filename
            human_name = resource_file.stem.replace("_", " ").replace("-", " ").title()
            file_map[slug] = ResearchInfo(
                path=resource_file,
                human_name=human_name
            )
    return file_map


