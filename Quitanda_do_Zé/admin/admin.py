from flask import Flask, render_template, Blueprint, request, redirect, session

admin_blueprint = Blueprint('admin', __name__, template_folder='templates')