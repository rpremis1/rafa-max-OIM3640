from config import consumer_key, consumer_secret, access_token, access_token_secret, bearer_token

import tweepy
import json
# import pandas as pd
# import plotnine

client = tweepy.Client(bearer_token=bearer_token)

# query = 'from:suhemparack -is:retweet'

# tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

# for tweet in tweets.data:
#     print(tweet.text)
#     if len(tweet.context_annotations) > 0:
#         print(tweet.context_annotations)

# new_query = 'from:elonmusk boring -is:retweet -is:reply'
new_query = 'from:elonmusk OR from:pmarca -is:retweet -is:reply'
start_time = '2022-04-19T00:00:00z'
# end_time = '2022-04-21T00:00:00z'

new_tweets = client.search_recent_tweets(query=new_query, start_time=start_time, tweet_fields = ["created_at", "text", "source"],
             user_fields = ["name", "username", "location", "verified", "description"], max_results = 10, expansions='author_id')

# new_tweets = client.search_recent_tweets(query=new_query, start_time=start_time, end_time=end_time, tweet_fields = ["created_at", "text", "source"],
#              user_fields = ["name", "username", "location", "verified", "description"], max_results = 10, expansions='author_id')

# print(new_tweets) # save as CSV or whatever to not keep querying
print(new_tweets.data)


