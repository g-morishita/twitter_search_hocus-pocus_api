import os

class Config(object):
    # configure Twitter API token from the environment variables
    # you can hard-code your token here instead of os.environ.get
    CONSUMER_KEY        = os.environ.get('CONSUMER_KEY')        or ''
    CONSUMER_SECRET     = os.environ.get('CONSUMER_SECRET')     or ''
    ACCESS_TOKEN_KEY    = os.environ.get('ACCESS_TOKEN_KEY')    or ''
    ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET') or ''
