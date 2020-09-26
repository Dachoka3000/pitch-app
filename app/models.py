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
    password_hash = db.Column(db.String(50), nullable=False)

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