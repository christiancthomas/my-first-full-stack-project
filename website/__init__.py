from flask import Flask

def create_app():
    """Initialize flask application and generate a secret key.
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '&05.F-zkfeBy.6r-SsD#b&1r~4=DJ'

    # Define blueprint locations
    from .views import views
    from .auth import auth

    # Register blueprints with our flask application.
    app.register_blueprint(views, url_prefix = '/') # This defines how to access the file
    app.register_blueprint(auth, url_prefix = '/') # This defines how to access the file

    return app
    
