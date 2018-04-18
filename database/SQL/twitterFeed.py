#!/usr/bin/env python
# encoding: utf-8

import tweepy  # https://github.com/tweepy/tweepy
import wget
from pymongo import MongoClient

from google.cloud import vision
from google.cloud.vision import types


# Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

def get_all_tweets(screen_name, output):
    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # verifys credentials
    valid_credentials = api.verify_credentials()
    if (valid_credentials == False):
        print
        "Incorrect credentials"
        return False

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for 10 most recent tweets
    # throws exception and breaks program
    try:
        new_tweets = api.user_timeline(screen_name=screen_name, count=10)
    except tweepy.TweepError as e:
        print('ERROR: could not download tweeter feed. \nException description:')
        print(e)
        return False

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=20, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if (len(alltweets) > 25):
            break
        print
        "...%s tweets downloaded so far" % (len(alltweets))

    # create set to hold only extracted media file on twitter feed
    media_files = set()

    # for each tweet check if it contains media files and add them to the media_files set
    for status in alltweets:
        try:
            media = status.entities.get('media', [])
            if (len(media) > 0):
                media_files.add(media[0]['media_url'])
            print
            "...%s" % (media)
        except:
            print
            "ERROR: No media in tweeter feed !!"
            return False

        else:
            print
            "...%s media tweets downloaded so far" % (len(media_files))

    # Download all media files found
    for media_file in media_files:
        wget.download(media_file, output)

    return len(media_files)