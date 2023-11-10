from flask import Flask, render_template, Blueprint, request, redirect, session
from session.session import verifica_sessao
from database.conexao import iniciar_db, get_db_conexao 
import uuid

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
    

#Rota para renderizar página de cadastro
@admin_blueprint.route('/cadprodutos')
def cadprodutos():
    if verifica_sessao():
        title = "CADASTRO DE PRODUTOS"
        return render_template('cadastro.html', title=title)
    else:
        return redirect('/login')
    
#Rota para cadastro no database
@admin_blueprint.route('/cadastro', methods=['post'])
def cadastro():
    if verifica_sessao():
        nome = request.form['nome']
        descricao = request.form['descricao']
        preco = request.form['preco']
        img = request.files['img']
        id_img = str(uuid.uuid4().hex)
        filename = id_img+nome+'.png'
        img.save('../../static/img/produtos')
        conexao = get_db_conexao()
        conexao.execute('INSERT INTO produtos (nome, descricao, preco, img) VALUES (?, ?, ?, ?)', (nome, descricao, preco, filename))
        conexao.commit()
        conexao.close()
        return redirect('/adm')
    else:
        return redirect('/login')
    


    
