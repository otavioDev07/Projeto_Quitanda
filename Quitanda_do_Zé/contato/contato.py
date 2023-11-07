from flask import Flask, render_template, Blueprint

contato_blueprint = Blueprint('contato', __name__, template_folder='templates')

@contato_blueprint.route('/contato')
def contato():
    titulo = 'CONTATO'
    return render_template('contato.html', titulo=titulo)