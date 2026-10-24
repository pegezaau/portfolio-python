# 02 — Analisador de Dados de Vendas

Lê um CSV de vendas, calcula faturamento total, ticket médio, produto mais vendido e vendas por categoria, e gera um relatório em texto.

## Como rodar
```bash
python analisador.py dados_exemplo.csv
# gera relatorio.txt na mesma pasta
```

## Conceitos
- Leitura e validação de CSV
- `collections.Counter` / `defaultdict`
- `statistics` para médias
- Geração de relatório formatado
