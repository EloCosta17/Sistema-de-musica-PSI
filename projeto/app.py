from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/artistas")
def artistas():
    return render_template("artistas.html")

@app.route("/artistas/novo", methods=["POST"])
def cadastro_artista():
    nome = request.form.get("nome")
    return render_template("artistas.html", nome=nome)

@app.route("/albuns")
def albuns():
    return render_template("albuns.html")

@app.route("/albuns/novo", methods=["POST"])
def cadastro_album():
    titulo = request.form.get("titulo")
    ano = request.form.get("ano")
    return render_template("albuns.html", titulo=titulo, ano=ano)

@app.route("/faixas")
def faixas():
    return render_template("faixas.html")

@app.route("/faixas/nova", methods=["POST"])
def cadastro_faixa():
    titulo = request.form.get("titulo")
    duracao = request.form.get("duracao_segundos")
    album_id = request.form.get("album_id")
    return render_template("faixas.html", titulo=titulo, duracao=duracao, album_id=album_id)

if __name__ == "__main__":
    app.run(debug=True)