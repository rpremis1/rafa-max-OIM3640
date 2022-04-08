# Project Proposal

## The Big Idea

The primary idea of this project is to use Twitter’s API in order to allow a user to search for words (or set of words) by a specific individual/username, during a specified period of time. Alas, the minimum viable product of this project is a website that, given a user-prompted set of words, username, and period of time, returns the tweets by that username that contains the words wanted. For instance, imagine a user wants to search for all tweets by Elon Musk (@elonmusk) containing the word “Dogecoin” between January 2021 and December 2021. It is important to mention that a user must know the Twitter username of the individual it wants to search for – an additional search for a Twitter username given a person’s name would be too time consuming. 
This minimum viable product would explore both the proper usage of an API, as well as the manipulation of the text data using the material learned in class (e.g. accessing a dictionary’s keys to retrieve the text data desired). Additionally, a stretch goal would include both the generation of descriptive analytics, such as the frequency of most used words in tweets containing the user’s set of words, number of tweets containing that word per week, etc., as well as NLP techniques to show how the sentiment of that author has changed over time.
Assuming the successful completion of both the minimum and stretch goals, the learning purpose of this project is fourfold: (1) further our understanding of the usage and data retrieval from APIs, (2) comprehend how to manipulate data with Pandas and generate visualizations using libraries like Matplotlib and Plotnine, (3) better understand how NLP libraries such as NLTK and the estimation of sentiment scores work, and (4) create web apps that allow the users to dynamically input what they want to search for by using Flask, HTML, CSS, and Heroku.

## Learning Goals

### Individual Goals - Rafa

(1) Further understand data retrieval from API, as well as its limitations (e.g. Twitter’s API has a cap on the maximum number of searches one can conduct in a day).

(2) Better comprehend the differences in data manipulation between R’s Tidyverse/dplyr and Pandas, as well as GGPlot2 vs. Matplotlib/Plotnine.

(3) Understand the estimation procedure of sentiment scores.

### Individual Goals - Max

(1) Build a great Flask WebApp by combining knowledge from my WebTech class with the learnings from the Problem Solving & Software Design Class. 

(2) Learn more about the integration of Flask and Heroku.

### Shared Goals

Understand how to use Pandas and visualization libraries such as Matplotlib and Plotnine.

## Implementation Plan

As it relates to the retrieval of data, we must first understand the format for which Twitter’s API returns data, as well as how to conduct GET requests for it. We have already gotten developed API keys and will be looking into the documentation this week. Assuming the successful completion of this part, we will have a list of tweets/sentences the user seeks, for which we will begin our data manipulation and analysis. Before using Pandas, we will create histogram functions to return a dictionary of word:frequency pairs of the most commonly used words (excluding stopwords). Then, we will use Pandas to count the average number of words grouped by week, as well as ungrouped (hence calculating the total number of commonly used words used in the period). Finally, we will estimate sentiment scores by using the NLTK packages, which will be applied over every sentence/tweet we have gathered.
As it pertains to the creation of the website, we will use the Flask Framework, HTML and CSS. Furthermore and with the use of Heroku, we will be able to host our website and make it accessible for external usage. 

## Project Schedule

Week 1: Get data using web scraping, Twitter API. Understand limitations of API and request additional extensions. (Possibly) create basic functions.
As we create functions, start working on a first Flask application and figure out how to integrate flask in heroku.
Week 2: use Pandas, Plotnine, Matplotlib, and NLTK to create our visualizations. Use our first results and integrate them in our flask application.
Week 3: Learn more about the different ways we could display our results and try them out – for instance, will we display the top 5 tweets returned, ordered by date, and a dropdown button to see more tweets? Or will we simply return all tweets at once?  
Week 4: 
Finalize our displaying and integration process with Flask and Heroku and have a WebApp that can be reached without the need of running the code in Python. 

## Collaboration Plan

Based on our knowledge in certain topics and areas, we came up with splitting the tasks like follows: Rafa is focusing more on getting the data we need, manipulating it and returning the results we want and Max is focusing on building our WebApp using flask and Heroku. We are choosing this particular structure because we feel very confident to achieve the best results for this project in the most efficient way. We also plan on having regular meetings where we discuss our progress and difficulties we might come across and ask for help in case one of us is stuck. Another advantage of this is that we can both work on the project in an asynchronous way and as we both have very different time slots available to actually work on the project, hence, this feels like the right solution. 

## Risks

As it pertains to data retrieval, it seems like the biggest risk is our lack of understanding of the API. For instance, we may have to request approval from Twitter to be able to gather more data in a fast manner. For the part of building a WebApp, the biggest risk is that we can’t manage to integrate Flask in Heroku, can’t visualize our result in the way we want to visualize them on our WebPage and can’t come up with a solution where a user can input a search word, user name and time frame and be given the expected output. 

## Additional Course Content

Further understanding of NLP techniques would certainly help in this project. Alternatively, covering Pandas and other data manipulation techniques/packages would also help.
More (code) examples of Flask or other frameworks that can be used in order to build a web application. Further explanation about Heroku and its implementation/integration with Flask.

