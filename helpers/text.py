"""
Text processing utility functions for the Fabric MCP Server.

This module contains functions for:
- Converting names to human-readable format
- Extracting descriptions from markdown files
"""

from pathlib import Path


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
    except OSError:
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

