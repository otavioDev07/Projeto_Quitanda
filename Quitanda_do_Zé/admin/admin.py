from flask import Flask, render_template, Blueprint, request, redirect, session
from session.session import verifica_sessao
from database.conexao import iniciar_db, get_db_conexao 

usuario = 'adm'
senha = '1234'
admin_blueprint = Blueprint('admin', __name__, template_folder='templates')

@admin_blueprint.route('/login')
def login():
    titulo = 'LOGIN'
    return render_template('login.html', titulo=titulo)

#Rota da página de acesso
@admin_blueprint.route('/acesso', methods=['post'])
def acesso():
    global usuario, senha
    usuario_info = request.form['usuario']
    senha_info = request.form['senha']
    if usuario == usuario_info and senha == senha_info:
        session['login'] = True
        return redirect('/adm')
    else:
        return render_template('login.html', msg="Usuário/Senha estão incorretos!")
    

#Rota da página ADM
@admin_blueprint.route('/adm')
def adm():
    global verifica_sessao, iniciar_db, get_db_conexao
    if verifica_sessao():
        iniciar_db()
        conexao = get_db_conexao()
        produtos = conexao.execute('SELECT * FROM produtos ORDER BY id DESC').fetchall()
        conexao.close()
        title = 'administração'
        return render_template('adm.html', produtos=produtos, title=title)
    else:
        return redirect('/login')

    
