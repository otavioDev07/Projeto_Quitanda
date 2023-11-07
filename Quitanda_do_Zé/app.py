from flask import Flask, Blueprint
from quem_somos.quem_somos import quemsomos_blueprint
from home.home import home_blueprint
from contato.contato import contato_blueprint
from admin.admin import admin_blueprint
from model.modelo import modelo_blueprint
from session.session import session_blueprint
from database.conexao import database_blueprint

app = Flask(__name__)
app.register_blueprint(quemsomos_blueprint) #Conecta a blueprint importada no arquivo principal
app.register_blueprint(home_blueprint)
app.register_blueprint(contato_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(modelo_blueprint)
app.register_blueprint(session_blueprint)
app.register_blueprint(database_blueprint)

usuario = 'adm'
senha = '1234'

if __name__ == '__main__': # garante que o código dentro dele só será executado se este script estiver sendo executado diretamente como o programa principal.
    app.run(debug=True)