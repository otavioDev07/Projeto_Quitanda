from flask import Flask, Blueprint, session, render_template, redirect
from quem_somos.quem_somos import quemsomos_blueprint
from home.home import home_blueprint
from admin.admin import admin_blueprint
from model.modelo import modelo_blueprint
from database.conexao import database_blueprint

app = Flask(__name__)
app.secret_key = 'seuzequitanda'
app.register_blueprint(quemsomos_blueprint) #Conecta a blueprint importada no arquivo principal
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(modelo_blueprint)
app.register_blueprint(database_blueprint)

usuario = 'adm'
senha = '1234'
logado = True

def verifica_sessao():
    if 'login' in session and session['login']: #Confirma se o indíce existe
        return True
    else:
        return False
    
if session:
    session.clear()


@app.route("/login")
def login():
    titulo = 'LOGIN'
    return render_template('login.html', titulo=titulo)

@app.route("/logoff")
def logoff():
   global logado
   logado = False
   session.clear()
   return redirect('/')

if __name__ == '__main__': # garante que o código dentro dele só será executado se este script estiver sendo executado diretamente como o programa principal.
    app.run(debug=True)