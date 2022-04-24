from asyncio.windows_events import NULL
from config import consumer_key, consumer_secret, access_token, access_token_secret, bearer_token
from aux_functions import create_dict, create_sorted_dict, get_datetime_utc, get_default_start_date, most_common, create_tweet_list, make_query

import tweepy
import string
import pandas as pd
from plotnine import *

client = tweepy.Client(bearer_token=bearer_token)

usernames = ['elonmusk', 'pmarca']
keywords = ['Boring']
new_query = make_query(usernames, 'OR', 'OR', include_retweet=False, include_reply=False)

start_time = get_default_start_date()
end_time = get_datetime_utc()

new_tweets = client.search_recent_tweets(query=new_query, start_time=start_time, end_time = end_time, tweet_fields = ["created_at", "text", "source"],
             user_fields = ["name", "username", "location", "verified", "description"], max_results = 10, expansions='author_id')

# print(new_tweets) # save as CSV or whatever to not keep querying
# print(new_tweets.data)

def main():
    print(get_datetime_utc())

    most_common_list = most_common(create_sorted_dict(create_dict(create_tweet_list(new_tweets))), 5, True)
    print(most_common_list)

    df_1 = pd.DataFrame(most_common_list, columns = ['frequency', 'word'])
    print(df_1)

    print((ggplot(df_1, aes(y = 'frequency', x = 'word', fill = 'word', color = 'word')) # https://plotnine.readthedocs.io/en/stable/
    + geom_bar(stat = 'identity') 
    + theme(legend_position = 'bottom', legend_title = element_blank())
    + scale_y_continuous(minor_breaks = NULL)
    + labs(x = '', y = '', title = 'Frequency of Word (Y) vs. Word Name (X) by Word Name (Colors) and Word Name (Facets)')))
    + facet_wrap('~movie_name', ncol = 3, scales = 'free_x')

if __name__ == '__main__':
    main()





