import string

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
