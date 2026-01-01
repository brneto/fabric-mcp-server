"""
Directory and path utility functions for the Fabric MCP Server.

This module contains functions for:
- Finding directories within the repository
- Discovering available resources
"""

from pathlib import Path

from ._types import ResearchInfo, ResourceType

from .config import REPO_PATH, PATTERNS_DIRS, STRATEGIES_DIRS, MD_RESOURCES_DIR, PDF_RESOURCES_DIR
from .text import slugify, humanize_name


# Mapping of resource types to their configurations
_RESOURCE_CONFIG = {
    "markdown": {"dir": MD_RESOURCES_DIR, "extension": "*.md"},
    "pdf": {"dir": PDF_RESOURCES_DIR, "extension": "*.pdf"},
}


def get_dir_content(base_path: Path, possible_dirs: list[str]) -> Path:
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
            # Convert filename to URL-friendly slug using centralized slugify
            slug = slugify(resource_file.stem)
            # Create a human-readable name from the filename
            human_name = humanize_name(resource_file.stem)
            file_map[slug] = ResearchInfo(
                path=resource_file,
                human_name=human_name
            )
    return file_map


