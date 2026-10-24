# 01 — Gerenciador de Tarefas CLI

Aplicativo de linha de comando para criar, listar, concluir e remover tarefas, com prioridades e persistência em JSON.

## Como rodar
```bash
python main.py adicionar "Estudar Python" --prioridade alta
python main.py listar
python main.py concluir 1
python main.py remover 1
```

## Conceitos
- `argparse` com subcomandos
- Classe `Tarefa` e `GerenciadorTarefas`
- Persistência em arquivo JSON
- Tratamento de erros de entrada
