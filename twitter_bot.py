import tweepy
import datetime
import time
import json
import requests
from bs4 import BeautifulSoup

# Load API keys
with open('keys.json', 'r') as file:
    keys = json.loads(file.read())
    
consumer_key = keys['consumer_key']
consumer_secret = keys['consumer_secret']

access_token = keys['access_token']

access_token_secret = keys['access_token_secret']


# Authenticate Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#tweets date and time every minute
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
while True:
    date = datetime.datetime.today()
    month = months[date.month - 1]
    year = date.year
    day = date.day
    minute = str(date.minute)
    if date.minute< 10:
        minute = '0' + minute
    if date.hour > 12:
        hour = date.hour - 12
        x = ' PM'
    else:
        hour = date.hour
        x = ' AM'
    statement = 'It is ' + str(hour) + ':' + str(minute) + x + ' on ' + str(month) + ' ' + str(day) + ', ' + str(year)
    tweet = api.update_status(statement)
    print(tweet.id)
    print(tweet.text)
    print(tweet.created_at)
    time.sleep(60)