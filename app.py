
from operator import methodcaller
from flask import Flask, render_template, request
from matplotlib.pyplot import plot
from pyparsing import replaceHTMLEntity

from aux_functions import *
from histogram import *
from sentiment import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get-sentiment/', methods=['GET', 'POST'])
def get_sentiment():

    if request.method == 'POST':
        usernames = []
        username1 = (request.form['username1'])
        username2 = (request.form['username2'])
        usernames.append(username1)
        usernames.append(username2)

        # start = (request.form['start-date'])
        # start_time = start + 'T00:00:00z'
        start_time = get_default_start_date()
        end = (request.form['end-date'])
        end_time = end+'T00:00:00z'
        keywords = []
        keyword = (request.form['keyword'])
        keywords.append(keyword)
        retweet = request.form.get('retweet')
        reply = request.form.get('reply')

        if retweet == 'on':
            retweet = True
        else:
            retweet = False

        if reply == 'on':
            reply = True
        else:
            reply = False

        new_query = make_query(usernames, 'OR', 'OR', keywords, retweet, reply)

        new_tweets = client.search_recent_tweets(query=new_query, start_time=start_time, end_time=end_time, tweet_fields=["created_at", "text", "source"],
                                                 user_fields=["name", "username", "location", "verified", "description"], max_results=10, expansions='author_id')
        sentiment_list = analyze_sentiment(create_tweet_list(new_tweets))
        sentiment_df = pd.DataFrame(
            sentiment_list, columns=['sentiment', 'value'])
        aggregated_df = sentiment_df.groupby(
            ['sentiment']).mean().reset_index()
        plot = ((ggplot(aggregated_df, aes(y='value', x='sentiment', fill='sentiment', color='sentiment'))
                 + geom_bar(stat='identity')
                 + theme(legend_position='bottom',
                         legend_title=element_blank())
                 + scale_y_continuous(minor_breaks=NULL)
                 + labs(x='', y='', title='Mean Sentiment Value (Y) vs. Sentiment Kind (X) by Sentiment Kind (Colors)', caption=f'Only tweets containing {keywords} by {usernames}')))

        return render_template('get_sentiment_result.html',
                               usernames=usernames,
                               start_time=start_time,
                               end_time=end_time,
                               keyword=keyword,
                               retweet=retweet,
                               reply=reply,
                               new_query=new_query,
                               plot=plot
                               
                               )

    else:
        return render_template('get_sentiment_form.html')


@app.route('/get-twitter-list/', methods=['GET', 'POST'])
def get_tweets():
    if request.method == 'POST':
        usernames = []
        username1 = (request.form['username1'])
        # username2 = (request.form['username2'])
        usernames.append(username1)
        # usernames.append(username2)

        start = (request.form['start-date'])
        start_time = start + 'T00:00:00z'
        end = (request.form['end-date'])
        end_time = end+'T00:00:00z'
        keywords = []
        keyword = (request.form['keyword'])
        keywords.append(keyword)
        retweet = request.form.get('retweet')
        reply = request.form.get('reply')

        if retweet == 'on':
            retweet = True
        else:
            retweet = False

        if reply == 'on':
            reply = True
        else:
            reply = False

        new_query = make_query(usernames, 'OR', 'OR', keywords, retweet, reply)
        new_tweets = client.search_recent_tweets(query=new_query, start_time=start_time, end_time=end_time, tweet_fields=["created_at", "text", "source"],
                                                 user_fields=["name", "username", "location", "verified", "description"], max_results=10, expansions='author_id')

        tweets = []
        for tweet in new_tweets.data:
            single_tweets = tweet.text
            tweets.append(single_tweets)

        return render_template('get_tweets_result.html',
                               tweets=tweets,
                               username1=username1
                               )
    else:
        return render_template('get_tweets_form.html')


@app.route('/get-histogram/', methods=['GET', 'POST'])
def get_histogram():
    if request.method == 'POST':
        usernames = []
        username1 = (request.form['username1'])
        username2 = (request.form['username2'])
        usernames.append(username1)
        usernames.append(username2)

        start = (request.form['start-date'])
        start_time = start + 'T00:00:00z'
        end = (request.form['end-date'])
        end_time = end+'T00:00:00z'
        keywords = []
        keyword = (request.form['keyword'])
        keywords.append(keyword)
        retweet = request.form.get('retweet')
        reply = request.form.get('reply')

        if retweet == 'on':
            retweet = True
        else:
            retweet = False

        if reply == 'on':
            reply = True
        else:
            reply = False

        new_query = make_query(usernames, 'OR', 'OR', keywords, retweet, reply)
        new_tweets = client.search_recent_tweets(query=new_query, start_time=start_time, end_time = end_time, tweet_fields = ["created_at", "text", "source"],
             user_fields = ["name", "username", "location", "verified", "description"], max_results = 10, expansions='author_id')


        most_common_list = most_common(create_sorted_dict(
            create_dict(create_tweet_list(new_tweets))), 5, True)

        df_1 = pd.DataFrame(most_common_list, columns=['frequency', 'word'])

        plot = (ggplot(df_1, aes(y='frequency', x='word', fill='word', color='word'))
                + geom_bar(stat='identity')
                + theme(legend_position='bottom', legend_title=element_blank())
                + scale_y_continuous(minor_breaks=NULL)
                # + facet_grid('~movie_name', scales = 'free_x')
                + labs(x='', y='', title='Frequency of Word (Y) vs. Word Name (X) by Word Name (Colors) and Word Name (Facets)'))

        return render_template('get_histogram_result.html',
                               most_common_list=most_common_list,
                               plot=plot,
                               df_1=df_1,
                               )
    else:
        return render_template('get_histogram_form.html')


if __name__ == '__main__':
    app.run(debug=True)
