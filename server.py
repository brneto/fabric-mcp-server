import asyncio
import json
import logging
import os
import shutil
import subprocess
from pathlib import Path
from typing import List, Optional

from mcp.server import Server
from mcp.server.stdio import stdio_server
import mcp.types as types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("fabric-mcp-server")

# Configuration
REPO_URL = "https://github.com/danielmiessler/fabric"
REPO_PATH = Path("/app/data/fabric")
PATTERNS_DIRS = ["data/patterns", "patterns"]
STRATEGIES_DIRS = ["data/strategies", "strategies"]

server = Server("fabric-mcp-server", version="0.1.0")

def run_command(command: List[str], cwd: Optional[Path] = None) -> None:
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

def sync_repo():
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
    for d in possible_dirs:
        path = base_path / d
        if path.exists() and path.is_dir():
            return path
    return base_path / possible_dirs[0]

def get_strategy_content(name: str) -> Optional[dict]:
    strategies_dir = get_dir_content(REPO_PATH, STRATEGIES_DIRS)
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

@server.list_tools()
async def handle_list_tools() -> List[types.Tool]:
    return [
        types.Tool(
            name="list_strategies",
            description="List all available strategies with their descriptions",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> List[types.TextContent]:
    if name == "list_strategies":
        strategies_dir = get_dir_content(REPO_PATH, STRATEGIES_DIRS)
        if not strategies_dir.exists():
            return [types.TextContent(type="text", text="No strategies found")]

        result = []
        for item in sorted(strategies_dir.glob("*.json")):
            strategy = get_strategy_content(item.stem)
            if strategy:
                desc = strategy.get("description", "No description")
                result.append(f"- **{item.stem}**: {desc}")

        if not result:
            return [types.TextContent(type="text", text="No strategies found")]

        return [types.TextContent(type="text", text="\n".join(result))]

    raise ValueError(f"Unknown tool: {name}")

@server.list_prompts()
async def handle_list_prompts() -> List[types.Prompt]:
    patterns_dir = get_dir_content(REPO_PATH, PATTERNS_DIRS)
    if not patterns_dir.exists():
        return []

    # Collect strategies to list them in description or arguments?
    # The requirement is "option to include a strategies to each prompt".
    # We can add an argument "strategy" to each prompt.
    prompts = []
    for item in patterns_dir.iterdir():
        if item.is_dir() and (item / "system.md").exists():
            prompts.append(
                types.Prompt(
                    name=item.name,
                    description=f"Fabric pattern: {item.name}",
                    arguments=[
                        types.PromptArgument(
                            name="strategy",
                            description="Optional strategy to apply (e.g. 'cot')",
                            required=False
                        ),
                        types.PromptArgument(
                            name="input",
                            description="User input to process (text, URL, etc.)",
                            required=True # Force client to ask for input
                        )
                    ]
                )
            )
    
    return sorted(prompts, key=lambda x: x.name)

@server.get_prompt()
async def handle_get_prompt(name: str, arguments: dict[str, str] | None) -> types.GetPromptResult:
    patterns_dir = get_dir_content(REPO_PATH, PATTERNS_DIRS)
    pattern_file = patterns_dir / name / "system.md"
    
    if not pattern_file.exists():
        raise ValueError(f"Pattern '{name}' not found")
        
    content = pattern_file.read_text(encoding="utf-8")

    # Prepend strategy if provided
    if arguments and arguments.get("strategy"):
        strategy_name = arguments["strategy"]
        strategy = get_strategy_content(strategy_name)
        if not strategy:
            raise ValueError(f"Strategy '{strategy_name}' not found")
        content = f"{strategy.get('prompt')}\n\n{content}"

    # Append user input if provided
    if arguments and arguments.get("input"):
        user_input = arguments["input"]
        content += f"\n{user_input}"

    return types.GetPromptResult(
        messages=[
            types.PromptMessage(
                role="user",
                content=types.TextContent(
                    type="text",
                    text=content
                )
            )
        ]
    )

async def main():
    # Sync repo on startup
    try:
        sync_repo()
    except Exception as e:
        logger.error(f"Failed to sync repo: {e}")
        # Continue? If repo fails, prompts will be empty.
    
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())