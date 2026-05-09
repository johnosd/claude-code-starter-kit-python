# 1. Visão Geral do Projeto

Este projeto implementa um cliente para a Google Books API (GCP), expondo os dados via API REST construída com FastAPI.

---

# 2. Stack e Convenções Técnicas

- **Framework:** APIREST com FastAPI (Python 3.11+)
- **Tests:** Com pytest
- **Deploy:** Railway
- **Estilo de código:** PEP 8, type hints obrigatórios em todas as funções

---

# 3. Padrões de Código Obrigatórios

- **Código limpo:** funções pequenas, responsabilidade única, nomes descritivos
- **Documentação:** Typehints e docstrings em todas as funções públicas explicando o *porquê*, não o *o quê*
- **Reuso:** sem duplicação — extraia lógica repetida em helpers ou serviços compartilhados

---

# 4. O que Claude NÃO deve fazer

- **Nunca** fazer `git push` direto na branch `main`
- Sempre criar uma branch separada para qualquer alteração e abrir um Pull Request
- nunca commitar secrets ou API Keys


# 5. Comandos disponíveis

- `/review` — code review com checklist de segurança e qualidade
- `/explain-codebase` — gera mapa do projeto para novos devs

# 6. Regras específicas por contexto

@.claude/rules/testing.md
@.claude/rules/api-conventions.md