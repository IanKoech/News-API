import urllib.request , json
from .models import Article 

# Getting api key
api_key = None

# Getting article url
article_url = None

def configure_request(app):
    api_key = app.config['NEWS_API_KEY']
    article_url = app.config['NEWS_API_BASE_URL']



def get_article(id):
    '''
    Function to get json to respond to url request
    '''
    get_article_url=article_url.format(id,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = process_articles(article_results_list)

    return article_results        

def process_articles(article_results_list):
    '''
    This function processes the articles results and transfers them to a list of objects
    
    Args:
        article_list: dictionaties that contain article details
    Returns:
        article_results: article objects
    '''
    article_results = []
    for article_item in article_results_list:
        id = article_item.get('id')
        name = article_item.get('name')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')

        if urlToImage:
            article_object = Article(id, name, author, title, description, url, urlToImage, publishedAt)
            article_results.append(article_object)

    return article_results  