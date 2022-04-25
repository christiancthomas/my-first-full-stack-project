""" Store standard roots for pages related to authentication.
    - Login Page
    - Logout Page
    - Sign Up Page
"""

# Define that this file is a blueprint, i.e., it contains the roots (URIs) for our webpage
from flask import Blueprint

# Define names of blueprint
auth = Blueprint('auth', __name__)

# Define 'Login', 'Logout', and 'Sign Up' routes and webpage functions.
@auth.route('/login')
def login():
    return '<p>Login</p>'

@auth.route('/logout')
def logout():
    return '<p>Logout</p>'

@auth.route('/signup')
def signup():
    return '<p>Sign Up</p>'