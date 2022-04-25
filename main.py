# Import the create_app function from the website package. We can do this because
# website is a python package. We can import by importing the name of folder (package).
from distutils.log import debug
from website import create_app

app = create_app()

# We only want to run this line if we are running main.py directly; NOT if we import it.
if __name__ == '__main__':
    # This runs the flask application (web server) and will automatically rerun if we change anything
    # in our code (debug=True)
    app.run(debug=True)