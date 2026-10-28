from flask import request, render_template
from controllers.artistas import artistas_bp
from models import Albuns, Artistas, Faixas

@app.route("/artistas")
def artistas():
    return render_template("artistas.html")

@app.route("/artistas/novo", methods=["POST"])
def cadastro_artista():
    nome = request.form.get("nome")
    return render_template("artistas.html", nome=nome)