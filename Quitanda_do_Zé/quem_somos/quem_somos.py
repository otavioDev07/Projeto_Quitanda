from flask import Flask, render_template, Blueprint

quemsomos_blueprint = Blueprint('quem_somos', __name__, template_folder='templates')

@quemsomos_blueprint.route('/sobre')
def sobre():
    titulo = 'QUEM SOMOS'
    return render_template('sobre.html', titulo=titulo)


