"""
Helper functions for the Fabric MCP Server.

This module contains utility functions for:
- Repository management (sync, clone)
- Pattern and strategy file operations
- Text processing and description extraction
"""

import json
import logging
import shutil
import subprocess
from pathlib import Path
from typing import List, Optional

# Configure logging
logger = logging.getLogger("fabric-mcp-server")

# Configuration
REPO_URL = "https://github.com/danielmiessler/fabric"
REPO_PATH = Path("/app/data/fabric")
PATTERNS_DIRS = ["data/patterns", "patterns"]
STRATEGIES_DIRS = ["data/strategies", "strategies"]


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


def get_strategy_content(name: str) -> Optional[dict]:
    """Load a strategy JSON file and return its content."""
    strategies_dir = get_strategies_dir()
    strategy_file = strategies_dir / f"{name}.json"

    if not strategy_file.exists():
        return None

    try:
        with open(strategy_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            return {
                "description": data.get("description", ""),
                "prompt": data.get("prompt", "") or data.get("content", "")
            }
    except Exception:
        return None


def humanize_name(name: str) -> str:
    """Convert snake_case pattern name to human-readable title.

    Example: 'create_micro_summary' -> 'Create Micro Summary'
    """
    return name.replace("_", " ").replace("-", " ").title()


def extract_pattern_description(system_md_path: Path, max_length: int = 200) -> str:
    """
    Extract a meaningful description from the pattern's system.md file.

    Looks for:
    1. Content after "# IDENTITY and PURPOSE" or "# IDENTITY" header
    2. The first meaningful paragraph starting with "You are..." or similar
    3. Falls back to the first non-empty paragraph

    Args:
        system_md_path: Path to the system.md file
        max_length: Maximum length of the returned description

    Returns:
        Extracted description string, truncated if necessary
    """
    try:
        content = system_md_path.read_text(encoding="utf-8")
    except Exception:
        return ""

    lines = content.split("\n")
    description_lines = []
    in_identity_section = False

    for line in lines:
        stripped = line.strip()

        # Check for IDENTITY and PURPOSE section
        if stripped.lower().startswith("# identity"):
            in_identity_section = True
            continue

        # If we hit another header while in identity section, stop
        if in_identity_section and stripped.startswith("#"):
            break

        # Collect lines in identity section
        if in_identity_section:
            # Skip empty lines at the start
            if not description_lines and not stripped:
                continue
            # Stop at "Take a step back" or similar instruction lines
            if stripped.lower().startswith("take a"):
                break
            if stripped:
                description_lines.append(stripped)
                # Get first paragraph only
                if len(description_lines) >= 3:
                    break

    # If no identity section, look for first "You are..." paragraph
    if not description_lines:
        for line in lines:
            stripped = line.strip()
            if stripped.lower().startswith("you are") or stripped.lower().startswith("you extract"):
                description_lines.append(stripped)
                break

    # Fallback: first non-empty, non-header line
    if not description_lines:
        for line in lines:
            stripped = line.strip()
            if stripped and not stripped.startswith("#"):
                description_lines.append(stripped)
                break

    description = " ".join(description_lines)

    # Truncate if too long
    if len(description) > max_length:
        description = description[:max_length - 3].rsplit(" ", 1)[0] + "..."

    return description


def get_pattern_content(name: str) -> Optional[str]:
    """Read the system.md content for a given pattern name."""
    patterns_dir = get_patterns_dir()
    pattern_file = patterns_dir / name / "system.md"

    if not pattern_file.exists():
        return None

    return pattern_file.read_text(encoding="utf-8")


def list_all_patterns() -> List[dict]:
    """
    List all available patterns with their metadata.

    Returns:
        List of dicts with 'name', 'human_name', 'description', and 'system_md_path'
    """
    patterns_dir = get_patterns_dir()
    if not patterns_dir.exists():
        return []

    patterns = []
    for item in sorted(patterns_dir.iterdir()):
        system_md = item / "system.md"
        if item.is_dir() and system_md.exists():
            extracted_desc = extract_pattern_description(system_md)
            human_name = humanize_name(item.name)

            if extracted_desc:
                description = f"{human_name}: {extracted_desc}"
            else:
                description = f"Fabric pattern: {human_name}"

            patterns.append({
                "name": item.name,
                "human_name": human_name,
                "description": description,
                "system_md_path": system_md
            })

    return patterns


def list_all_strategies() -> List[dict]:
    """
    List all available strategies with their metadata.

    Returns:
        List of dicts with 'name' and 'description'
    """
    strategies_dir = get_strategies_dir()
    if not strategies_dir.exists():
        return []

    strategies = []
    for item in sorted(strategies_dir.glob("*.json")):
        strategy = get_strategy_content(item.stem)
        if strategy:
            strategies.append({
                "name": item.stem,
                "description": strategy.get("description", "No description")
            })

    return strategies

