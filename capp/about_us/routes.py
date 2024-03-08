from flask import render_template, Blueprint
about_us = Blueprint('about_us', __name__)

@about_us.route('/about_us')
def about_us_home():
  return render_template('about_us.html', title='about_us')