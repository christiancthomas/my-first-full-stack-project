""" Create a database model for users and posts. """

from time import timezone

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# Define models that our users and notes need to conform to.
class User(db.Model, UserMixin):
    """
    The User class defines the schema to be used in the database for users.
    ...

    Attributes
    ----------
    id : int
        id value of the user.
    email : str
        email address for the user.
    password : string
        password of the user.
    first_name : string
        first name of the user.
    notes : int
        stores all note ids associated with a user.
    """
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')


class Note(db.Model):
    """
    The Note class defines the schema to be used in the database for notes.
    ...

    Attributes
    ----------
    id : int
        id value of the note.
    data : str
        data contained within the note represented as a string.
    date : DateTime
        time the note was created handled by func.now().
    user_id : int
        Associates the user_id for the note with the user id in the user object ('user.id'); i.e., the user that created the note. Stores the id value in user_id. This reflects a one-to-many relationship.
    """

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
