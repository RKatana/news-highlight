import urllib.request,json
from .models import News, Sources

api_key = None
base_url = None

def configure_request(app):
    global api_key, base_url
    # api_key= app.config['NEWS_API_KEY']
    api_key = 'dfab4670bae14b02bc7e9ae068f638bd'
    base_url = app.config['NEWS_API_BASE_URL']

def get_news(kenya):
    '''
    This function loads the url in a json readable form
    '''
    # get_news_url = base_url.format(kenya,api_key)
    get_news_url= 'https://newsapi.org/v2/everything?q={}&sortBy=publishedAt&language=en&apiKey={}'.format(kenya,api_key)
    print(get_news_url)
    with urllib.request.urlopen(get_news_url) as url:
        news_data = url.read()
        news_response = json.loads(news_data)
        news_results = None

        if news_response['articles']:
            news_results_list = news_response['articles']
            news_results = process_results(news_results_list)
        return news_results
def process_results(news_updates):
    '''
    This function returns a list of news articles
    '''
    news_results = []
    for news_object in news_updates:
        name = news_object.get('name')
        author =  news_object.get('author')
        title = news_object.get('title')
        description = news_object.get('description')
        url = news_object.get('url')
        urlToImage =news_object.get('urlToImage')
        publishedAt = news_object.get('publishedAt')
        content = news_object.get('content')

        new_article = News(name,author,title,description,url,urlToImage,publishedAt,content)
        news_results.append(new_article)
    return news_results
#The function to load the news sources
def news_sources(sources):
    '''
    This function loads the url in a json readable form
    '''
    # get_news_url = base_url.format(kenya,api_key)
    news_source_url= 'https://newsapi.org/v2/sources?q={}&apiKey={}'.format(sources,api_key)
    with urllib.request.urlopen(news_source_url) as url:
        source_data = url.read()
        news_response = json.loads(source_data)
        source_results = None

        if news_response['sources']:
            news_results_list = news_response['sources']
            source_results = process_results(news_results_list)
        return source_results

def source_results(sources):
    '''
    This function returns a list of news articles
    '''
    source_results = []
    for source in sources:
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')

        new_source = Sources(name,description,url,category)
        source_results.append(new_source)
    return source_results


