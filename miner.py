import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from textblob import TextBlob
import re
import json
import matplotlib.pyplot as plt
import test

consumer_key = 'JdEqoubiop3zuFlFl8UYhVN99'
consumer_secret = 'GviIfoaOv1XvqDY3cWhwrrBuzq3IqnFaO16xKbvXeVs566DJgt'
access_token = '838204806107971589-ufrVlCTnTdVI7ws96HXv2b2tMqgIZhM'
access_secret = 'kOywFT9HtHAqAiNuLqzBkAmdYwwvhW65BQZLscqzABR4p'

count = int(input('How many tweets do you want to mine? '))
num = 0





class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    
    listener = StdOutListener()
    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    
    while num <= count:
        stream = Stream(auth, listener)
        stream.filter(track = ['Donald Trump'])
        num += 1