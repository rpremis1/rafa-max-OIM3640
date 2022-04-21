usernames = ['elonmusk', 'pmarca']
keywords = ['Doge', 'Twitter']


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

print(make_query(usernames, 'OR', 'OR', keywords, include_retweet=True, include_reply=True))


