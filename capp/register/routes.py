from flask import render_template, Blueprint
register = Blueprint('register', __name__)

@register.route('/register')
def register_home():
    return render_template('register.html', title='register')