import os
class Config:
    NEWS_API_BASE_URL='https://newsapi.org/v2/everything?q={}&from=2018-10-09&sortBy=publishedAt&language=en&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}