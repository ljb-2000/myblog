# -*- coding: UTF-8 -*- 
__author__ = 'agmcs'
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import validators


class LoginForm(Form):
    name = StringField(u'用户名',validators=[validators.data_required()])
    password = PasswordField(u'密码',validators=[validators.data_required()])
    # password2 = PasswordField(u'再输入一遍',validators=[validators.data_required, validators.EqualTo('password',u'密码不同')])
    remember_me = BooleanField(u'记住我')
    submit = SubmitField(u'登陆')