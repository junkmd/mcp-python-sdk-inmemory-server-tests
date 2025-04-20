# mcp-python-sdk-inmemory-server-tests

## Commands
Setup:
```sh
curl https://get.volta.sh | bash
volta install node
npm install
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync --frozen
```

Run tests:
```sh
uv run pytest tests/.
```

Test and debug `mcpserver.py` with the [MCP Inspector](https://github.com/modelcontextprotocol/inspector):
```sh
uv run mcp dev mcpserver.py
```

Format codebases:
```sh
uv run ruff format .
uv run ruff check --select I --fix .
```
