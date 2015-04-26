# -*- coding: UTF-8 -*- 
__author__ = 'agmcs'
from app import db, loginManager
from flask.ext.login import UserMixin, AnonymousUserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

#用户
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128),unique=True)
    name = db.Column(db.String(64),unique=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise "Password cant be read"

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return "<User %r>" %self.name

    def __unicode__(self):
        return self.name


#文章
class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(25), nullable=False)
    body = db.Column(db.Text, nullable=False)
    modify_date = db.Column(db.DateTime, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('categorys.id'))
    def __repr__(self):
        return "<Article %r>" %self.title

    def __unicode__(self):
        return self.title


tag_article = db.Table('registrations',
                       db.Column('tag_id',db.Integer,db.ForeignKey('tags.id')),
                       db.Column('article_id',db.Integer,db.ForeignKey('articles.id'))
                       )


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24))
    articles = db.relationship('Article',
                               secondary = tag_article,
                               backref=db.backref('tags',lazy = 'dynamic'),
                               lazy='dynamic')

    def __repr__(self):
        return "<Tag %r>" %self.name

    def __unicode__(self):
        return self.name


#友情链接
class FriendLink(db.Model):
    __tablename__ = 'friendlinks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    url = db.Column(db.String(120))

    def __repr__(self):
        return "<FriendLink %r>" %self.name

    def __unicode__(self):
        return self.name


class Category(db.Model):
    __tablename__ = 'categorys'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    articles = db.relationship('Article',backref = 'category', lazy = 'dynamic')

    def __repr__(self):
        return "<Category %r>" %self.name

    def __unicode__(self):
        return self.name



@loginManager.user_loader
def load(user_id):
    return User.query.get(int(user_id))