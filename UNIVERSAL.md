## MCP Servers

```nu
# Jcodemunch (stdio)
uvx jcodemunch-mcp

# Nushell (stdio)
nu --mcp

# Context7 (optional)
bunx -y @upstash/context7-mcp # you can use others

# codebase-memory-mcp
Invoke-WebRequest -Uri https://raw.githubusercontent.com/DeusData/codebase-memory-mcp/main/install.ps1 -OutFile install.ps1
curl -fsSL https://raw.githubusercontent.com/DeusData/codebase-memory-mcp/main/install.sh | bash
codebase-memory-mcp config set auto_index true

# graphifyy
uv tool install graphifyy
uv tool install "graphifyy[mcp]"
graphify install --platform hermes
graphify install --platform agents # (~/.agents/skills)
```

## Skills

```nu
# macOS / Linux / WSL / Git Bash
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash

# Windows (PowerShell)
irm https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.ps1 | iex
```
