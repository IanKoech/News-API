class Source:
    '''
    Source class to define source objects
    '''

    def __init__(self, id, name, description, url, category, language, country):
        
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.catergory = category
        self.language = language
        self.country = country

class Article:
    '''
    Class to define article objects
    '''

    def __init__(self, id, name, author, title, description, url, urlToImage, publishedAt):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt