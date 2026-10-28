from flask import request, render_template
from controllers.albuns import albuns_bp
from models import Albuns, Artistas, Faixas

@app.route("/albuns")
def albuns():
    return render_template("albuns.html")

@app.route("/albuns/novo", methods=["POST"])
def cadastro_album():
    titulo = request.form.get("titulo")
    ano = request.form.get("ano")
    return render_template("albuns.html", titulo=titulo, ano=ano)