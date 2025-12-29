"""
Repository management functions for the Fabric MCP Server.

This module contains functions for:
- Cloning the Fabric repository
- Updating/syncing the repository
- Executing shell commands
"""

import logging
import shutil
import subprocess
from pathlib import Path
from typing import List, Optional

from .config import REPO_URL, REPO_PATH

# Configure logging
logger = logging.getLogger("fabric-mcp-server")


def run_command(command: List[str], cwd: Optional[Path] = None) -> None:
    """Execute a shell command with error handling."""
    try:
        subprocess.run(
            command,
            cwd=cwd,
            check=True,
            capture_output=True,
            text=True
        )
    except subprocess.CalledProcessError as e:
        logger.error(f"Command failed: {e.cmd}")
        logger.error(f"Stdout: {e.stdout}")
        logger.error(f"Stderr: {e.stderr}")
        raise


def sync_repo() -> None:
    """Clone or update the Fabric repository."""
    if REPO_PATH.exists():
        if (REPO_PATH / ".git").exists():
            logger.info("Updating existing repository...")
            run_command(["git", "pull"], cwd=REPO_PATH)
            logger.info("Repository updated successfully")
        else:
            logger.warning("Directory exists but is not a git repo. Removing and cloning...")
            shutil.rmtree(REPO_PATH)
            run_command(["git", "clone", REPO_URL, str(REPO_PATH)])
            logger.info("Repository cloned successfully")
    else:
        logger.info("Cloning repository...")
        REPO_PATH.parent.mkdir(parents=True, exist_ok=True)
        run_command(["git", "clone", REPO_URL, str(REPO_PATH)])
        logger.info("Repository cloned successfully")

