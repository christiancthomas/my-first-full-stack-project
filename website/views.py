""" Store standard roots for the website
    - Home Page
"""

# Define that this file is a blueprint, i.e., it contains the roots (URIs) for our webpage
# render_template function allows us to render our webpage template
from flask import Blueprint, render_template

# Define names of blueprint
views = Blueprint('views', __name__)

# Define our views. First, define the path and declare a function that will run at that path.
@views.route('/') # This is called a decorator.
def home():
    # return "<h1>Test</h1>" # Just a quick header tag to test the webpage's functionality.
    return render_template('home.html')
