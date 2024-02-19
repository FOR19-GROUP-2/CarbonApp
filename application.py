from flask import Flask, render_template
application = Flask(__name__)

@application.route('/')
@application.route('/home')
def home():
  return render_template('home.html')

@application.route('/methodology')
def methodology():
  return render_template('methodology.html', title='methodology')

@application.route('/carbon_app')
def carbon_app():
    return render_template('carbon_app.html', title='carbon_app')

@application.route('/contact')
def contact():
  return render_template('contact.html', title='contact')

@application.route('/about_us')
def about_us():
  return render_template('about_us.html', title='about_us')

@application.route('/login')
def login():
  return render_template('login.html', title='login')

@application.route('/register')
def register():
  return render_template('register.html', title='register')

if __name__=='__main__':
  application.run(debug=True)  