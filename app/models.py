from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    is_admin = db.Column(db.Boolean, default=False)

class Tool(db.Model):  # <-- should not be inside the User class
    id = db.Column(db.Integer, primary_key=True)  # typo: Integer, not Ineger
    name = db.Column(db.String(150))
    description = db.Column(db.Text)  # typo: Text, not text
    filename = db.Column(db.String(150))
