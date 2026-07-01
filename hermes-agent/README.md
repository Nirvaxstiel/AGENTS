# Installation

1. Replace SOUL.md
2. Open up config.yaml
3. Copy and append/paste the contents to the existing config.yaml in .hermes
4. Run `hermes setup` and ensure these keys are set:
   - EXA_API_KEY=
   - OPENCODE_ZEN_API_KEY=
   - HERMES_MAX_ITERATIONS=
   - OPENROUTER_API_KEY=
5. Also configure/migrate skills while you are in `hermes setup`.
6. Copy the codebase-memory-mcp-shim.py to `~/.local/bin`.
