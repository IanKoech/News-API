from flask import render_template
from . import main
from ..request import get_sources,get_articles


#views 
@main.route('/')
def index():
    """
    View root page function that returns index page and the various news sources
    """
    
   
    # Getting the news sources
    news_source=get_articles('general')
    
    return render_template('index.html', title = title, sources = news_source ,statement = tag_line)


@main.route('/articles/<source_id>')  
def articles(source_id):
    '''
    View function that retuns that renders the source articles
    '''
    tag = f'{source_id}'
    news_articles = get_articles(source_id)
    return render_template('articles.html',articles = news_articles,tag = tag)