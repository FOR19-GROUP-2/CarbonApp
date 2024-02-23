from flask import Flask
application = Flask(__name__)

from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.carbon_app.routes import carbon_app
from capp.about_us.routes import about_us
from capp.contact.routes import contact
from capp.login.routes import login
from capp.register.routes import register

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_app)
application.register_blueprint(about_us)
application.register_blueprint(contact)
application.register_blueprint(login)
application.register_blueprint(register)