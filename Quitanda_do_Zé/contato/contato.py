from flask import Flask, render_template, Blueprint

contato_blueprint = Blueprint('contato', __name__, template_folder='templates')