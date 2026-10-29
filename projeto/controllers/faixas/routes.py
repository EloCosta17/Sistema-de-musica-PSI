from flask import request, render_template
from controllers.faixas import faixas_bp
from models.models import Album, Faixa

@faixas_bp.route("/faixas")
def faixas():
    return render_template("faixas/faixas.html")

@faixas_bp.route("/faixas/nova", methods=["POST"])
def cadastro_faixa():
    titulo = request.form.get("titulo")
    duracao = request.form.get("duracao_segundos")
    album_id = request.form.get("album_id")
    return render_template("faixas/faixas.html", titulo=titulo, duracao=duracao, album_id=album_id)
