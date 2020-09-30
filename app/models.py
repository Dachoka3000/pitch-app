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
    password_hash = db.Column(db.String(255), nullable=False)
    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref='user', lazy='dynamic')

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
    pitches = db.relationship('Pitch',backref='category',lazy='dynamic')

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
    comments = db.relationship('Comment', backref='pitch',lazy='dynamic')
    votes = db.relationship('Vote',backref='pitch', lazy='dynamic')

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

class Vote(db.Model):
    '''
    vote model that creates a table for votes
    '''
    __tablename__='votes'
    id = db.Column(db.Integer, primary_key = True)
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    def __repr__(self):
        return f"Upvotes:{self.upvote} with Downvotes:{self.downvote}"

class Upvotes:
    '''
    Upvotes class that instantiates new classes of upvotes
    '''

    all_upvotes = []

    def __init__(self, upvotes):
        '''
        init class that initializes new instances of upvotes
        Args:
            upvotes: number of upvotes a pitch has
        '''
        self.upvotes = upvotes

    def save_upvote(self):
        Upvotes.all_upvotes.append(self)

    @classmethod
    def clear_upvotes(cls):
        Upvotes.all_upvotes.clear()

    @classmethod
    def get_upvotes(cls,id):

        voteup=[]

        for upvote in cls.all_upvotes:
            if upvote.pitch_id==id:
                voteup.append(upvote)
        return voteup

class Downvotes:
    '''
    Downvotes class that instantiates new classes of downvotes
    '''

    all_downvotes = []

    def __init__(self, downvotes):
        '''
        init class that initializes new instances of downvotes
        Args:
            downvotes: number of downvotes a pitch has
        '''
        self.downvotes = downvotes

    def save_upvote(self):
        Downvotes.all_downvotes.append(self)

    @classmethod
    def clear_downvotes(cls):
        Downvotes.all_downvotes.clear()

    @classmethod
    def get_downvotes(cls,id):

        votedown=[]

        for downvote in cls.all_downvotes:
            if downvote.pitch_id==id:
                votedown.append(downvote)
        return votedown
