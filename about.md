# Instructions for the use of this website

This website uses the Twitter API to retrieve information the user desires. Before discussing the specific use cases of each of the functions of this website, we shall first discuss the usage and limitations of the Twitter API. The Twitter API has multiple parameters available for usage, though in our case we are interested in only a few specific ones: usernames, keywords, date intervals, and max results. In order to query from the whole tweet database, one would need to be granted academic access to the Twitter API -- which is only available to Master's/PhD students. As such, our queries have an important limitation: it can only search for tweets in the previous seven days. Given this constraint, we have chosen to automatically input the last seven days into our query in order to avoid issues, and because allowing users to specify dates conditional on the last seven would be relatively redundant. Alas, the user should input a username(s), keyword (can be left blank), number of results (min: 10, max: 100), and whether he/she wants retweets and/or replies by this user to be included. 

## Tweets

This page allows a user to search for tweets by a certain user(name) containing a keyword, and specify whether or not they want to include retweets/replies. The following is an example of a query looking for tweets by Elon Musk containing the word 'speech' that can include retweets and replies.

![tweets](images/tweet_list.jpeg.png)

# 