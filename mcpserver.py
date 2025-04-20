import asyncio

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mymcpserver")


async def say_hello(name: str) -> str:
    await asyncio.sleep(0.05)
    return f"Hello, {name}!"


@mcp.tool()
def greet_asyncio_run(name: str) -> int:
    """DO NOT USE! ~Say hello to a person.~"""
    return asyncio.run(say_hello(name))


@mcp.tool()
async def greet(name: str) -> int:
    """Say hello to a person."""
    return await say_hello(name)


@mcp.tool()
async def add(a: int, b: int) -> int:
    """Add two numbers"""
    await asyncio.sleep(0.05)
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b
