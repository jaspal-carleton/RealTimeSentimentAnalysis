###############################################################################
# Script         : sentiment.py
# Description    : Python Class to perform Sentiment Analysis
# Author         : Jaspal Singh (jaspal.singh@carleton.ca)
# Date           : 04/12/2020
# Version        : 1.0
###############################################################################

#######################################
# Import Libraries
#######################################
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#######################################
# Class for Sentiment Analysis
#######################################
class Sentiment:
    # Define Init Method
    def __init__(self):
        self.scores = []
    
    # Method to Calculate Sentiment Score for Live Tweets
    def sentiment_scores(self, sentence):
        
        # Create a SentimentIntensityAnalyzer object.
        sid_obj = SentimentIntensityAnalyzer()

        # polarity_scores method of SentimentIntensityAnalyzer
        # oject gives a sentiment dictionary.
        # which contains pos, neg, neu, and compound scores.
        sentiment_dict = sid_obj.polarity_scores(sentence)
        
        # Negative Sentiment Score
        neg = round(sentiment_dict['neg']*100,2)
        
        # Neutral Sentiment Score
        neu = round(sentiment_dict['neu']*100,2)
        
        # Positive Sentiment Score
        pos = round(sentiment_dict['pos']*100,2)
        
        # Return Scores
        self.scores = [neg, neu, pos]
        return self.scores
    