from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

application = Flask(__name__)

application.config['SECRET_KEY'] = '3oueqkfdfas8ruewqndr8ewrewrouewrere44554'
DBVAR = 'postgresql://postgres:Skole123@awseb-e-pkphjnmpjc-stack-awsebrdsdatabase-hjmk2avjfod8.czy4aiswgvkx.eu-north-1.rds.amazonaws.com:5432//ebdb'
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
application.config['SQLALCHEMY_BINDS'] ={'transport': 'sqlite:///transport.db'}

#application.config['SECRET_KEY'] = os.environ['SECRET_KEY']  
#DBVAR = f"postgresql://{os.environ['RDS_USERNAME']}:{os.environ['RDS_PASSWORD']}@{os.environ['RDS_HOSTNAME']}/{os.environ['RDS_DB_NAME']}"
#application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR 
#application.config['SQLALCHEMY_BINDS'] ={'transport': DBVAR}

db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager= LoginManager(application)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.carbon_app.routes import carbon_app
from capp.about_us.routes import about_us
from capp.contact.routes import contact
#from capp.login.routes import login
#from capp.register.routes import register
from capp.users.routes import users

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_app)
application.register_blueprint(about_us)
application.register_blueprint(contact)
#application.register_blueprint(login)
#application.register_blueprint(register)
application.register_blueprint(users)

# Test
#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Add this line to suppress the warning
