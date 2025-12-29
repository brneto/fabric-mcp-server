# Fabric MCP Server (Docker)

A Model Context Protocol (MCP) server that exposes [Daniel Miessler's Fabric](https://github.com/danielmiessler/fabric) patterns and strategies to MCP-compliant clients. It automatically syncs with the upstream Fabric repository, allowing you to use its powerful prompts directly within your AI workflow.

## Features

- **Dynamic Sync**: Clones or updates the Fabric repository every time the server starts.
- **Pattern Prompts**: Automatically creates an MCP prompt for every folder in `patterns/`.
- **Smart Descriptions**: Extracts meaningful descriptions from each pattern's `system.md` file to help LLMs understand when to use each pattern.
- **Strategy Support**: Every prompt includes an optional `strategy` argument to prepend context from `strategies/`. Natural language phrases like "with strategy cot" or "using cot strategy" are recognized.
- **User Input**: Every prompt requires an `input` argument for user-provided content (text, URL, etc.).
- **Execute Pattern Tool**: Exposes an `execute_pattern` tool so AI agents can execute any Fabric pattern programmatically with optional strategy.
- **List Patterns Tool**: Exposes a `list_patterns` tool so AI agents can discover available Fabric patterns programmatically.
- **List Strategies Tool**: Exposes a `list_strategies` tool to discover available strategies and their descriptions.
- **Research Resources**: Exposes research documents as MCP resources in both markdown and PDF formats, accessible via custom URIs (e.g., `markdown://researches/the-prompt-report`, `pdf://researches/the-prompt-report`).
- **Resource Subscriptions**: Supports subscribing to markdown resource changes, notifying clients when files are modified.

## Project Structure

```
fabric-mcp-server/
├── server.py              # Main entry point, MCP server registration
├── Dockerfile
├── pyproject.toml
│
├── helpers/               # Helper utilities package
│   ├── __init__.py        # Re-exports all functions
│   ├── _types.py          # TypedDict definitions
│   ├── config.py          # Configuration constants
│   ├── repo.py            # Repository management (sync, clone)
│   ├── paths.py           # Directory/path utilities
│   ├── text.py            # Text processing utilities
│   ├── patterns.py        # Pattern operations
│   └── strategies.py      # Strategy operations
│
├── mcp_handlers/          # MCP protocol handlers package
│   ├── __init__.py        # Re-exports all handlers
│   ├── tools.py           # Tool handlers (list_patterns, execute_pattern, etc.)
│   ├── resources.py       # Resource handlers (research documents)
│   └── prompts.py         # Prompt handlers (Fabric patterns as prompts)
│
└── resources/
    ├── markdown/
    │   └── researches/    # Markdown research documents exposed as MCP resources
    └── pdf/
        └── researches/    # PDF research documents exposed as MCP resources
```

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

### 5. Usage via Docker MCP Gateway

If you are using the **Docker MCP Gateway** CLI, you can run this server directly using:

```bash
docker mcp gateway run fabric-mcp-server
```

### 6. Global Registration (Docker MCP Catalog)

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
          - execute_pattern
          - list_patterns
          - list_strategies
          - list_research_resources
          - read_research_resource
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
3. **Resources**: It scans the `resources/markdown/researches/` and `resources/pdf/researches/` folders for research documents and exposes them as MCP resources with custom URIs.
4. **Subscriptions**: Clients can subscribe to markdown resource changes. The server monitors the markdown resources folder and sends notifications when files are modified (PDF subscriptions are not supported).
5. **Execution**:
   - When you select a prompt (e.g., `extract_wisdom`), it reads the `system.md` file.
   - If you provide a `strategy` (e.g., `cot`), it fetches the strategy JSON, extracts the prompt content, and **prepends** it to the system message.
   - The `input` argument content is **appended** to the end of the prompt.
6. **Tools**: 
   - Use `execute_pattern` to run any Fabric pattern with content and optional strategy.
   - Use `list_patterns` to discover all available Fabric patterns.
   - Use `list_strategies` to discover available strategies and their descriptions.
   - Use `list_research_resources` to discover all available research documents.
   - Use `read_research_resource` to read a specific research document by name (supports both human-readable names like "The Prompt Report" and slugs like "the-prompt-report").

## MCP Prompts, Tools, and Resources

> **Important Note**: In the Model Context Protocol (MCP):
> - **Prompts** are templates exposed by servers for the client (you) to use
> - **Tools** are functions the AI agent can call directly
> - **Resources** are data sources (files, documents) that can be read by clients
>
> As an AI agent, LLMs primarily see Tools. They may not have direct visibility into user-facing Prompts (like `analyze_bill_short` or `youtube_summary`) from connected MCP servers. Those are typically accessed via your client's UI (e.g., typing `/` in your chat interface with Claude Desktop).
>
> This is why we expose:
> - **Prompts**: For clients that support the `/` command interface
> - **`execute_pattern` Tool**: So AI agents can run any pattern programmatically via natural language
> - **`list_patterns` Tool**: So AI agents can discover available patterns
> - **`list_research_resources` Tool**: So AI agents can discover available research documents
> - **`read_research_resource` Tool**: So AI agents can read research documents via natural language
> - **Resources**: Research documents accessible via `markdown://researches/{title}` and `pdf://researches/{title}` URIs

## Usage Examples

### Using Prompts via Client UI

MCP Prompts are accessed through your client's UI. For example, in Claude Desktop, type `/` followed by the pattern name:

| Client Action | Result |
|--------------|--------|
| Type `/create_micro_summary` | Invokes the pattern with prompts for `input` (required) and `strategy` (optional) |
| Type `/summarize` | Invokes the summarize pattern |
| Type `/extract_wisdom` | Invokes the extract wisdom pattern |

### Using Tools via Natural Language

AI agents can use the available tools to discover and execute patterns:

| Natural Language Prompt | Tool Called | Arguments |
|------------------------|-------------|-----------|
| "What Fabric patterns are available?" | `list_patterns` | - |
| "Show me the available strategies" | `list_strategies` | - |
| "What research documents are available?" | `list_research_resources` | - |
| "List all research papers" | `list_research_resources` | - |
| "Read the Prompt Report research paper" | `read_research_resource` | `name="The Prompt Report"` or `name="the-prompt-report"` |
| "Show me the content of the prompt report" | `read_research_resource` | `name="the-prompt-report"`, `format="markdown"` |
| "Summarize the key findings from the prompt report" | `read_research_resource` | `name="the-prompt-report"` |
| "Create a micro summary of https://youtu.be/abc123" | `execute_pattern` | `pattern="create_micro_summary"`, `input="https://youtu.be/abc123"` |
| "Summarize this article with strategy cot: https://example.com/article" | `execute_pattern` | `pattern="summarize"`, `input="https://example.com/article"`, `strategy="cot"` |
| "Extract wisdom using chain-of-thought from this text: [text]" | `execute_pattern` | `pattern="extract_wisdom"`, `input="[text]"`, `strategy="cot"` |

### Using Resources

MCP Resources are data sources exposed by the server. Research documents are available in both markdown and PDF formats via custom URIs:

| Resource URI | Description |
|-------------|-------------|
| `markdown://researches/the-prompt-report` | The Prompt Report (Markdown format) |
| `pdf://researches/the-prompt-report` | The Prompt Report (PDF format) |

#### Accessing Resources via Client UI

MCP Resources are accessed differently than Prompts. In Gemini CLI, use the `@` prefix to reference and embed resource content into your chat:

| Feature | Access Method | Function |
|---------|---------------|----------|
| MCP Prompts | `/<name>` | Runs a pre-defined prompt template |
| MCP Resources | `@<uri>` | Fetches and attaches data (files, docs) to your message |

| Client Action | Result |
|--------------|--------|
| Type `@fabric:markdown://researches/the-prompt-report` | Embeds the markdown research document into your chat context |
| Type `@fabric:pdf://researches/the-prompt-report` | Embeds the PDF research document into your chat context |

**Tip**: Type `@` in Gemini CLI to see auto-completion for all available resources from connected MCP servers.

**Example usage**:
```
@fabric:markdown://researches/the-prompt-report Summarize the key findings from this research paper
```

#### Adding New Resources

To add new research documents:
- Place markdown files in `resources/markdown/researches/`
- Place PDF files in `resources/pdf/researches/`

Files will be automatically discovered and exposed with a URL-friendly slug based on the filename.

#### Resource Subscriptions

Clients can subscribe to **markdown** resource changes to receive notifications when files are modified:

- **Subscribe**: Call `resources/subscribe` with a markdown resource URI to start receiving change notifications
- **Unsubscribe**: Call `resources/unsubscribe` to stop receiving notifications

When a subscribed markdown file is modified, the server sends a `notifications/resources/updated` notification to the client.

> **Note**: PDF resources do not support subscriptions.

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

