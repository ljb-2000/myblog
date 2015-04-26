# -*- coding: UTF-8 -*- 
__author__ = 'agmcs'
from . import main
from flask import render_template, abort, request
from app.models import Article, Tag, FriendLink, Category


@main.route('/search',methods=['GET','POST'])
def search():

    text = request.args.get('search','')
    page = request.args.get('p', 1, type=int)
    pagenation = Article.query.filter(Article.title.like('%' + text + '%')).order_by(Article.modify_date.desc()).paginate(page, per_page=7, error_out = False)
    posts = pagenation.items

    return render_template('index.html', pagenation = pagenation, posts = posts, **global_map())


def global_map():
    tags = Tag.query.all()
    links = FriendLink.query.all()
    categorys = Category.query.all()
    map = {
         'tags': tags,
         'links': links,
         'categorys':categorys
    }
    return map


@main.route('/')
def index():
    page = request.args.get('p', 1, type=int)
    pagenation = Article.query.order_by(Article.modify_date.desc()).paginate(page, per_page=7, error_out = False)
    posts = pagenation.items
    return render_template('index.html', pagenation = pagenation, posts = posts, **global_map())


@main.route('/p/<int:id>')
def article(id):
    post = Article.query.get_or_404(int(id))
    return render_template('article.html',post = post, **global_map())

@main.route('/tag/<int:id>')
def by_tag(id):
    tag = Tag.query.get_or_404(id)

    page = request.args.get('p', 1, type=int)
    pagenation = tag.articles.paginate(page, per_page=7, error_out = False)
    posts = pagenation.items
    return render_template('by_tag.html', pagenation = pagenation,id=id, posts = posts, **global_map())


@main.route('/category/<int:id>')
def by_category(id):
    category = Category.query.get_or_404(int(id))

    page = request.args.get('p', 1, type=int)
    pagenation = category.articles.paginate(page, per_page=7, error_out = False)
    posts = pagenation.items
    return render_template('by_category.html', pagenation = pagenation,id=id, posts = posts, **global_map())