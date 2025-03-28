from mcp.server.fastmcp import FastMCP

# 간단한 "국가-수도" 데이터베이스 (딕셔너리)
capitals = {
    "대한민국": "서울",
    "미국": "Washington, D.C.",
    "프랑스": "Paris",
    "일본": "Tokyo",
}

# MCP 서버 생성
mcp = FastMCP("CountryInfo")


# 1. Resource: 모든 국가 리스트 제공
@mcp.resource("countries://list")
def list_countries() -> list[str]:
    """사용 가능한 모든 국가 이름 리스트 반환"""
    return list(capitals.keys())


# 2. Resource: 특정 국가의 정보 조회
@mcp.resource("country://{name}")
def get_country_info(name: str) -> str:
    """특정 국가의 수도 정보 반환"""
    return f"{name}의 수도는 {capitals.get(name, '알 수 없음')}입니다."


# 3. Tool: 수도 조회
@mcp.tool()
def get_capital(country: str) -> str:
    """주어진 국가의 수도 이름을 반환"""
    if country in capitals:
        return f"{country}의 수도는 {capitals[country]}입니다."
    return f"죄송합니다. {country}의 수도 정보를 찾을 수 없습니다."


# 4. Prompt: 국가 정보 조회 프롬프트
@mcp.prompt()
def country_info_prompt(country: str) -> str:
    """국가 정보 조회를 위한 프롬프트 생성"""
    return f"다음 국가의 정보를 알려주세요: {country}"


if __name__ == "__main__":
    mcp.run()
