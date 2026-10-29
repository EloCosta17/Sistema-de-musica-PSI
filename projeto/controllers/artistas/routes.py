from flask import request, render_template
from controllers.artistas import artistas_bp
from models.models import Album, Artista

@artistas_bp.route("/artistas")
def artistas():
    return render_template("artistas/artistas.html")

@artistas_bp.route("/artistas/novo", methods=["POST"])
def cadastro_artista():
    nome = request.form.get("nome")
    return render_template("artistas/artistas.html", nome=nome)