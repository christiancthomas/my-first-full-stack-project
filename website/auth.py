""" Store standard roots for pages related to authentication.
    - Login Page
    - Logout Page
    - Sign Up Page
"""

# Define that this file is a blueprint, i.e., it contains the roots (URIs) for our webpage
import email
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

# Define names of blueprint
auth = Blueprint('auth', __name__)

# Define 'Login', 'Logout', and 'Sign Up' routes and webpage functions.
@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Query db for email + password.
        user = User.query.filter_by(email=email).first()
        if user:

            # Check if password is valid.
            if check_password_hash(user.password, password):
                flash('Login successful.', category='success')
                login_user(user, remember=True) # Stores login status until session/cache is cleared
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')

        else:
            flash('Email does not exist.', category='error')

    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    # Differentiate between request types.
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Error handling with message flashing where applicable before adding user to db.
        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category = 'error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category = 'error')
        elif len(email) < 4:
            flash('Please enter a valid email address.', category = 'error')
        elif len(password1) < 7:
            flash('Password must be 7 characters or greater.', category = 'error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Login successful!', category='success')
            login_user(new_user, remember=True) # Stores login status until session/cache is cleared
            flash('Account creation successful!', category = 'success')
            return redirect(url_for('views.home'))
    
    return render_template('sign_up.html', user=current_user)
