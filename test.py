###############################################################################
# Script         : test.py
# Description    : Testing Script for the Web-App
# Author         : Jaspal Singh (jaspal.singh@carleton.ca)
# Date           : 04/12/2020
# Version        : 1.0
###############################################################################

#######################################
# Import Libraries
#######################################
import libs.tweet as twt
import libs.sentiment as sa

#######################################
# Class for Test Cases
#######################################
class Testing:
    # Define Init Method
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.aborted = 0
        self.scores = []
    
    # Print Test Summary
    def printSummary(self):
        total = self.passed + self.failed + self.aborted
        print("\n")
        print("-"*60)
        print("{:15s}{:15s}{:15s}{:15s}".format("Total Test", "Pass", "Fail", "Abort"))
        print("-"*60)
        print("{:15s}{:15s}{:15s}{:15s}".format(str(total), str(self.passed), str(self.failed), str(self.aborted)))
    
    # Print Formatted Sentiment Output
    def printSentimentScores(self):
        print("-"*100)
        print("{:66s}{:12s}{:12s}{:12s}".format("Tweet", "Positive %", "Negative %", "Neutral %"))
        print("-"*100)
        for item in self.scores:
            msg = (item['tweet'][:60]+'...') if len(item['tweet'])>60 else item['tweet']
            pos = str(item['pos'])
            neg = str(item['neg'])
            neu = str(item['neu'])
            print("{:66s}{:12s}{:12s}{:12s}".format(msg, pos, neg, neu))
        
    # Execute Test Cases
    def runTestCases(self):
        tweet_obj = twt.Tweet()
        sentiment_obj = sa.Sentiment()
        tweets = tweet_obj.testTweetMsg()
        for tweet in tweets:
            score = sentiment_obj.sentiment_scores(tweet)
            self.scores.append({'tweet':tweet, 'pos': score[2], 'neg': score[0], 'neu':score[1]})
            self.passed += 1
        

#######################################
# Main
#######################################
if __name__ == '__main__':
    # Create test object
    test_obj = Testing()
    # Run the test cases
    test_obj.runTestCases()
    # Print the test results
    test_obj.printSentimentScores()
    test_obj.printSummary()
    print("\n\n")

#######################################
# End of Script
#######################################