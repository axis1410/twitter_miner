# twitter_miner
This script gets tweets from a user and analyses their likes, retweets and sentiment
To use this, first get your tokens and api key at https://www.apps.twitter.com .
This script converts the scraped tweets into elements of a result set, much like a result set when handling databases in Java.
Then it analyses their words for sentiments. For example, negative words such as 'rude', 'mean', etc will give the tweet a negative sentiment and the opposite will give the tweet a positive sentiment and some may leave it at neutral. It is important to know that Re module doesn't understand sarcasm so there is room for error. 
I would also like to conclude that this project was inspired by a YouTube video and I do not own most of the code but I did personalize it as much as I could.
