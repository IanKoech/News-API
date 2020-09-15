from flask import render_template,request,redirect,url_for
from app import app

@app.route('/')
def index():
    '''
    Default page 
    '''
    message='News Application is running smoothly'
    return render_template('index.html',message=message)

@app.route('/search/<org_name>')
def search(org_name):
    """
    This method returns news from different news pages
    """
    company=f'{org_name}'