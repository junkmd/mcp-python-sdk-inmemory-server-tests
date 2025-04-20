import contextlib
from collections.abc import AsyncIterator

import pytest
from mcp.client.session import ClientSession
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_client_session,
)
from mcp.types import TextContent

import mcpserver


@contextlib.asynccontextmanager
async def create_client() -> AsyncIterator[ClientSession]:
    async with create_client_session(mcpserver.mcp._mcp_server) as client:
        yield client


ASYNCIO_EVENT_LOOP_ERR_MSG = "asyncio.run() cannot be called from a running event loop"


class Test_FromClient:
    @pytest.mark.asyncio
    async def test_greet_asyncio_run(self):
        async with create_client() as client:
            res = await client.call_tool("greet_asyncio_run", {"name": "you"})
            cnt = res.content[0]
            assert isinstance(cnt, TextContent)
            assert cnt.text != "Hello, you!"  # CHECK THIS OUT!
            assert ASYNCIO_EVENT_LOOP_ERR_MSG in cnt.text
            assert res.isError  # CHECK THIS OUT!

    @pytest.mark.asyncio
    async def test_greet(self):
        async with create_client() as client:
            res = await client.call_tool("greet", {"name": "you"})
            cnt = res.content[0]
            assert isinstance(cnt, TextContent)
            assert cnt.text == "Hello, you!"

    @pytest.mark.asyncio
    async def test_add(self):
        async with create_client() as client:
            res = await client.call_tool("add", {"a": 1, "b": 2})
            cnt = res.content[0]
            assert isinstance(cnt, TextContent)
            assert cnt.text == "3"

    @pytest.mark.asyncio
    async def test_multiply(self):
        async with create_client() as client:
            res = await client.call_tool("multiply", {"a": 2, "b": 3})
            cnt = res.content[0]
            assert isinstance(cnt, TextContent)
            assert cnt.text == "6"
