---
paths: 
  - "src/api/**/*.py"
---

# Convenções de API

- **Endpoints RESTful:** siga os padrões REST para nomeação e estrutura de endpoints (ex: `GET /books`, `POST /books/{id}/reviews`)
- **Validação de dados:** use Pydantic para validação rigorosa de entrada e saída, garantindo que os dados estejam sempre no formato esperado
- **Tratamento de erros:** implemente tratamento de erros consistente, retornando mensagens claras e códigos HTTP apropriados (ex: 400 para bad request, 404 para not found)
- **Autenticação:** use OAuth2 ou JWT para proteger endpoints sensíveis, garantindo que apenas usuários autorizados possam acessá-los
- **Documentação:** aproveite a documentação automática do FastAPI, mas adicione descrições detalhadas e exemplos de uso para cada endpoint
- **Versionamento:** considere versionar a API (ex: `/v1/books`) para facilitar futuras mudanças sem quebrar clientes existentes