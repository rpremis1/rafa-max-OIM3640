
from operator import methodcaller
from flask import Flask, render_template, request
from pyparsing import replaceHTMLEntity

from aux_functions import *
from histogram import *
from sentiment import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/find-twitter-tweet/', methods=['GET', 'POST'])
def get_sentiment():
    
    if request.method == 'POST':
        usernames = []
        username1 = (request.form['username1'])
        username2 = (request.form['username2'])
        usernames.append(username1)
        usernames.append(username2)
        
        # print(usernames)
        
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
        
        if reply =='on': 
            reply = True 
        else: 
            reply = False 

        new_query = make_query(usernames, 'OR', 'OR', keywords, retweet, reply)
        

       
        # new_query = make_query(username, 'OR', 'OR', keywords, False, False)
        # new_tweets = new_tweets = client.search_recent_tweets(query=new_query, start_time=start_time, end_time=end_time, tweet_fields=["created_at", "text", "source"],
        #                                                       user_fields=["name", "username", "location", "verified", "description"], max_results=10, expansions='author_id')
        # sentiment_list = analyze_sentiment(create_tweet_list(new_tweets))
        # sentiment_df = pd.DataFrame(sentiment_list, columns=['sentiment', 'value'])
        # aggregated_df = sentiment_df.groupby(['sentiment']).mean().reset_index()
        # if query:
        
        # new_query = make_query(username, 'OR', 'OR', keyword, retweet, reply)

        return render_template('get_sentiment_result.html',
                               usernames=usernames,
                               start_time=start_time,
                               end_time=end_time,
                               keyword=keyword,
                               retweet=retweet,
                               reply=reply,
                               new_query = new_query

                               # query = new_query
                               )

        # print((ggplot(aggregated_df, aes(y='value', x='sentiment', fill='sentiment', color='sentiment'))
        #     + geom_bar(stat='identity')
        #     + theme(legend_position='bottom', legend_title=element_blank())
        #     + scale_y_continuous(minor_breaks=NULL)
        #     + labs(x='', y='', title='Mean Sentiment Value (Y) vs. Sentiment Kind (X) by Sentiment Kind (Colors)', caption=f'Only tweets containing {keywords} by {usernames}')))

    else:
        return render_template('get_sentiment_form.html')


if __name__ == '__main__':
    app.run(debug=True)
