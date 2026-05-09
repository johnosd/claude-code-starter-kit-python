# /review — Code Review

Revise o arquivo especificado como argumento. Se nenhum argumento for fornecido,
revise os arquivos modificados no working directory atual.

Faça um code review estruturado dos arquivos alterados (ou do arquivo atual, se nenhum for especificado).
Para cada seção abaixo, liste os achados com severidade **[CRÍTICO | AVISO | SUGESTÃO]** e uma ação corretiva clara.
Se não houver achados em uma seção, escreva "Nenhum problema encontrado."

---

## 1. Segurança

- Secrets ou API keys hardcoded (tokens, senhas, URLs com credenciais)
- Variáveis de ambiente acessadas sem valor padrão seguro
- Entradas de usuário sem validação ou sanitização (SQL injection, path traversal, etc.)
- Dependências com vulnerabilidades conhecidas

## 2. Qualidade de Código

- Funções com mais de uma responsabilidade — proponha a separação
- Código duplicado — indique onde extrair helper ou serviço
- Nomes de variáveis/funções que não descrevem a intenção
- Complexidade ciclomática alta (muitos `if` aninhados, loops complexos)
- Tratamento de erros ausente ou genérico demais (`except Exception` sem log)

## 3. Type Hints

- Funções públicas sem anotação de parâmetros ou retorno
- Uso de `Any` onde um tipo mais específico seria possível
- Retornos opcionais sem `Optional[...]` ou `X | None`
- Modelos Pydantic com campos sem tipo explícito

## 4. Testes

- Lógica de negócio sem cobertura de testes
- Casos de borda não testados (lista vazia, valor None, erro de rede)
- Testes que dependem de estado externo sem mock (chamadas HTTP reais, banco de dados)
- Nomes de funções de teste que não descrevem o cenário (`test_1`, `test_func`)

## 5. Padrões FastAPI

- Endpoints sem `response_model` definido
- Validação de entrada feita manualmente em vez de via schema Pydantic
- Exceções levantadas sem `HTTPException` com status code adequado
- Dependências (`Depends`) mal organizadas ou duplicadas

---

Ao final, apresente um **resumo executivo** com:
- Total de achados por severidade
- Os 2-3 itens mais urgentes para corrigir
