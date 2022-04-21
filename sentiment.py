from config import consumer_key, consumer_secret, access_token, access_token_secret, bearer_token
from aux_functions import analyze_sentiment, create_dict, create_sorted_dict, process_file, most_common, create_tweet_list

import tweepy
import json
import nltk
# nltk.download('vader_lexicon') # This is needed to run the sentiment analyis
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

client = tweepy.Client(bearer_token=bearer_token)

new_query = 'from:elonmusk -is:retweet -is:reply'
start_time = '2022-04-15T00:00:00z'

new_tweets = client.search_recent_tweets(query=new_query, start_time=start_time, tweet_fields = ["created_at", "text", "source"],
             user_fields = ["name", "username", "location", "verified", "description"], max_results = 10, expansions='author_id')

def main():
    a_list = create_tweet_list(new_tweets)
    sentiment_list = analyze_sentiment(a_list)
    sentiment_df = pd.DataFrame(sentiment_list, columns = ['sentiment', 'value'])
    print(sentiment_df)

if __name__ == '__main__':
    main()