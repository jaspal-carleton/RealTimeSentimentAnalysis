## Real-Time Sentiment Analysis ##
## A Python based tool to perform Real Time Sentiment Analysis using the Lexicon method ##

### Disclaimer

This software simulates live streaming data and does not fetch real time data from the internet. However, a live streaming component can be easily integrated by replacing the input coming from .json file. Lastly, the Sentiment Analysis module present in the software is fully functional and provides real results.

### Author

Jaspal Singh: jaspal.singh@carleton.ca

### Acknowledgement

I would like to express my sincere gratitude to the course Professor Dr. Emma Farago for her immense knowledge and support throughout the course.

### Organization

Department of Systems and Computer Engineering,
Carleton University, Ottawa, ON , CANADA

### Pre-Requisites to run the software

Python Anaconda Framework (https://www.anaconda.com)

### Installation instruction of dependencies

Step 1: Download the project as ZIP file or otherwise do a git clone of the project.

Step 2: Do a change directory to the project folder. If downloaded, first Unzip the downloaded file and then do change directory.

Step 3: Execute the following pip/pip3 command from the command line interface (cli) or command terminal.
```
pip install -r requirements.txt

or

pip3 install -r requirements.txt
```

### Instructions to run the software

Step 1 : Start/execute the main python script from the command terminal or cli.
```
$ python main.py
```

Step 2 : Open any web-browser and navigate to the following URL.
```
http://localhost:8000
```

Step 3: To stop/quit the main python script, just press CTRL-C from your keyboard.

### Folder Structure of the repository

```
RealTimeSentimentAnalysis/
├── LICENSE
├── README.md
├── input
│   ├── __init__.py
│   └── covid19.json
├── libs
│   ├── __init__.py
│   ├── sentiment.py
│   └── tweet.py
├── main.py
├── requirements.txt
├── static
│   ├── js
│   │   └── histogram.js
│   └── logo.gif
├── templates
│   ├── index.html
│   └── live-stream.html
└── test.py
```

### Input

The simulation of live streaming of tweets is done using input.json file.

```
./input/input.json
```

### Output

The program displays live output and does not generate output file. Navigate to the following URL when main program is running.

```
http://localhost:8000
```

### Testing of Software

To test the software, execute the following test python script from the command terminal or cli.

```
$ python test.py
```

### Live Stream Simulator

In order to simulate the live streaming data (in this case the Live Tweets), the tweets were manually captured and copied into the JSON file in the following format.

```
{
    "tweets": [
        {
            "time": "1587069929",
            "tweet": "Wow! My wife, a healthcare worker, ordered scrubs from @MarksCanada and they included this lovely note."
        },
        {
            "time": "1587069930",
            "tweet": "I know people are scared that giving Doug Ford too much credit during #Covid19Ontario could lead to his reelection. But on a more optimistic note - maybe he'll enjoy people not thinking he's a dick so much, he'll do the decent thing more often even when this is over? #onpoli"
        }
    ]
}

```
Next, the live data loading API uses the random library to randomly pick one of the tweet from the input JSON file. This randomly picked tweet is then fed to the Sentiment Analysis module for further processing. Finally, the Sentiment Scores of the tweet are shown as histogram in the web browser to end user.

### References and Credits:

The author would like to thank and give credits to the original authors/owners/developers/team of VADER, HighCharts and Bootstrap.

1. VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text
(by C.J. Hutto and Eric Gilbert)
Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
```
https://github.com/cjhutto/vaderSentiment
```

2. HighCharts:
```
https://www.highcharts.com
https://github.com/highcharts/highcharts/tree/master
```

3. Bootstrap:
```
https://getbootstrap.com
```