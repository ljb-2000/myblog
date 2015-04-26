# -*- coding: UTF-8 -*- 
__author__ = 'agmcs'
from flask import render_template
from flask import url_for, redirect, request
from flask.ext.admin import BaseView, expose,AdminIndexView
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.base import MenuLink
from flask.ext.login import current_user
from .form import LoginForm
from ..models import User
from flask.ext.login import login_user,logout_user,login_required
from wtforms import widgets,fields


class CKTextAreaWidget(widgets.TextArea):

    def __call__(self, field, **kwargs):
        kwargs.setdefault('class_', 'ckeditor')
        kwargs.pop('class','')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(fields.TextField):
    widget = CKTextAreaWidget()


class MyIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if current_user.is_authenticated():
            print "dfsfs"
            return self.render('admin/index.html')
        else:
            return redirect(url_for('.login'))

    @expose('/login',methods=['GET','POST'])
    def login(self):
        print "dsfsdg"
        form = LoginForm()
        if form.validate_on_submit():
            u = User.query.filter_by(name = form.name.data).first()
            if u is not None and u.check_password(form.password.data):
                login_user(u)
                return redirect(request.args.get('next') or url_for('.index'))
        return self.render('admin/login.html', form = form)


    @expose('/logout')
    @login_required
    def logout(self):
        logout_user()
        return redirect(url_for('.index'))



class PostView(ModelView):
    form_overrides = dict(body=CKTextAreaField)
    def is_accessible(self):
        return current_user.is_authenticated()

class UserView(ModelView):
    # column_list = ('email', 'name', 'articles')
    # column_searchable_list = ('name', 'email')#可搜索字段
    # inline_models = (Article,)#内联对象
    # inline_models = [(Article, dict(form_columns=['title']))]
    # form_choices = {'my_form_field': [
    #     ('name', 'display_value'),
    # ]}
    def is_accessible(self):
        return current_user.is_authenticated()


class FriendLinkView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated()


class TagView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated()

class CategoryView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated()