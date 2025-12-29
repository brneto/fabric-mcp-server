"""
Configuration constants for the Fabric MCP Server.

This module contains all configuration values used throughout the application.
"""

from pathlib import Path


# Repository configuration
REPO_URL = "https://github.com/danielmiessler/fabric"
REPO_PATH = Path("/app/data/fabric")

# Directory paths within the repository
PATTERNS_DIRS = ["data/patterns", "patterns"]
STRATEGIES_DIRS = ["data/strategies", "strategies"]

# Local resources directory
RESOURCES_DIR = Path(__file__).parent.parent / "resources" / "markdown" / "researches"

