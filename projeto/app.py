
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/albuns")
def Albuns():
    return render_template("albuns.html")

@app.route("/faixas")
def faixas():
    return render_template("faixas.html")

@app.route("/artistas")
def artistas():
    return render_template("artistas.html")


if __name__ == "__main__":
    app.run(debug=True)
