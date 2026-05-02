# Installation

This is an optional custom tabbed agent.

1. Copy to `~/.config/opencode`

## Tachikoma

`/Tachikoma-Agent-Skills` - Custom tabbed agent that uses skills and tools.
`/tachikoma-mcp` - tools that tachikoma can use

### Tachikoma Agent Skills

- Install globally for opencode `~/.config/opencode`
- Or, locally in `your-repo/.opencode`

### Tachikoma-MCP

To be used by the Tachikoma Agent.

- Clone this in a separate directory.
- `uv sync`
- Configure the MCP via opencode.json
- Point the stdio binary to `.venv/Scripts/tachikoma-mcp.exe`
