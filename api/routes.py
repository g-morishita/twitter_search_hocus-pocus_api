from api import api, tw_api
from flask import jsonify

@api.route('/hashtags/<string:hashtag>', methods=['GET'])
def getByHashtags(hashtag):
    """
    Returns the list of tweets with a given hashtag in JSON format
    """
    
    # get a response by a hashtag
    hs_response = tw_api.request('search/tweets', { 'q': hashtag })

    # convert TwitterResponse object to list of dict
    hs_result = []
    for tweet in hs_response:
        hs_result.append(tweet)

    return jsonify(hs_result)

@api.route('/users/<string:user>', methods=['GET'])
def getByUser(user):
    """
    Returns the list of tweets that certain user has on his/her own feed in JSON format
    """
    pass
