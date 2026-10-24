# 03 — API de Biblioteca (Flask)

API REST para cadastrar livros, listar, buscar por ID, emprestar e devolver.

## Como rodar
```bash
pip install -r requirements.txt
python app.py
# http://localhost:5000/livros
```

## Rotas
| Método | Rota | Descrição |
|--------|------|-----------|
| GET | /livros | Lista todos |
| GET | /livros/<id> | Busca um livro |
| POST | /livros | Cadastra `{"titulo": "...", "autor": "..."}` |
| POST | /livros/<id>/emprestar | Empresta |
| POST | /livros/<id>/devolver | Devolve |
