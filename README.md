# Fabric MCP Server (Docker)

A Model Context Protocol (MCP) server that exposes [Daniel Miessler's Fabric](https://github.com/danielmiessler/fabric) patterns and strategies to MCP-compliant clients. It automatically syncs with the upstream Fabric repository, allowing you to use its powerful prompts directly within your AI workflow.

## Features

- **Dynamic Sync**: Clones or updates the Fabric repository every time the server starts.
- **Pattern Prompts**: Automatically creates an MCP prompt for every folder in `patterns/`.
- **Smart Descriptions**: Extracts meaningful descriptions from each pattern's `system.md` file to help LLMs understand when to use each pattern.
- **Strategy Support**: Every prompt includes an optional `strategy` argument to prepend context from `strategies/`. Natural language phrases like "with strategy cot" or "using cot strategy" are recognized.
- **User Input**: Every prompt requires an `input` argument for user-provided content (text, URL, etc.).
- **List Patterns Tool**: Exposes a `list_patterns` tool so AI agents can discover available Fabric patterns programmatically.
- **List Strategies Tool**: Exposes a `list_strategies` tool to discover available strategies and their descriptions.

## Prerequisites

- [Docker](https://docs.docker.com/) installed and running.

## Build

Build the Docker image locally:

```bash
docker build -t fabric-mcp-server .
```

## Running the Server

### 1. Manual Test (Stdio)
To test if the server starts and syncs the repository correctly:

```bash
docker run -i fabric-mcp-server
```
*Note: The server communicates via JSON-RPC over stdin/stdout. You will see logs on stderr and can interact via the MCP Inspector.*

### 2. Access via MCP Gateway (Claude Desktop, etc.)

To use this server with a gateway like **Claude Desktop**, add the following to your `claude_desktop_config.json` (usually located at `~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

```json
{
  "mcpServers": {
    "fabric": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "fabric-mcp-server"
      ]
    }
  }
}
```

### 3. Access via Gemini CLI

To use this server with the **Gemini CLI**, add the following to your `~/.gemini/settings.json`:

```json
{
  "mcpServers": {
    "fabric": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "fabric-mcp-server"
      ]
    }
  }
}
```

### 4. Usage with MCP Gateway "Run" Command

If you are using a gateway that supports running servers via a direct command string, use:

```bash
docker run -i --rm fabric-mcp-server
```

### 4. Usage via Docker MCP Gateway

If you are using the **Docker MCP Gateway** CLI, you can run this server directly using:

```bash
docker mcp gateway run fabric-mcp-server
```

### 5. Global Registration (Docker MCP Catalog)

To make this server visible to all Docker MCP clients (like the `docker mcp` CLI) using the configuration files in `~/.docker/mcp/`:

1.  **Build the Image**:
    ```bash
    docker build -t fabric-mcp-server .
    ```

2.  **Create a Local Catalog**:
    Create a file named `local.yaml` in your catalogs directory (usually `~/.docker/mcp/catalogs/local.yaml`):

    ```yaml
    version: 3
    name: local-catalog
    displayName: Local Catalog
    registry:
      fabric:
        title: Fabric
        description: Fabric patterns and strategies
        type: server
        image: fabric-mcp-server:latest
        tools:
          - list_patterns
          - list_strategies
        prompts: []  # One prompt per pattern in the Fabric repository
        resources: {}
        metadata:
          category: productivity
          tags:
            - fabric
            - ai
            - prompts
          owner: local
    ```

3.  **Enable the Server**:
    Edit your registry file (usually `~/.docker/mcp/registry.yaml`) and add the `fabric` entry under `registry:`:

    ```yaml
    registry:
      # ... other servers ...
      fabric:
        ref: ""
    ```

4.  **Verify**:
    Run `docker mcp list` (if available) or simply try running it:
    ```bash
    docker mcp gateway run fabric
    ```

## How it Works

1. **Startup**: The server clones `https://github.com/danielmiessler/fabric` into the container.
2. **Prompts**: It scans folders like `extract_wisdom`, `summarize`, etc. in `patterns/`.
3. **Execution**:
   - When you select a prompt (e.g., `extract_wisdom`), it reads the `system.md` file.
   - If you provide a `strategy` (e.g., `cot`), it fetches the strategy JSON, extracts the prompt content, and **prepends** it to the system message.
   - The `input` argument content is **appended** to the end of the prompt.
4. **Tools**: 
   - Use `list_patterns` to discover all available Fabric patterns.
   - Use `list_strategies` to discover available strategies and their descriptions.

## MCP Prompts vs Tools

> **Important Note**: In the strict Model Context Protocol (MCP) definition, **Prompts** are templates exposed by servers for the client (you) to use, while **Tools** are functions the AI agent can call directly.
>
> As an AI agent, LLMs primarily see Tools. They may not have direct visibility into user-facing Prompts (like `analyze_bill_short` or `youtube_summary`) from connected MCP servers. Those are typically accessed via your client's UI (e.g., typing `/` in your chat interface with Claude Desktop).
>
> This is why we expose both:
> - **Prompts**: For clients that support the `/` command interface
> - **`list_patterns` Tool**: So AI agents can programmatically discover and reference available patterns

## Usage Examples

### Using Prompts via Client UI

MCP Prompts are accessed through your client's UI. For example, in Claude Desktop, type `/` followed by the pattern name:

| Client Action | Result |
|--------------|--------|
| Type `/create_micro_summary` | Invokes the pattern with prompts for `input` (required) and `strategy` (optional) |
| Type `/summarize` | Invokes the summarize pattern |
| Type `/extract_wisdom` | Invokes the extract wisdom pattern |

### Using Tools via Natural Language

AI agents can use the available tools to discover patterns and strategies:

| Natural Language Prompt | Tool Called |
|------------------------|-------------|
| "What Fabric patterns are available?" | `list_patterns` |
| "Show me the available strategies" | `list_strategies` |
| "List all patterns for summarization" | `list_patterns` (then filters results) |

### Prompt Arguments

When invoking a prompt (via `/` command), you can provide:

| Argument | Required | Description | Example |
|----------|----------|-------------|---------|
| `input` | Yes | The content to analyze (text, URL, etc.) | `https://youtu.be/abc123` |
| `strategy` | No | Thinking strategy to enhance analysis | `cot`, `tot` |

**Tip**: For best results when using strategies, include phrases like:
- "with strategy cot"
- "using strategy tot"  
- "apply cot strategy"

