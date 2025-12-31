"""
Pattern operations for the Fabric MCP Server.

This module contains functions for:
- Reading pattern content
- Listing all available patterns
"""

from ._types import PatternInfo

from .paths import get_patterns_dir
from .text import humanize_name, extract_pattern_description


def get_pattern_content(name: str) -> str | None:
    """Read the system.md content for a given pattern name."""
    patterns_dir = get_patterns_dir()
    pattern_file = patterns_dir / name / "system.md"

    if not pattern_file.exists():
        return None

    return pattern_file.read_text(encoding="utf-8")


def list_all_patterns() -> list[PatternInfo]:
    """
    List all available patterns with their metadata.

    Returns:
        List of PatternInfo dicts with 'name', 'human_name', 'description', and 'system_md_path'
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

            # Add usage hint to help LLM understand how to invoke with strategy
            description += " [Supports optional 'strategy' argument like 'cot', 'tot' for enhanced reasoning]"

            patterns.append(PatternInfo(
                name=item.name,
                human_name=human_name,
                description=description,
                system_md_path=system_md
            ))

    return patterns

