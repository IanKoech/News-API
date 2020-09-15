class Articles:
    '''
    Class to define article objects
    '''
    def __init__(self,author,publishedAt,title,urlToImage,description,url):
        self.author=author
        self.publishedAt=publishedAt
        self.title=title
        self.urlToImage=urlToImage
        self.description=description
        self.url=url