def convert_resp2list(response, pages_limit = 1):
    """ 
    convert TwitterResponse object to list of dict

    response : TwitterResponse
    pages_limit : int
        the limited number of pages 

    return : list
        the list of response
    """
    from TwitterAPI.TwitterError import TwitterRequestError
    
    response_list = []
    limit_tweets = 1

    try:
        for tweet in response.get_iterator():
            if 'text' in tweet:
                response_list.append(tweet)

            # if exceed week's worth maxiumu, then don't get tweets anymore
            elif 'message' in tweet and tweet['code'] == 88:
                response_list.append(tweet)
                print('SUSPEND, RATE LIMIT EXCEEDED: {}\n'.format(item['message']))
                break

            # if exceed pages_limit, then don't get tweets anymore
            limit_tweets += 1
            if ( limit_tweets > pages_limit * 100):
                break
    except TwitterRequestError as tw_e:
        return [{'error' : 'No tweets or users found'}]

    return response_list

def get_response(tw_api, method, options, pages_limit):
    """
    using TwitterPager, search tweets according to a given method
    The format is in JSON.
    If there is no tweets found, the message that No tweets found is returned 
    tw_app : TwitterAPI object
    method : string
        ex) 'serach/tweets', 'statuses/user_timeline'
    options : dict
        ex) '{ 'screen_name': name }, {'q' : query }
    pages_limit : int
        the limited number of pages
    
    return : the Jsonified list of tweets
    """

    from TwitterAPI import TwitterPager

    response = TwitterPager(tw_api, method, options)
    return response
