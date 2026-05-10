---
context: fork
allowed-tools:
  - Read
  - Glob
  - Grep
argument-hint: "[nome do modulo ou vazio para projeto completo]"
---

# Explain Codebase
Se um argumento for fornecido, foque no módulo especificado.
Se não, mapeie o projeto completo.

## Passos

1. Use Glob para identificar os arquivos relevantes (.py, .js, .ts, .md, etc.) e sua estrutura hierárquica. Gere um mapa do projeto com os módulos e seus relacionamentos.
2. Use Read para ler os arquivos principais de cada módulo (ex: index.js, main.py) e extrair as funções, classes, e suas responsabilidades. Preste atenção a comentários e docstrings para entender o propósito de cada componente.
3. Use Grep para identificar padrões comuns, como chamadas de função, importações, e uso de variáveis-chave. Isso ajuda a entender como os módulos interagem e quais são as dependências críticas.
4. Apresente o resultado em formato markdown, destacando os módulos principais, suas responsabilidades, e como eles se conectam. Use diagramas simples (ex: ASCII art) para ilustrar a estrutura do projeto e as relações entre os componentes.

## Formato de saída

### 🗂️ Estrutura do projeto
(mapa de pastas com descrição de cada diretório)


### 🔑 Arquivos-chave
(lista dos arquivos mais importantes e seus propósitos)

### 🔄 Fluxo principal
(como uma requisição percorre o sistema do entry point até a resposta)

### 📦 Dependências externas
(principais libs do requirements.txt e para que servem)

### 🚀 Por onde começar
(recomendação para novo dev: qual arquivo ler primeiro, qual rodar primeiro)