import string
import nltk
# nltk.download('vader_lexicon') # This is needed to run the sentiment analyis
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from datetime import datetime, timezone 

def create_dict(listed_review):
    """
    Returns a dictionary mapping words and their respective frequencies, given a list of reviews.
    """
    res = {}
    for line in range(len(listed_review)):
        line = listed_review[line]
        word = line.split()
        for words in word:
            res[words] = res.get(words, 0) + 1
    return res


def create_sorted_dict(a_dict):
    """
    Returns a dictionary of sorted word:frequency pairs given a dictionary.
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
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist

def most_common(sorted_dictionary, k_words, excluding_stopwords=False):
    """
    Returns a final list of word:frequency pairs, which may exclude stopwords if specified by the user. The function is also parametrized by a sorted_dictionary, and a number of k words (k_words) to keep
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
    lst = []
    for tweet in tweets.data:
        lst.append(tweet.text)
    return lst

def analyze_sentiment(listed_review):
    """
    This function takes a list of reviews and uses the SentimentIntensityAnalyzer function from nltk to derive sentiment scores for each of the reviews being analyzed. It requires that the user
    specifies a review in list format, as done in previous lines of code.
    """
    lst = []
    for line in range(len(listed_review)):
        line = listed_review[line]
        score = SentimentIntensityAnalyzer().polarity_scores(line)
        for key, value in score.items():
            lst.append((key, value))
    return lst

def get_datetime_utc():
    first_time = str(datetime.now(timezone.utc))
    new_time = first_time.replace(" ", "T")
    split_time = new_time.split(".")[0]
    final_time = split_time + 'z'
    return final_time

def make_query(usernames, username_operator, keyword_operator, keywords=None, include_retweet=False, include_reply=False):
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