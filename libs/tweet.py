###############################################################################
# Script         : tweet.py
# Description    : Python Class to manage tweets
# Author         : Jaspal Singh (jaspal.singh@carleton.ca)
# Date           : 04/12/2020
# Version        : 1.0
###############################################################################

#######################################
# Import Libraries
#######################################
import random
import json

#######################################
# Class to generate/simulate Live Tweets
#######################################
class Tweet:
    # Define Init Method
    def __init__(self):
        self.inputFile = 'input/covid19.json'
    
    # Method to Load Tweets
    def loadTweets(self):
        with open(self.inputFile) as f:
            data = json.load(f)
            return data
    
    # Method to get Tweet
    def getTweet(self):
        tweets = self.loadTweets()
        index = random.randint(0,99)
        msg = tweets['tweets'][index]['tweet']
        return msg.encode("utf-8")
    
    # Method for White-Box-Testing
    def testTweetMsg(self):
        sentences = ["I am really SCARED of Coronavirus!",
        "Really SAD to see so many Deaths :(",
        "Unfortunately we are running out of Ventilators. This is not good.",
        "Present situation is very scary.",
        "I am hell afraid to go out for shopping.",
        "Social distancing is EXCELLENT option.",
        "Drink lot of Vitamin-C",
        "We are in this together, let's hope for best!",
        "Thanks! Government for Emergency Benefits. Kudos!!!",
        "Three cheers for frontiline workers :)"]
        return sentences