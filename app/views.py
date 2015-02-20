from flask import render_template, Blueprint


portal = Blueprint('portal', __name__)


@portal.route('/aboutme', methods=['GET'])
def aboutme():
    return render_template('aboutme.html')
