from flask import render_template, Blueprint
login = Blueprint('login', __name__)

@login.route('/login')
def login_home():
    return render_template('login.html', title='login')
