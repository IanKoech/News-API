from flask import Flask
from flask_bootstrap import flask_bootstrap
from config import config_options

bootstrap=Bootstrap(app)
app=Flask(__name__,instance_relative_config=True)

#Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')
from app import views,error