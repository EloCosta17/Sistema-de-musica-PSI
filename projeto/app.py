from flask import Flask, render_template
from database import criando_banco
from controllers.albuns import albuns_bp
from controllers.artistas import artistas_bp
from controllers.faixas import faixas_bp
from controllers.auth import auth_bp
from flask import session as flask_session  

app = Flask(__name__)
app.secret_key = 'chave_secreta'

app.register_blueprint(albuns_bp)
app.register_blueprint(artistas_bp)
app.register_blueprint(faixas_bp)
app.register_blueprint(auth_bp)

criando_banco()

@app.route("/")
def index():
    usuario_logado = flask_session.get('usuario_nome')
    return render_template("index.html", usuario=usuario_logado)

if __name__ == "__main__":
    app.run(debug=True)