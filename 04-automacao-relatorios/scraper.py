"""Automação e Web Scraping — Projeto 04 do portfólio Python."""
import argparse, csv, re
from pathlib import Path

DEMO = [
    {"nome": "Notebook Gamer", "preco": 4299.90},
    {"nome": "Monitor 27 polegadas", "preco": 1199.00},
    {"nome": "Cadeira Ergonômica", "preco": 899.90},
]

def limpar_preco(texto):
    numeros = re.sub(r"[^\d,.]", "", texto).replace(".", "").replace(",", ".")
    try: return float(numeros)
    except ValueError: return 0.0

def coletar_da_web(url):
    import requests
    from bs4 import BeautifulSoup
    resp = requests.get(url, timeout=15, headers={"User-Agent": "PortfolioPython/1.0"})
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    itens = []
    for card in soup.select(".produto, .product, article"):
        nome = card.get_text(" ", strip=True)[:80]
        preco_tag = card.select_one(".preco, .price")
        if nome and preco_tag:
            itens.append({"nome": nome, "preco": limpar_preco(preco_tag.get_text())})
    return itens

def salvar_relatorio(itens, destino="relatorio_precos.csv"):
    with open(destino, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["nome", "preco"]); writer.writeheader(); writer.writerows(itens)
    if itens:
        precos = [i["preco"] for i in itens]
        print(f"Itens: {len(itens)} | Menor: R$ {min(precos):.2f} | Maior: R$ {max(precos):.2f} | Média: R$ {sum(precos)/len(precos):.2f}")
    print(f"Relatório salvo em {Path(destino).resolve()}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--demo", action="store_true"); parser.add_argument("--url")
    args = parser.parse_args()
    dados = DEMO if args.demo or not args.url else coletar_da_web(args.url)
    salvar_relatorio(dados)
