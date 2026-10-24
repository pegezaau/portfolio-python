"""Gerenciador de Tarefas CLI — Projeto 01 do portfólio Python."""
import argparse, json
from dataclasses import dataclass, asdict
from pathlib import Path

ARQUIVO = Path(__file__).with_name("tarefas.json")
PRIORIDADES = ("baixa", "media", "alta")

@dataclass
class Tarefa:
    id: int
    titulo: str
    prioridade: str = "media"
    concluida: bool = False

class GerenciadorTarefas:
    def __init__(self, arquivo=ARQUIVO):
        self.arquivo = arquivo
        self.tarefas = self._carregar()

    def _carregar(self):
        if not self.arquivo.exists():
            return []
        try:
            dados = json.loads(self.arquivo.read_text(encoding="utf-8"))
            return [Tarefa(**item) for item in dados]
        except (json.JSONDecodeError, TypeError):
            return []

    def _salvar(self):
        self.arquivo.write_text(json.dumps([asdict(t) for t in self.tarefas], ensure_ascii=False, indent=2), encoding="utf-8")

    def adicionar(self, titulo, prioridade="media"):
        if prioridade not in PRIORIDADES:
            raise ValueError(f"Prioridade inválida. Use: {', '.join(PRIORIDADES)}")
        novo_id = max((t.id for t in self.tarefas), default=0) + 1
        tarefa = Tarefa(id=novo_id, titulo=titulo.strip(), prioridade=prioridade)
        self.tarefas.append(tarefa); self._salvar(); return tarefa

    def listar(self, apenas_pendentes=False):
        return [t for t in self.tarefas if not (apenas_pendentes and t.concluida)]

    def concluir(self, tarefa_id):
        for t in self.tarefas:
            if t.id == tarefa_id:
                t.concluida = True; self._salvar(); return t
        raise ValueError("Tarefa não encontrada.")

    def remover(self, tarefa_id):
        antes = len(self.tarefas)
        self.tarefas = [t for t in self.tarefas if t.id != tarefa_id]
        if len(self.tarefas) == antes:
            raise ValueError("Tarefa não encontrada.")
        self._salvar()

def main():
    parser = argparse.ArgumentParser(description="Gerenciador de Tarefas")
    sub = parser.add_subparsers(dest="comando", required=True)
    p_add = sub.add_parser("adicionar"); p_add.add_argument("titulo"); p_add.add_argument("--prioridade", default="media", choices=PRIORIDADES)
    p_list = sub.add_parser("listar"); p_list.add_argument("--pendentes", action="store_true")
    p_done = sub.add_parser("concluir"); p_done.add_argument("id", type=int)
    p_del = sub.add_parser("remover"); p_del.add_argument("id", type=int)
    args = parser.parse_args()
    g = GerenciadorTarefas()
    try:
        if args.comando == "adicionar":
            t = g.adicionar(args.titulo, args.prioridade); print(f"✅ Tarefa #{t.id} criada: {t.titulo} [{t.prioridade}]")
        elif args.comando == "listar":
            tarefas = g.listar(args.pendentes)
            if not tarefas: print("Nenhuma tarefa encontrada.")
            for t in tarefas: print(f"{'✅' if t.concluida else '⬜'} #{t.id} {t.titulo} [{t.prioridade}]")
        elif args.comando == "concluir":
            t = g.concluir(args.id); print(f"✅ Tarefa #{t.id} concluída!")
        elif args.comando == "remover":
            g.remover(args.id); print(f"🗑️ Tarefa #{args.id} removida.")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
