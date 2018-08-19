from api import api

@api.route('/hashtags/<str:hashtag>', methods=['GET'])
def getByHashtags(hashtag):
    """
    Returns the list of tweets with a given hashtag in JSON format
    """
    pass

@api.route('/users/<str:user>', methods=['GET'])
def getByUser(user):
    """
    Returns the list of tweets that certain user has on his/her own feed in JSON format
    """
    pass
