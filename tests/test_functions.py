import asyncio

import mcpserver


class Test_Functions:
    def test_greet_asyncio_run(self):
        assert mcpserver.greet_asyncio_run("you") == "Hello, you!"

    def test_greet(self):
        assert asyncio.run(mcpserver.greet("you")) == "Hello, you!"

    def test_add(self):
        assert asyncio.run(mcpserver.add(1, 2)) == 3

    def test_multiply(self):
        assert mcpserver.multiply(2, 3) == 6
