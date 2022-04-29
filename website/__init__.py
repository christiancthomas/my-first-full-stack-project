from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, login_manager

# Define new db.
db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    """Initialize flask application and generate a secret key.
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '&05.F-zkfeBy.6r-SsD#b&1r~4=DJ'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # Defining db location for flask
    db.init_app(app) # tells the db that we're going to use the flask app we defined


    # Define blueprint locations
    from .views import views
    from .auth import auth

    # Register blueprints with our flask application.
    app.register_blueprint(views, url_prefix = '/') # This defines how to access the file
    app.register_blueprint(auth, url_prefix = '/') # This defines how to access the file

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # Tell flask how to load a user.
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

def create_database(app):
    """ 
    Use path module to check if database exists. If not, create the database using db.create_all().
    """
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created database.')
