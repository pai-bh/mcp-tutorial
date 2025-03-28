from mcp.server.fastmcp import FastMCP

# MCP 서버 생성
mcp = FastMCP("Demo Server")


# 간단한 계산기 도구 추가
@mcp.tool()
def add(a: int, b: int) -> int:
    """두 숫자를 더합니다."""
    return a + b


# 간단한 리소스 추가
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """개인화된 인사말을 반환합니다."""
    return f"안녕하세요, {name}님!"


# 프롬프트 추가
@mcp.prompt()
def echo_prompt(message: str) -> str:
    """에코 프롬프트를 생성합니다."""
    return f"다음 메시지를 처리해주세요: {message}"


if __name__ == "__main__":
    mcp.run()  # MCP 서버 실행 (기본 transport=stdio)
