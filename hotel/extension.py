from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy 
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()
flask_login = LoginManager()
login_manager = LoginManager()
