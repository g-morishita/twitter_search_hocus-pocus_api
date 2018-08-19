import os

class Config(object):
    CONSUMER_KEY        = os.environ.get('CONSUMER_KEY')        or ''
    CONSUMER_SECRET     = os.environ.get('CONSUMER_SECRET')     or ''
    ACCESS_TOKEN_KEY    = os.environ.get('ACCESS_TOKEN_KEY')    or ''
    ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET') or ''
