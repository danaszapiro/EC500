#!/usr/bin/env python
# encoding: utf-8

import tweepy  # https://github.com/tweepy/tweepy
import wget
import os
import subprocess
import json
import urllib
import requests
import io
import re
import glob
from shutil import copyfile



from google.cloud import vision

from google.cloud.vision import types
from os import listdir
from pickle import FALSE
from symbol import except_clause

# Twitter API credentials
consumer_key = ''
consumer_secret = ''
access_key = ''
access_secret = ''


def get_all_tweets(screen_name):
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
        wget.download(media_file, "./output")

    return True


# Function definition to make video from images using Ffmpeg
def make_video():
    # uses subprocess.call to use the ffmpeg command, also crops images to fit within frame
    try:
        os.chdir(r"C:\Users\antth\PycharmProjects\EC500Project2\output")
        for index, oldfile in enumerate(glob.glob("*.jpg"), start=1):
            newfile = 'image{}.jpg'.format(index)
            os.rename(oldfile, newfile)

        os.chdir(r"C:\Users\antth\PycharmProjects\EC500Project2\output")
        os.system('ffmpeg -y -loglevel panic -framerate 1/3 -i image%d.jpg video.mp4')
        copyfile("C:/Users/antth/PycharmProjects/EC500Project2/output/video.mp4", "C:/Users/antth/PycharmProjects/EC500Project2/static/video.mp4")
        copyfile("C:/Users/antth/PycharmProjects/EC500Project2/output/imagelabels.txt", "C:/Users/antth/PycharmProjects/EC500Project2/static/imagelabels.txt")


    except (RuntimeError, TypeError, NameError):
        print("ERROR: ffmpeg unable to to create video")
        pass
    else:
        print("Video done. Saved as out.mp4")


# Function definition, uses google vision API to lable all images located in output folder
def lable_images():
    # creates google vision API client
    client = vision.ImageAnnotatorClient()

    # creates ouput file to write lables
    file = open("./output/imagelabels.txt", "w")

    # for loop to go through .jpg pictures in output folder
    pictures = [pic for pic in listdir("./output") if pic.endswith('jpg')]
    for picture in pictures:
        file_name = os.path.join(os.path.dirname(__file__), "output", picture)

        # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations

        # writes current image  URL
        file.write('Lables for  ' + picture + ' :\n')
        print('Lables:' + picture)

        for label in labels:
            # writes current image labels
            file.write(label.description + '\n')
            print(label.description)

    file.close()


if __name__ == '__main__':
    # pass in the username of the account you want to download feed from
    try:
        valid_tweetfeed = get_all_tweets("BU_Tweets")

        # Only calls subsequent functions if media download from twitter feed was successful
        if (valid_tweetfeed):
            lable_images()
            make_video()
    except Exception as e:
        print(str(e))
    else:
        if (valid_tweetfeed):
            print("Done. Program successful")
        else:
            print("ERROR: Unable ro run program for the selected twitter feed.\nPlease try again with another username")
