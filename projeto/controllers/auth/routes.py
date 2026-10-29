from flask import request, render_template, url_for, redirect, session as flask_session, flash
from controllers.auth import auth_bp
from database import session
from werkzeug.security import generate_password_hash, check_password_hash
from models.models import Usuario

@auth_bp.route('/cadastro', methods=['POST','GET'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        usuario_existente = session.query(Usuario).filter_by(nome=nome).first()
        if usuario_existente:
            return redirect(url_for('auth.cadastrar'))

        senha = generate_password_hash(senha)
        usuario_novo = Usuario(nome=nome, email=email, senha=senha)
        session.add(usuario_novo)
        session.commit()
        return redirect(url_for('auth.login'))

    return render_template('auth/cadastro.html')

@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        nome = request.form.get('nome')
        senha = request.form.get('senha')

        usuario = session.query(Usuario).filter_by(nome=nome).first()
        if usuario and check_password_hash(usuario.senha, senha):
            flask_session['usuario_id'] = usuario.id
            flask_session['usuario_nome'] = usuario.nome
            return redirect(url_for('index'))
        else:
            flash("Informações incorretas")
            return redirect(url_for('auth.login'))

    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    flask_session.clear()
    return redirect(url_for('index'))
