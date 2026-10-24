"""API de Biblioteca — Projeto 03 do portfólio Python (Flask)."""
from flask import Flask, jsonify, request, abort

app = Flask(__name__)
livros = [
    {"id": 1, "titulo": "Clean Code", "autor": "Robert C. Martin", "disponivel": True},
    {"id": 2, "titulo": "Python Fluente", "autor": "Luciano Ramalho", "disponivel": True},
]
_proximo_id = 3

def buscar(livro_id):
    return next((l for l in livros if l["id"] == livro_id), None)

@app.get("/livros")
def listar():
    return jsonify(livros)

@app.get("/livros/<int:livro_id>")
def detalhe(livro_id):
    livro = buscar(livro_id) or abort(404, "Livro não encontrado")
    return jsonify(livro)

@app.post("/livros")
def criar():
    global _proximo_id
    dados = request.get_json(silent=True) or {}
    if not dados.get("titulo") or not dados.get("autor"):
        abort(400, "Campos 'titulo' e 'autor' são obrigatórios")
    livro = {"id": _proximo_id, "titulo": dados["titulo"], "autor": dados["autor"], "disponivel": True}
    _proximo_id += 1; livros.append(livro)
    return jsonify(livro), 201

@app.post("/livros/<int:livro_id>/emprestar")
def emprestar(livro_id):
    livro = buscar(livro_id) or abort(404, "Livro não encontrado")
    if not livro["disponivel"]: abort(409, "Livro já emprestado")
    livro["disponivel"] = False; return jsonify(livro)

@app.post("/livros/<int:livro_id>/devolver")
def devolver(livro_id):
    livro = buscar(livro_id) or abort(404, "Livro não encontrado")
    livro["disponivel"] = True; return jsonify(livro)

@app.get("/")
def home():
    return jsonify({"api": "Biblioteca", "rotas": ["/livros"]})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
