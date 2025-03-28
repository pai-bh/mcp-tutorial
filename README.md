# MCP (Model Context Protocol) Tutorial

<div align="center">

[![Python Version][python-badge]][python-url]
[![MCP Version][mcp-badge]][mcp-url]
[![Documentation][docs-badge]][docs-url]

[python-badge]: https://img.shields.io/badge/python-3.11-blue.svg
[python-url]: https://www.python.org/downloads/
[mcp-badge]: https://img.shields.io/badge/mcp-1.6.0-green.svg
[mcp-url]: https://pypi.org/project/mcp/
[docs-badge]: https://img.shields.io/badge/docs-modelcontextprotocol.io-blue.svg
[docs-url]: https://modelcontextprotocol.io

</div>

## 📚 학습 단계

### Step 0: MCP 이해하기
- [MCP 개념 및 구조](docs/00_MCP란?.md)
  - Resources, Tools, Prompts 이해
  - MCP vs 전통적인 API
  - 통신 프로토콜 이해

### Step 1: MCP Inspector 활용
- [Inspector를 통한 테스트](docs/01_MCP%20inspector를%20활용한%20테스트.md)
  - 기본 서버 구현 (country_server.py)
  - Inspector 사용법
  - 세션 관리 및 통신 방식

### Step 2: 외부 서비스 연동
- Google Calendar 연동 (진행 예정)
- Slack 연동 (진행 예정)
- Figma 연동 (진행 예정)

## 🚀 시작하기

### 환경 설정
```bash
# Poetry 설치 (필요한 경우)
curl -sSL https://install.python-poetry.org | python3 -

# 프로젝트 의존성 설치
poetry install

# 가상환경 활성화
poetry shell
```

### 기본 서버 실행
```bash
mcp dev country_server.py
```

## 📁 프로젝트 구조 (초안)
```shell
.
├── docs/
│ ├── 00_MCP란?.md
│ └── 01_MCP inspector를 활용한 테스트.md
├── country_server.py # 기본 MCP 서버 예제
├── country_client.py # Python 클라이언트 예제
├── pyproject.toml # 의존성 관리
└── README.md
```

## 🔗 참고 자료

### 공식 문서
- [MCP 공식 문서](https://modelcontextprotocol.io)
- [Python SDK GitHub](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Agent 예제](https://github.com/lastmile-ai/mcp-agent)

### 커뮤니티 자료
- [간단하게 만들면서 이해해보는 MCP](https://velog.io/@todd/간단하게-만들면서-이해해보는-MCP)
- [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers)
- [PyTorch KR Discussion](https://discuss.pytorch.kr/t/deep-research-model-context-protocol-mcp/6594)

### 추가 학습 자료
- [Building Effective Agents - Anthropic](https://www.anthropic.com/engineering/building-effective-agents)