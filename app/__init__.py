# -*- coding: UTF-8 -*-
from flask.ext.admin.menu import MenuLink

__author__ = 'agmcs'
from flask import Flask, url_for
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.moment import Moment
from flask.ext.admin import Admin
from flask.ext.bootstrap import Bootstrap
from Config import config
loginManager = LoginManager()
loginManager.session_protection = 'strong'
loginManager.login_view = 'auth.login'
bootstrap = Bootstrap()


db = SQLAlchemy()
moment = Moment()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    loginManager.init_app(app)
    db.init_app(app)
    moment.init_app(app)
    bootstrap.init_app(app)


    #Blueprint
    from main import main
    app.register_blueprint(main)
    #admin

    from app.admins.adminViews import MyIndexView,PostView,UserView,FriendLinkView,TagView,CategoryView
    from app.models import User,Article,FriendLink,Tag, Category
    admin = Admin(app = app,template_mode='bootstrap3',name='Hei', endpoint='admin',index_view=MyIndexView())
    admin.add_view(PostView(Article,db.session,name=u'文章管理'))
    admin.add_view(FriendLinkView(FriendLink,db.session,name=u'友情链接'))
    admin.add_view(TagView(Tag,db.session,name=u'标签管理'))
    admin.add_view(CategoryView(Category,db.session,name=u'分类管理'))

    return app
