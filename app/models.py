class News:
    '''
    This class defines the news object
    '''
    def __init__(self,name,author,title,description,url,urlToImage,publishedAt,content):
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content

class Sources:
    '''
    This class returns the sources
    '''
    def __init__(self,name,description,category,url):
        self.name = name
        self.description = description
        self.category = category
        self.url = url
        