from api import api, tw_api
from flask import jsonify, request
from api.helper import convert_resp2list

def convert_resp2list(response):
    """ 
    convert TwitterResponse object to list of dict
    """
    response_list = []
    for tweet in response:
        response_list.append(tweet)

    return response_list

@api.route('/hashtags/<string:hashtag>', methods=['GET'])
def getByHashtags(hashtag):
    """
    Returns the list of tweets with a given hashtag in JSON format
    """

    # page_limits 
    DEFAULT_PAGES = 1
    pages_limit = request.args.get('pages_limit') or DEFAULT_PAGES 

    # get a response by a hashtag
    hs_response = tw_api.request('search/tweets', { 'q': '#' + hashtag, 'count': 100 })
    hs_result = convert_resp2list(hs_response)

    return jsonify(hs_result)

@api.route('/users/<string:user>', methods=['GET'])
def getByUser(user):
    """
    Returns the list of tweets that certain user has on his/her own feed in JSON format
    """

    # get a response by a username
    usr_response = tw_api.request('statuses/user_timeline', { 'screen_name': user })
    usr_result = convert_resp2list(usr_response)

    return jsonify(usr_result)
