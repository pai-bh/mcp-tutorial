from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def call_echo_tool():
    # 서버 파라미터 설정
    server_params = StdioServerParameters(command="python", args=["country_server.py"])

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # 서버 연결 초기화
            await session.initialize()

            # echo_tool 호출
            result = await session.call_tool(
                "get_capital", arguments={"country": "France"}
            )
            print(result)


# 스크립트 실행
if __name__ == "__main__":
    import asyncio

    asyncio.run(call_echo_tool())
