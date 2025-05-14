[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/junkmd-mcp-python-sdk-inmemory-server-tests-badge.png)](https://mseep.ai/app/junkmd-mcp-python-sdk-inmemory-server-tests)

# mcp-python-sdk-inmemory-server-tests

This repository provides example code and tests for developing robust MCP tools.  
It demonstrates how unit tests on individual functions can miss asynchronous pitfalls like `asyncio.run` in tools.  
A more reliable testing approach using in-memory client sessions is showcased.

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
