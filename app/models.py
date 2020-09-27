from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    '''
    The user model that creates table containing user info
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(200), unique=True,index = True, nullable=False)
    email = db.Column(db.String(300),unique = True, index = True, nullable = False)
    bio = db.Column(db.String(255))
    password_hash = db.Column(db.String(50), nullable=False)
    pitchez = db.relationship('Pitch', backref='user')
    commentz = db.relationship('Comment', backref='user')

    @property
    def password(self):
        raise AttributeError('You are not permitted to view this password')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'

class Category(db.Model):
    '''
    class model that creates a table for pitch categories
    '''
    __tablename__='categories'
    id = db.Column(db.Integer, primary_key = True)
    catname = db.Column(db.String(200),unique = True, nullable = False)
    pitches = db.relationship('Pitch',backref='category')

    def __repr__(self):
        return f'Category {self.catname}'



class Pitch(db.Model):
    '''
    pitch model that creates a table for pitches
    '''
    __tablename__='pitches'
    id = db.Column(db.Integer, primary_key = True)
    pitchword = db.Column(db.String(), nullable = False)
    catname_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref='comment')

    def __repr__(self):
        return f'Pitch {self.pitchword}'

class Comment(db.Model):
    '''
    comment model that creates a table for comments
    '''
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key = True)
    commentword = db.Column(db.String())
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    users_id = db.Column(db.Integer,db.ForeignKey('users.id'))


    def __repr__(self):
        return f'Comment {self.commentword}'
