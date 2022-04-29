import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from datetime import datetime, timezone, timedelta 

def create_dict(listed_tweets):
    """
    Returns a dictionary mapping words and their respective frequencies, given a list of tweets.

    Parameters
    ----------
    listed_reviews: list
    """
    res = {}
    for line in range(len(listed_tweets)):
        line = listed_tweets[line]
        word = line.split()
        for words in word:
            res[words] = res.get(words, 0) + 1
    return res

def create_sorted_dict(a_dict):
    """
    Returns a dictionary of sorted word:frequency pairs given a dictionary.

    Parameters
    ----------
    a_dict: dict
    """
    sorted_keys = sorted(a_dict, key=a_dict.get, reverse=True)
    sorted_dict = {}
    for key in sorted_keys:
        sorted_dict[key] = a_dict[key]
    return sorted_dict


def process_file(filename):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding='UTF8')

    strippables = string.punctuation + string.whitespace

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break

        line = line.replace('-', ' ')

        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()

            hist[word] = hist.get(word, 0) + 1

    return hist

def most_common(sorted_dictionary, k_words, excluding_stopwords=False):
    """
    Returns a final list of word:frequency pairs, which may exclude stopwords if specified by the user. The function is also parametrized by a sorted dictionary (sorted_dictionary), and a number of k words (k_words) to keep.

    Parameters
    ----------
    Sorted_dictionary: a sorted dict
    k_words: int
    """
    stopwords = process_file('data/stopwords.txt')
    lst = []
    for word, freq in sorted_dictionary.items():
        if excluding_stopwords:
            if word in stopwords:
                continue
        lst.append((freq, word))
    return lst[0:k_words]

def create_tweet_list(tweets):
    """
    Creates a list of tweets given the Twitter API's response data.
    """
    lst = []
    for tweet in tweets.data:
        lst.append(tweet.text)
    return lst

def analyze_sentiment(listed_tweets):
    """
    This function takes a list of tweets and uses the SentimentIntensityAnalyzer function from nltk to derive sentiment scores for each of the tweets being analyzed. It requires that the user
    specifies tweets in a list format. It then returns the sentiment scores in a list format.

    Parameters
    ----------
    listed_tweets: list
    """
    lst = []
    for line in range(len(listed_tweets)):
        line = listed_tweets[line]
        score = SentimentIntensityAnalyzer().polarity_scores(line)
        for key, value in score.items():
            lst.append((key, value))
    return lst

def get_datetime_utc():
    """
    Derives current datetime as required by the Twitter API, if not specified by a user. The format required is "YYYY-mm-ddTHH:mm:ssz".
    """
    first_time = datetime.now(timezone.utc)
    correct_time = str(first_time - timedelta(0, 60, 0))
    new_time = correct_time.replace(" ", "T")
    split_time = new_time.split(".")[0]
    final_time = split_time + 'z'
    return final_time

def get_default_start_date():
    """
    Derives initial/start date as required by the Twitter API. Given that we only have Elevated access to the API, start date must be within 7 days of the current search. 
    """
    time = datetime.now(timezone.utc)
    start_date = str(time - timedelta(6, 86380, 0))
    new_time = start_date.replace(" ", "T")
    split_time = new_time.split(".")[0]
    final_time = split_time + 'z'
    return final_time

def make_query(usernames, username_operator = 'OR', keyword_operator = 'OR', keywords=None, include_retweet=False, include_reply=False):
    """
    Formats queries to be sent to the Twitter API given its specific format. The only required arguments are the start time, end time and username(s). 

    Parameters
    ----------

    usernames: list | list of strings
    username_operator: bool | AND or OR
    keyword_operator: bool | AND or OR
    keywords: list | list of strings
    include_retweet: bool | True or False
    include_reply: bool | True or False

    example query: from:elonmusk speech -is:retweet -is:reply. This would search for all of Elon Musk's tweets containing the word "speech" in the past 7 days, that are neither retweets nor replies.
    """
    usernames_str = f' {username_operator} from: '.join(usernames)
    if keywords is None:
        initial_query = f'from: {usernames_str}'
    elif keywords is not None:   
        keywords_str = f' {keyword_operator} '.join(keywords)
        initial_query = f'from: {usernames_str} {keywords_str}'
    if include_retweet and include_reply:
        query = initial_query
    if include_retweet is False and include_reply is False:
        query = initial_query + ' -is:retweet' + ' -is:reply'
    elif include_reply is False:
        query = initial_query + ' -is:reply'
    elif include_retweet is False:
        query = initial_query + ' -is:retweet'
    return query

