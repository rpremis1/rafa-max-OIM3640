
from operator import methodcaller
from types import NoneType
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

    try: 

        if request.method == 'POST':
            usernames = []
            username1 = (request.form['username1'])
            username2 = (request.form['username2'])
          
           

            usernames.append(username1)
            usernames.append(username2)
            

            start_time = get_default_start_date()
            end_time = get_datetime_utc()
            keywords = []
            keyword = (request.form['keyword'])
            if keyword is None:
                keywords = None
            else:
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
                    + labs(x='', y='', title='Mean Sentiment Value (Y) vs. Sentiment Kind (X) by Sentiment Kind (Colors)')))

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
    except: 
        return render_template('oops.html')

@app.route('/get-twitter-list/', methods=['GET', 'POST'])
def get_tweets():
    try: 
        if request.method == 'POST':
            usernames = []
            username1 = (request.form['username1'])
            usernames.append(username1)
         
            start_time = get_default_start_date()
            end_time = get_datetime_utc()
            keywords = []
            keyword = (request.form['keyword'])
            if keyword is None:
                keywords = None
            else:
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

            max_result = (request.form['result'])
            if max_result == '':
                max_result = 100
            else:
                max_result = int(request.form['result'])

          
            new_query = make_query(usernames, 'OR', 'OR', keywords, retweet, reply)
            new_tweets = client.search_recent_tweets(query=new_query, start_time=start_time, end_time=end_time, tweet_fields=["created_at", "text", "source"],
                                                    user_fields=["name", "username", "location", "verified", "description"], max_results= 100, expansions='author_id')

            if type(new_tweets.data) == NoneType:
                return render_template('oops.html')
            else:
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
    except: 
        return render_template('oops.html')


@app.route('/get-histogram/', methods=['GET', 'POST'])
def get_histogram():
    try: 

        if request.method == 'POST':
            usernames = []
            username1 = (request.form['username1'])
            username2 = (request.form['username2'])
           
            usernames.append(username1)
            usernames.append(username2)
           
            start_time = get_default_start_date()
        
            end_time = get_datetime_utc()
            keywords = []
            keyword = (request.form['keyword'])
            if keyword is None:
                keywords = None
            else:
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
                                                    user_fields=["name", "username", "location", "verified", "description"], max_results= 10, expansions='author_id')

            most_common_list = most_common(create_sorted_dict(
                create_dict(create_tweet_list(new_tweets))), 5, True)

            df_1 = pd.DataFrame(most_common_list, columns=['frequency', 'word'])

            plot = (ggplot(df_1, aes(y='frequency', x='word', fill='word', color='word'))
                    + geom_bar(stat='identity')
                    + theme(legend_position='bottom', legend_title=element_blank())
                    + scale_y_continuous(minor_breaks=NULL)
                    + labs(x='', y='', title='Frequency of Word (Y) vs. Word Name (X) by Word Name (Colors) and Word Name (Facets)'))

            return render_template('get_histogram_result.html',
                                most_common_list=most_common_list,
                                plot=plot,
                                df_1=df_1,
                                )
        else:
            return render_template('get_histogram_form.html')
    except: 
        return render_template('oops.html')


if __name__ == '__main__':
    app.run(debug=True)
