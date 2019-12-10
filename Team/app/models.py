from datetime import datetime
from . import db
# from . import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

class User(UserMixin, db.Model):
    '''
    Class is responsible for each user's credentials as well as password resets.
    '''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    # followed = db.relationship('User',
    #                            secondary=followers,
    #                            primaryjoin=(followers.c.follower_id == id),
    #                            secondaryjoin=(followers.c.followed_id == id),
    #                            backref=db.backref('followers', lazy='dynamic'),
    #                            lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def getResetToken(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verifyResetToken(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.leads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(UserMixin,db.Model):
    '''
    Class is responsible for creating new tasks.
    '''
    id = db.Column(db.Integer, primary_key=True)
    nameTitle = db.Column(db.String(256),  index=True)
    content = db.Column(db.UnicodeText, index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    complete = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Posts {}>'.format(self.nameTitle)

# @login.user_loader
# def load_user(id):
#     return User.query.get(int(id))