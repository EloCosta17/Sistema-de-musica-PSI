from flask import request, render_template
from controllers.autores import faixas_bp
from models import Albuns, Artistas, Faixas

@faixas_bp.route("/faixas")
def faixas():
    return render_template("faixas.html")

@faixas_bp.route("/faixas/nova", methods=["POST"])
def cadastro_faixa():
    titulo = request.form.get("titulo")
    duracao = request.form.get("duracao_segundos")
    album_id = request.form.get("album_id")
    return render_template("faixas.html", titulo=titulo, duracao=duracao, album_id=album_id)
