from flask import Flask, render_template, Blueprint

home_blueprint = Blueprint('home', __name__, template_folder='templates')