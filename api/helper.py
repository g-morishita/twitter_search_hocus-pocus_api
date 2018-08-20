def convert_resp2list(response):
    """ 
    convert TwitterResponse object to list of dict
    """
    response_list = []
    for tweet in response:
        response_list.append(tweet)

    return response_list
