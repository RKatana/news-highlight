from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news
from ..models import All_news

@main.route('/')
def index():
    live_news = get_news()
    title = 'Home - The home to global news'
    return render_template('index.html',updates = live_news,title= title)