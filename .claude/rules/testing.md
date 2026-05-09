---
paths:
  - "tests/**/*.py"

---

# Convenções de Testes
- **Testes unitários:** foco em funções isoladas, sem dependências externas
- **Mocks:** use mocks para isolar dependências, mas evite mockar a própria função testada
- **Nomenclatura:** nomeie os testes com `test_` seguido do comportamento esperado, ex: `test_calculate_total_returns_correct_sum`
- **Cobertura:** busque alta cobertura, mas priorize qualidade sobre quantidade — teste os casos de borda e falhas esperadas
- **Organização:** agrupe testes relacionados em classes ou módulos, mas evite hierarquias profundas
- **Fixtures:** use fixtures para setup/teardown compartilhado, mas mantenha-as simples e específicas
- **Simplicidade** — cada teste deve ser fácil de entender e focado em um único comportamento ou cenário