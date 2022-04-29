from asyncio.windows_events import NULL
from types import NoneType
from config import bearer_token
from aux_functions import get_datetime_utc, get_default_start_date, make_query

import tweepy

client = tweepy.Client(bearer_token=bearer_token)


def main():
    usernames = ['elonmusk']
    keywords = ['speech']
    new_query = make_query(usernames, 'OR', 'OR', keywords=keywords,
                           include_retweet=False, include_reply=False)

    start_time = get_default_start_date()
    end_time = get_datetime_utc()
    max_results = 100

    new_tweets = client.search_recent_tweets(query=new_query, start_time=start_time, end_time=end_time, tweet_fields=["created_at", "text", "source"],
                                             user_fields=["name", "username", "location", "verified", "description"], max_results=max_results, expansions='author_id')

    if type(new_tweets.data) == NoneType:
        print('Not working')
    else:
        for tweet in new_tweets.data:
                print(tweet.text)

if __name__ == "__main__":
    main()
