from flask import Flask
from config import Config
from TwitterAPI import TwitterAPI

# initialization and configuration
api = Flask(__name__)
api.config.from_object(Config)

# authorize 
print(api.config['CONSUMER_KEY'])
print(api.config['CONSUMER_SECRET'])
print(api.config['ACCESS_TOKEN_KEY'])
print(api.config['ACCESS_TOKEN_SECRET'])
tw_api = TwitterAPI(api.config['CONSUMER_KEY'], api.config['CONSUMER_SECRET'], api.config['ACCESS_TOKEN_KEY'], api.config['ACCESS_TOKEN_SECRET'])
r = tw_api.request('search/tweets', { 'q': 'pizza' })
print(r.status_code)
count = 0
for i in r:
    count += 1
print(count)

from api import routes 
