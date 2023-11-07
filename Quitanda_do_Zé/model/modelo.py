from flask import Flask, render_template, Blueprint

modelo_blueprint = Blueprint('modelo', __name__, template_folder='templates')

@modelo_blueprint.route('/modelo')
def modelo():
    titulo = 'PÁGINA MODELO'
    return render_template('modelo.html', titulo=titulo)