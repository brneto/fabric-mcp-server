"""
Helper functions for the Fabric MCP Server.

This package contains utility functions organized into modules:
- config: Configuration constants
- repo: Repository management (sync, clone)
- paths: Directory/path utilities
- text: Text processing utilities
- patterns: Pattern operations
- strategies: Strategy operations
"""

# Re-export all public functions for backward compatibility
from .config import (
    REPO_URL,
    REPO_PATH,
    PATTERNS_DIRS,
    STRATEGIES_DIRS,
    MD_RESOURCES_DIR,
    PDF_RESOURCES_DIR,
)

from .repo import (
    run_command,
    sync_repo,
)

from .paths import (
    get_dir_content,
    get_patterns_dir,
    get_strategies_dir,
    get_available_researches,
    ResourceType,
)

from .text import (
    humanize_name,
    extract_pattern_description,
)

from .patterns import (
    get_pattern_content,
    list_all_patterns,
)

from .strategies import (
    get_strategy_content,
    list_all_strategies,
)

__all__ = [
    # Config
    "REPO_URL",
    "REPO_PATH",
    "PATTERNS_DIRS",
    "STRATEGIES_DIRS",
    "MD_RESOURCES_DIR",
    "PDF_RESOURCES_DIR",
    # Repo
    "run_command",
    "sync_repo",
    # Paths
    "get_dir_content",
    "get_patterns_dir",
    "get_strategies_dir",
    "get_available_researches",
    "ResourceType",
    # Text
    "humanize_name",
    "extract_pattern_description",
    # Patterns
    "get_pattern_content",
    "list_all_patterns",
    # Strategies
    "get_strategy_content",
    "list_all_strategies",
]

