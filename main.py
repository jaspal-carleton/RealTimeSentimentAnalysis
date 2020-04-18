###############################################################################
# Script         : main.py
# Description    : Python Flask App for Real Time Sentiment Analysis
# Author         : Jaspal Singh (jaspal.singh@carleton.ca)
# Date           : 04/12/2020
# Version        : 1.0
###############################################################################

#######################################
# Import Libraries
#######################################
from flask import Flask, jsonify, render_template, make_response
import json
from time import time
import libs.tweet as twt
import libs.sentiment as sa

#######################################
# Define Python-Flask Web-App Object
#######################################
app = Flask(__name__)

#######################################
# Web-App Home Path
#######################################
@app.route('/')
def main():
    return render_template('index.html', data='test')

#######################################
# Web-App Live Streaming Path
#######################################
@app.route('/live-stream')
def live_stream():
    # Get current timestamp
    t = time() * 1000
    
    # Fetch a Live Tweet
    tweet_obj = twt.Tweet()
    tweet = tweet_obj.getTweet()
    
    # Calculate Sentiment Score for Live Tweet
    sentiment_obj = sa.Sentiment()
    scores = sentiment_obj.sentiment_scores(tweet)
    
    # Prepare Data Structure Result to be displayed as sentiment scores on the web-app
    data = [[t, scores[0]], [t, scores[1]], [t, scores[2]], [t, tweet]]
    
    # Do HTTP Post to Web-Client of Sentiment Scores as JSON
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

#######################################
# Main: Run Web-App on localhost @ Port# 8000
#######################################
if __name__ == '__main__':
    # Launch the flask web-app
    app.run(host='localhost', port=8000, debug=True)

#######################################
# End of Script
#######################################