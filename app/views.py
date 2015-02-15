import flask
from flask import render_template

portal = flask.Blueprint('portal', __name__)

@portal.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')
