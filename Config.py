# -*- coding: UTF-8 -*- 
__author__ = 'agmcs'
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "sdgi3h4igkfv"
    CSRF_ENABLE = True
    SQLALCHEMY_SUBMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app():
        pass

class Dev(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'database.db')
    DEBUG = True


config = {'default': Dev,
          'dev': Dev
          }