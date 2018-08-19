# Twitter Search Hocus Pocus API

## Description
Twitter Search Hocus Pocus API is a RESTful API that offers two methods to get tweets easily. 

They are:

1. to get a list of tweets with a given hashtag in a JSON format.
2. The second one is to get a list of tweets certain user tweets in a JSON format.

Here is how the API works.

If you want to get tweets with a hashtag #Avengers, 

```
curl -X GET "http://localhost:5000/hashtags/Avengers" -H "accept: application/json"
```

Likewise, if you want to get tweets someone specific tweeted,

```
curl -X GET "http://localhost:5000/users/pamyurin" -H "accept: application/json"
```

