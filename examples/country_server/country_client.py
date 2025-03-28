from typing import Any, Dict, Optional

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


class MCPClient:
    def __init__(self, server_path: str):
        self.server_params = StdioServerParameters(command="python", args=[server_path])

    async def list_tools(self, print_result: bool = True):
        """사용 가능한 도구 목록 조회"""
        async with stdio_client(self.server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.list_tools()
                if print_result:
                    print(result)

    async def execute_tool(
        self, name: str, arguments: Dict[str, Any], print_result: bool = True
    ):
        """MCP 도구를 실행하는 메서드"""
        async with stdio_client(self.server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.call_tool(name=name, arguments=arguments)
                if print_result:
                    print(result)

    async def get_prompt(
        self,
        name: str,
        arguments: Optional[Dict[str, str]] = None,
        print_result: bool = True,
    ):
        """프롬프트 조회"""
        async with stdio_client(self.server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.get_prompt(name=name, arguments=arguments)
                if print_result:
                    print(result)


async def main():
    client = MCPClient("examples/country_server/country_server.py")

    # 클라이언트 요청예시 1 : 도구 목록 조회
    await client.list_tools()

    # 클라이언트 요청예시 2 : 도구 실행
    await client.execute_tool(name="get_capital", arguments={"country": "프랑스"})

    # 클라이언트 요청예시 3: 프롬프트 조회
    await client.get_prompt(name="country_info_prompt", arguments={"country": "프랑스"})


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
