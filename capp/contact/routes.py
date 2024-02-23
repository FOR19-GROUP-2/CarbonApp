from flask import render_template, Blueprint
contact = Blueprint('contact', __name__)

@contact.route('/contact')
def contact_home():
  return render_template('contact.html', title='contact')