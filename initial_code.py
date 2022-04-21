from config import consumer_key, consumer_secret, access_token, access_token_secret, bearer_token
import os
import requests
import json
import pandas as pd
import datetime
import dateutil.parser
import time
import unicodedata
import tweepy

# os.environ['TOKEN'] = '<BEARER_TOKEN>'

# def auth():
#     return os.getenv('TOKEN')

# def create_headers(bearer_token):
#     headers = {"Authorization": "Bearer {}".format(bearer_token)}
#     return headers

# def create_url(keyword, start_date, end_date, max_results = 10):
    
#     search_url = "https://api.twitter.com/2/tweets/search/all" #Change to the endpoint you want to collect data from

#     #change params based on the endpoint you are using
#     query_params = {'query': keyword,
#                     'start_time': start_date,
#                     'end_time': end_date,
#                     'max_results': max_results,
#                     'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
#                     'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
#                     'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
#                     'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
#                     'next_token': {}}
#     return (search_url, query_params)

# def connect_to_endpoint(url, headers, params, next_token = None):
#     params['next_token'] = next_token   #params object received from create_url function
#     response = requests.request("GET", url, headers = headers, params = params)
#     print("Endpoint Response Code: " + str(response.status_code))
#     if response.status_code != 200:
#         raise Exception(response.status_code, response.text)
#     return response.json()

# bearer_token = auth()
# headers = create_headers(bearer_token)
# keyword = "xbox lang:en"
# start_time = "2021-03-01T00:00:00.000Z"
# end_time = "2021-03-31T00:00:00.000Z"
# max_results = 15

# url = create_url(keyword, start_time,end_time, max_results)
# json_response = connect_to_endpoint(url[0], headers, url[1])

# print(json.dumps(json_response, indent=4, sort_keys=True))
# # authentication

# auth = tweepy.OAuthHandler(consumer_key = consumer_key, consumer_secret = consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)
# print(api.update_status('tweepy + oauth!'))

# username_tweets = tweepy.Cursor(api.user_timeline, screen_name="elonmusk", tweet_mode='extended').items(10)
# print(username_tweets)

# list = []
# for tweet in username_tweets:
#     text = tweet._json["full_text"]

#     refined_tweet = {'text' : text,
#                     'favorite_count' : tweet.favorute_count,
#                     'retweet_count' : tweet.retweet_count,
#                     'created_at' : tweet.created_at}
    
#     list.append(refined_tweet)

# username_tweets_list = [tweet.text for tweet in username_tweets]
# print(username_tweets_list[0])  

# try:
#     redirect_url = auth.get_authorization_url()
# except tweepy.TweepError:
#     print 'Error! Failed to get request token.'

# bearer_token = os.environ.get("BEARER_TOKEN")

# search_url = "https://api.twitter.com/2/tweets/search/recent"

# # Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# # expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
# query_params = {'query': '(from:twitterdev -is:retweet) OR #twitterdev','tweet.fields': 'author_id'}


# def bearer_oauth(r):
#     """
#     Method required by bearer token authentication.
#     """

#     r.headers["Authorization"] = f"Bearer {bearer_token}"
#     r.headers["User-Agent"] = "v2RecentSearchPython"
#     return r

# def connect_to_endpoint(url, params):
#     response = requests.get(url, auth=bearer_oauth, params=params)
#     print(response.status_code)
#     if response.status_code != 200:
#         raise Exception(response.status_code, response.text)
#     return response.json()


# def main():
#     json_response = connect_to_endpoint(search_url, query_params)
#     print(json.dumps(json_response, indent=4, sort_keys=True))


# if __name__ == "__main__":
#     main()