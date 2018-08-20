from flask import Flask
from config import Config
from TwitterAPI import TwitterAPI

# initialization and configuration
api = Flask(__name__)
api.config.from_object(Config)

# authorize 
tw_api = TwitterAPI(api.config['CONSUMER_KEY'], api.config['CONSUMER_SECRET'], api.config['ACCESS_TOKEN_KEY'], api.config['ACCESS_TOKEN_SECRET'])

from api import routes 
