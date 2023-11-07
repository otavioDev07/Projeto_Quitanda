from flask import Flask, render_template, Blueprint

home_blueprint = Blueprint('home', __name__, template_folder='templates')


@home_blueprint.route("/")
def index():
    titulo = 'PÁGINA INICIAL'
    return render_template('index.html', titulo=titulo)