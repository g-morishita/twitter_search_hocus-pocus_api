from api import api

@bp.route('/hashtags/<str:hashtag>', method=['GET'])
def getByHashtags(hashtag):
    """
    Returns the list of tweets with a given hashtag in a JSON format
    """
    pass

@bp.route('/users/<str:user>', method=['GET'])
def getByUser(user):
    """
    Returns the list of tweets that certain user tweeted in a JSON format
    """
    pass
