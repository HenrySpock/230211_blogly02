"""Models for Blogly."""
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy
import datetime  

db = SQLAlchemy() 

def connect_db(app):
    db.app = app
    db.init_app(app)
 
class Post(db.Model):
    """Post."""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False , default=datetime.datetime.utcnow) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref='posts')

class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50), nullable=False)
    image_url = db.Column(
        db.String(),
        nullable=False,
        default="https://www.freeiconspng.com/thumbs/person-icon/gray-person-icon-27.png",
    )

    @property
    def full_name(self):
        """Return full name of user."""
        if self.middle_name:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.last_name}"
        
       