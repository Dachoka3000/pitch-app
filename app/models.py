from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    '''
    The user model that creates table containing user info
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(200), unique=True,index = True, nullable=False)
    email = db.Column(db.String(300),unique = True, index = True, nullable = False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'User {self.username}'