from flask import Flask, render_template, Blueprint, redirect, session

session_blueprint = Blueprint('session', __name__, template_folder='templates')

logado = False
session_blueprint.secret_key = 'meublogotavio'

def verifica_sessao():
    if 'login' in session and session['login']: #Confirma se o indíce existe
        return True
    else:
        return False
    
if session:
    session.clear()


@session_blueprint.route("/login")
def login():
    titulo = 'LOGIN'
    return render_template('login.html', titulo=titulo)

@session_blueprint.route("/logoff")
def logoff():
    titulo = 'LOGOFF'
    return render_template('login.html', titulo=titulo)