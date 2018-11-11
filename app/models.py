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
    def __init__(self,id,name):
        self.id = id
        self.name = name
        