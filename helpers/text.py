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


def slugify(name: str) -> str:
    """Convert a human-readable name to a URL-friendly slug.

    Example: 'The Prompt Report' -> 'the-prompt-report'
    Example: 'the-prompt-report' -> 'the-prompt-report' (already a slug)
    """
    return name.lower().replace("_", "-").replace(" ", "-")


def _find_identity_section_start(lines: list[str]) -> int:
    """Find the index where the IDENTITY section starts, or -1 if not found."""
    for i, line in enumerate(lines):
        if line.strip().lower().startswith("# identity"):
            return i + 1
    return -1


def _should_stop_collecting(stripped: str) -> bool:
    """Check if we should stop collecting description lines."""
    if stripped.startswith("#"):
        return True
    if stripped.lower().startswith("take a"):
        return True
    return False


def _extract_from_identity_section(lines: list[str]) -> list[str]:
    """Extract description lines from the IDENTITY section."""
    start_idx = _find_identity_section_start(lines)
    if start_idx < 0:
        return []

    description_lines = []
    for line in lines[start_idx:]:
        stripped = line.strip()

        if _should_stop_collecting(stripped):
            break

        # Skip empty lines at the start
        if not description_lines and not stripped:
            continue


        if stripped:
            description_lines.append(stripped)
            if len(description_lines) >= 3:
                break

    return description_lines


def _extract_you_are_paragraph(lines: list[str]) -> list[str]:
    """Extract the first 'You are...' or 'You extract...' paragraph."""
    for line in lines:
        stripped = line.strip()
        if stripped.lower().startswith(("you are", "you extract")):
            return [stripped]
    return []


def _extract_first_paragraph(lines: list[str]) -> list[str]:
    """Extract the first non-empty, non-header line."""
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            return [stripped]
    return []


def _truncate_description(description: str, max_length: int) -> str:
    """Truncate description to max_length, breaking at word boundary."""
    if len(description) <= max_length:
        return description
    return description[:max_length - 3].rsplit(" ", 1)[0] + "..."


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

    # Try extraction strategies in order of preference
    description_lines = (
        _extract_from_identity_section(lines)
        or _extract_you_are_paragraph(lines)
        or _extract_first_paragraph(lines)
    )

    description = " ".join(description_lines)
    return _truncate_description(description, max_length)

