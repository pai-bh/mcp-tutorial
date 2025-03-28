LangChina 기반 MCP Tutorial

- 목표1: 구글 캘린더 연동
- 목표2: Slack 연동
- 목표3: Figma연동


- 목표: MCP의 통신방법
- 목표: MCP의 보안취약점


```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Echo")


@mcp.resource("echo://{message}")
def echo_resource(message: str) -> str:
    """Echo a message as a resource"""
    return f"Resource echo: {message}"


@mcp.tool()
def echo_tool(message: str) -> str:
    """Echo a message as a tool"""
    return f"Tool echo: {message}"


@mcp.prompt()
def echo_prompt(message: str) -> str:
    """Create an echo prompt"""
    return f"Please process this message: {message}"


if __name__ == "__main__":
    mcp.run()

```
위와 같은 코드를 작성 후, 아래 shell 실행

```shell
mcp dev echo_server.py
```
위처럼 `mcp dev` 명령어를 통하면, mcp inspector를 활용?
참고링크 : https://modelcontextprotocol.io/docs/tools/inspector

 

```bash
mcp-tutorial-py3.11➜  mcp-tutorial mcp dev echo_server.py

Starting MCP inspector...
Proxy server listening on port 3000

🔍 MCP Inspector is up and running at http://localhost:5173 🚀
```


https://github.com/modelcontextprotocol/python-sdk 를 활용해서..간단하게 서버구축?
물론, FastMCP 사용할것같음.


- 참고링크 : https://www.youtube.com/watch?v=kQmXtrmQ5Zg&t=2s
- 참고링크 : https://github.com/lastmile-ai/mcp-agent
- 참고링크 : https://modelcontextprotocol.io/introduction
- 참고링크 : https://discuss.pytorch.kr/t/deep-research-model-context-protocol-mcp/6594
- 참고링크 : https://github.com/modelcontextprotocol/python-sdk/blob/main/README.md?utm_source=pytorchkr&ref=pytorchkr


[Agent관련 참고링크]
- https://www.anthropic.com/engineering/building-effective-agents


[도움이 많이 된 링크]
- https://velog.io/@todd/%EA%B0%84%EB%8B%A8%ED%95%98%EA%B2%8C-%EB%A7%8C%EB%93%A4%EB%A9%B4%EC%84%9C-%EC%9D%B4%ED%95%B4%ED%95%B4%EB%B3%B4%EB%8A%94-MCP
- https://github.com/punkpeye/awesome-mcp-servers
