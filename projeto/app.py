from flask import Flask, render_template
from database import criando_banco
from controllers.albuns import albuns_bp
from controllers.artistas import artistas_bp
from controllers.faixas import faixas_bp

app = Flask(__name__)
app.secret_key = 'chave_secreta'

app.register_blueprint(albuns_bp)
app.register_blueprint(artistas_bp)
app.register_blueprint(faixas_bp)

criando_banco()

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)