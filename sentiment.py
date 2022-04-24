from config import consumer_key, consumer_secret, access_token, access_token_secret, bearer_token
from aux_functions import analyze_sentiment, create_tweet_list, get_datetime_utc, get_default_start_date, make_query

import tweepy
import pandas as pd

client = tweepy.Client(bearer_token=bearer_token)

usernames = ['elonmusk', 'pmarca']
keywords = ['Boring']
new_query = make_query(usernames, 'OR', 'OR', include_retweet=False, include_reply=False)

start_time = get_default_start_date()
end_time = get_datetime_utc() 

new_tweets = client.search_recent_tweets(query=new_query, start_time=start_time, end_time = end_time, tweet_fields = ["created_at", "text", "source"],
             user_fields = ["name", "username", "location", "verified", "description"], max_results = 10, expansions='author_id')

def main():
    sentiment_list = analyze_sentiment(create_tweet_list(new_tweets))
    sentiment_df = pd.DataFrame(sentiment_list, columns = ['sentiment', 'value'])
    print(sentiment_df)

if __name__ == '__main__':
    main()