from api import api, tw_api
from flask import jsonify, request
from api.helper import convert_resp2list, get_response
from TwitterAPI import TwitterPager

@api.route('/hashtags/<string:hashtag>', methods=['GET'])
def getByHashtags(hashtag):
    """
    Returns the list of tweets with a given hashtag in JSON format
    pages_limit: One page has 100 tweets. You can set the limit of the number of pages.
        Usage: hashtags/<hashtag>?pages_limit=3

    Note that if you search by a hashtag no one uses, return a empty list alike the users endpoint.
    """

    # set page_limits. The default is 1 
    pages_limit = request.args.get('pages_limit') or 1
    pages_limit = int(pages_limit)

    raw_response = get_response(tw_api, 'search/tweets', { 'q': '#' + hashtag, 'count': 100 }, pages_limit)
    list_response = convert_resp2list(raw_response)
    return jsonify(list_response)

@api.route('/users/<string:user>', methods=['GET'])
def getByUser(user):
    """
    Returns the list of tweets that certain user has on his/her own feed in JSON format
    pages_limit: One page has 100 tweets. You can set the limit of the number of pages.
        Usage: hashtags/<hashtag>?pages_limit=3

    Note that if you search by a user that does not exist, return a JSON which includes an error message
    """

    # set page_limits. The default is 1 
    pages_limit = request.args.get('pages_limit') or 1
    pages_limit = int(pages_limit)

    raw_response = get_response(tw_api, 'statuses/user_timeline', {'screen_name' : user, 'count': 100 }, pages_limit)
    list_response = convert_resp2list(raw_response)
    return jsonify(list_response)
