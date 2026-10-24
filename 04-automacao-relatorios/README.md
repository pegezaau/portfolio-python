# 04 — Automação e Web Scraping

Coleta títulos e preços de uma página (exemplo configurável), limpa os dados e gera um relatório CSV + resumo em texto. Inclui modo de demonstração offline para testar sem internet.

## Como rodar
```bash
pip install -r requirements.txt
python scraper.py --demo
python scraper.py --url https://exemplo.com/produtos
```

## Conceitos
- Requisições HTTP com `requests`
- Parsing HTML com `BeautifulSoup`
- Limpeza de dados e exportação CSV
- Agendamento/automação de relatórios
