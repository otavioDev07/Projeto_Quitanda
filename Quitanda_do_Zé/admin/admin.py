from flask import Flask, render_template, Blueprint, request, redirect, session

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
    
