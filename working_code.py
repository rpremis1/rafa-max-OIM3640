from config import consumer_key, consumer_secret, access_token, access_token_secret, bearer_token
from aux_functions import create_dict, create_sorted_dict, process_file, most_common

import tweepy
import json
import string
# import pandas as pd
# import plotnine

client = tweepy.Client(bearer_token=bearer_token)

# query = 'from:suhemparack -is:retweet'

# tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

# for tweet in tweets.data:
#     print(tweet.text)
#     if len(tweet.context_annotations) > 0:
#         print(tweet.context_annotations)

# new_query = 'from:elonmusk OR from:pmarca boring -is:retweet -is:reply'
new_query = 'from:elonmusk -is:retweet -is:reply'
start_time = '2022-04-15T00:00:00z'
# end_time = '2022-04-21T00:00:00z'

new_tweets = client.search_recent_tweets(query=new_query, start_time=start_time, tweet_fields = ["created_at", "text", "source"],
             user_fields = ["name", "username", "location", "verified", "description"], max_results = 10, expansions='author_id')

# new_tweets = client.search_recent_tweets(query=new_query, start_time=start_time, end_time=end_time, tweet_fields = ["created_at", "text", "source"],
#              user_fields = ["name", "username", "location", "verified", "description"], max_results = 10, expansions='author_id')

# print(new_tweets) # save as CSV or whatever to not keep querying
# print(new_tweets.data)

def create_tweet_list(tweets):
    lst = []
    for tweet in tweets.data:
        lst.append(tweet.text)
    return lst

a_list = create_tweet_list(new_tweets)

a_dict = create_dict(a_list)
sorted_dict = create_sorted_dict(a_dict)
most_common_list = most_common(sorted_dict, 5, True)

print(most_common_list)





