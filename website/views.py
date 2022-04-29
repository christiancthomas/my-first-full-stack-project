""" Store standard roots for the website
    - Home Page
"""

# Define that this file is a blueprint, i.e., it contains the roots (URIs) for our webpage
# render_template function allows us to render our webpage template
from crypt import methods
import json
from flask import Blueprint, flash, jsonify, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

# Define names of blueprint
views = Blueprint('views', __name__)

# Define our views. First, define the path and declare a function that will run at that path.
@views.route('/', methods=['GET', 'POST']) # This is called a decorator.
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Please enter some text before posting!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template('home.html', user=current_user)

# Deleting posts.
@views.route('/delete-note', methods=['POST'])
def delete_note():
    """
    Used to delete posts on the website.
    """
    note = json.loads(request.data)
    note_id = note['noteId']
    note = Note.query.get(note_id)

    # Validate the note exists and that the user signed in is the owner of the note before deleting it from db.
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({}) # Need to return something for flask to be happy.
