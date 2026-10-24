"""Analisador de Dados de Vendas — Projeto 02 do portfólio Python."""
import csv, sys
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean

def carregar_vendas(caminho):
    vendas = []
    with open(caminho, newline="", encoding="utf-8") as f:
        for linha in csv.DictReader(f):
            try:
                vendas.append({"produto": linha["produto"], "categoria": linha["categoria"], "quantidade": int(linha["quantidade"]), "preco": float(linha["preco"])})
            except (KeyError, ValueError):
                continue
    return vendas

def analisar(vendas):
    valores = [v["quantidade"] * v["preco"] for v in vendas]
    por_categoria = defaultdict(float)
    for v, valor in zip(vendas, valores): por_categoria[v["categoria"]] += valor
    mais_vendido = Counter(v["produto"] for v in vendas).most_common(1)
    return {"total_vendas": len(vendas), "faturamento": sum(valores), "ticket_medio": mean(valores) if valores else 0, "produto_mais_vendido": mais_vendido[0][0] if mais_vendido else "-", "por_categoria": dict(por_categoria)}

def gerar_relatorio(resultado, destino="relatorio.txt"):
    linhas = ["RELATÓRIO DE VENDAS", "="*40, f"Total de vendas: {resultado['total_vendas']}", f"Faturamento: R$ {resultado['faturamento']:.2f}", f"Ticket médio: R$ {resultado['ticket_medio']:.2f}", f"Produto mais vendido: {resultado['produto_mais_vendido']}", "", "Por categoria:"]
    for cat, valor in sorted(resultado["por_categoria"].items()): linhas.append(f"  - {cat}: R$ {valor:.2f}")
    Path(destino).write_text("\n".join(linhas), encoding="utf-8")
    return "\n".join(linhas)

if __name__ == "__main__":
    arquivo = sys.argv[1] if len(sys.argv) > 1 else "dados_exemplo.csv"
    resultado = analisar(carregar_vendas(arquivo))
    print(gerar_relatorio(resultado))
    print("\nRelatório salvo em relatorio.txt")
