# Twitter Search Hocus Pocus API

## Description
Twitter Search Hocus Pocus API is a RESTful API that offers two methods to get tweets easily. 

They are:

1. to get a list of tweets with a given hashtag in JSON format.
2. to get a list of tweets certain user has on his/her own feed in JSON format.

Here is how the API works.

If you want to get tweets with a hashtag #Avengers, 

```
curl -X GET "http://localhost:5000/hashtags/Avengers" -H "accept: application/json"
```

Likewise, if you want to get tweets someone specific(let's say Kyary Pamyu Pamyu) has on his/her feed,

```
curl -X GET "http://localhost:5000/users/pamyurin" -H "accept: application/json"
```

## Requirements

### python version
- python>=3.0

### pip 
- flask>=1.0
- TwitterAPI
- (requests)

`requests` package is required only if you run tests.

## Set up

for windows users(Power shell), you must use `set` instead of `export`.

### install the required packages

Make sure you have installed python>=3.0.

run the following command.

```
$ pip install flask TwitterAPI
```

### Set Twitter Token to the environment variables

If you do not have Twitter access token and secret, you have to get them [here](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html).

After that, run on a bash

```
$ export CONSUMER_KEY="<your consumer key>"
$ export CONSUMER_SECRET="<your consumre secret>"
$ export ACCESS_TOKEN_KEY="<your access token key>"
$ export ACCESS_TOKEN_SECRET="<your access token secret>"
```

Make sure that the keys and secrets are between `"`. 

On Linux, that does not matter, however, on Powershell it matters.

You are ready to use Twitter API.

### Set FLASK_APP

run on a bash

```
$ export FLASK_APP=search_api.py
```

The setting is over now.

## Run the API endpoints

run this in a project root directory where README.md is located.

```
$ flask run
```

You can access to `http://localhost:5000`.

## Check if the API works

In the browser, type `http://localhost:5000/hashtags/Avengers` let's say.

If you see long text which is in JSON format, it works out perfectly.

Of course, you can check it using `curl` or `wget`.

## Documentation
read `document.html`, which is included in a repository.
