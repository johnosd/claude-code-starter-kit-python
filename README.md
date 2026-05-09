# Claude Code Starter Kit — Python

Adicione Claude Code ao seu time Python em 5 minutos.

Chega de cada dev configurar do zero. Este starter kit entrega
convenções compartilhadas, comandos prontos e PR reviews automáticos
— tudo versionado no Git e funcionando no primeiro clone.

---

## O que você ganha

- **`/review`** — code review com checklist real: segurança, performance, type hints e cobertura
- **`/explain-codebase`** — novo dev no time? Roda o skill e recebe um mapa do projeto em segundos
- **Convenções automáticas** — regras específicas por tipo de arquivo, sem poluir o contexto
- **PR reviews no GitHub Actions** — Claude Code roda automaticamente em cada pull request
- **MCP do GitHub integrado** — Claude Code acessa issues, PRs e contexto do repositório direto no terminal

---

## Quick start

```bash
git clone https://github.com/seu-usuario/claude-code-starter-kit-python
cd claude-code-starter-kit-python

cp .env.example .env
# edite .env com suas credenciais

pip install -r requirements.txt

uvicorn src.api.main:app --reload
```

Acesse em `http://localhost:8000/docs` para usar a interface Swagger UI.

---

## Endpoints

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/books?q={termo}` | Busca livros na Google Books API |
| `GET` | `/books?q={termo}&page=2` | Paginação de resultados |

**Interfaces de documentação:**

| URL | Interface |
|---|---|
| `http://localhost:8000/docs` | Swagger UI — teste direto no navegador |
| `http://localhost:8000/redoc` | ReDoc — documentação alternativa |

---

## Estrutura
```
.
├── CLAUDE.md                          # convenções universais do projeto
├── .claude/
│   ├── rules/
│   │   ├── testing.md                 # carrega só em arquivos test_*.py
│   │   └── api-conventions.md         # carrega só em src/api/
│   ├── commands/
│   │   └── review.md                  # /review — checklist completo
│   └── skills/
│       └── explain-codebase/
│           └── SKILL.md               # /explain-codebase — mapa do projeto
├── .mcp.json                          # GitHub MCP com env var expansion
├── .github/
│   └── workflows/
│       └── claude-review.yml          # PR reviews automáticos
├── .env.example                       # template de variáveis de ambiente
├── src/
│   └── api/
│       ├── main.py                    # app FastAPI — endpoints e roteamento
│       └── example.py                 # integração com Google Books API
├── tests/
│   └── test_example.py                # exemplo de teste
└── requirements.txt
```
---

## Como funciona

**Convenções automáticas por arquivo:**
editando tests/test_.py    → regras de teste carregam automaticamente
editando src/api/.py       → convenções de API carregam automaticamente
qualquer outro arquivo      → só as convenções universais do CLAUDE.md


**Slash commands disponíveis:**

```bash
/review          # checklist: segurança, performance, type hints, cobertura
/explain-codebase  # mapa do projeto para novos devs
```

**PR review automático:**
Cada pull request recebe um comment automático com findings estruturados — 
sem configuração adicional após o setup inicial.

---

## Pré-requisitos

- Claude Code instalado (`npm install -g @anthropic-ai/claude-code`)
- Assinatura Claude Pro ou Max (ou API key)
- Node.js 18+
- Python 3.11+

---

## Configuração

**1. Variáveis de ambiente**

Copie `.env.example` para `.env` e preencha:
```
ANTHROPIC_API_KEY=sk-ant-...
GITHUB_TOKEN=ghp_...
GOOGLE_BOOKS_API_KEY=AIza...
```

**2. GitHub Actions**

No repositório, adicione os secrets:
- `ANTHROPIC_API_KEY` — sua chave da API Anthropic

Pronto. O workflow `.github/workflows/claude-review.yml` já está configurado.

---

## Conceitos implementados (Claude Certified Architect)

| Task Statement | Conceito |
|---|---|
| 3.1 | CLAUDE.md hierárquico com @import e .claude/rules/ |
| 3.2 | Slash commands e skills com frontmatter (context:fork, allowed-tools) |
| 3.3 | Path-specific rules com glob patterns |
| 3.4 | Plan mode vs direct execution |
| 3.6 | CI/CD com -p flag e --output-format json |
| 2.4 | .mcp.json com environment variable expansion |

---

## Licença

MIT — use, adapte e distribua livremente.