import urllib.request,json
from .models import Articles
#Getting the api key
api_key=None
#Getting movie base url
base_url=None
def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
#Import the app instance and from it form api key from config object

#urllib.request module helps create a connection to our API URl and send requests and json modules format

def get_news(category):
    """
    Function that gets json response to our url request
    """
    get_news_url=base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data=url.read()
        get_news_response=json.loads(get_news_data)
        news_results=None

        if get_news_response['results']:
            news_results_list=get_news_response['results']
            news_results=process_results(news_results_list)

    return news_results

def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects
    Args:
        movie_list: A list of dictionaries that contain movie details
    Returns :
        movie_results: A list of movie objects
    '''
    news_results = []
    for news_item in news_list:
        author = news_item.get('author')
        publishedAt = news_item.get('publishedAt')
        title = news_item.get('title')
        urlToImage = news_item.get('urlToImage')
        description = news_item.get('description')
        url = news_item.get('url')

        news_object = Articles(author,publishedAt,title,urlToImage,description,url)
        article_results.append(article_object)
    return news_results

def get_articles(id):
    get_article_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_article_details_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

        article_object = None
        if article_details_response['articles']:
            articles_results_list = article_details_response['articles']
            articles_results = process_results(articles_results_list)

    return articles_results

