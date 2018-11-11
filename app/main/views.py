from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news
from ..models import News,Sources

@main.route('/')
def index():
    live_news = get_news('kenya')
    title = 'Home - The home to global news'

    search_news = request.args.get('news_search')
    if search_news:
        return redirect(url_for('search',news_feed=search_news))
    else:
        return render_template('index.html',updates = live_news,title= title)

@main.route('/search/<news_feed>')
def search(news_feed):
    search_list = news_feed.split(" ")
    title_format = "+".join(search_list)
    # news_feed = get_news(title_format)
    searched_news = get_news(title_format)
    title = 'News results'
    return render_template('search.html',related=searched_news,title=title)

