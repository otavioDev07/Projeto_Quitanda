from flask import Flask, Blueprint, session
from quem_somos.quem_somos import quemsomos_blueprint
from home.home import home_blueprint
from contato.contato import contato_blueprint
from admin.admin import admin_blueprint

app = Flask(__name__)
app.register_blueprint(quemsomos_blueprint, home_blueprint, contato_blueprint, admin_blueprint)

app.secret_key = 'meublogotavio'
logado = False
usuario = 'seuzé'
senha = 'amobananasemexericas'

def verifica_sessao():
    if 'login' in session and session['login']: #Confirma se o indíce existe
        return True
    else:
        return False
    
if session:
    session.clear()
    

if __name__ == '__main__': # garante que o código dentro dele só será executado se este script estiver sendo executado diretamente como o programa principal.
    app.run(debug=True)