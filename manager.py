# -*- coding: UTF-8 -*-
from flask import url_for
from flask.ext.admin import Admin

__author__ = 'agmcs'
from app import create_app, db
from flask.ext.script import Manager, Shell
from flask.ext.migrate import MigrateCommand, Migrate
from app.models import User, Article, FriendLink,Tag, Category

app = create_app('dev')
manager = Manager(app)
migrate = Migrate(app, db=db)

manager.add_command("db", MigrateCommand)

def init_context():
    return dict(app=app, db=db, User=User, Article=Article, FriendLink=FriendLink,Tag=Tag, Category=Category)

manager.add_command('shell', Shell(make_context=init_context))








if __name__ == '__main__':
    manager.run()