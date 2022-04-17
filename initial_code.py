from config import consumer_key, consumer_secret, access_token, access_token_secret, bearer_token
import os
import requests
import json
import tweepy

# authentication
auth = tweepy.OAuthHandler(consumer_key = consumer_key, consumer_secret= consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth=auth)

print(api.update_status('tweepy + oauth!'))
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