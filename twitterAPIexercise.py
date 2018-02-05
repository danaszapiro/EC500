#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import wget
import os
import subprocess
import json
import urllib 
import requests
import io
import re

from google.cloud import vision

from google.cloud.vision import types
from os import listdir

#Twitter API credentials
consumer_key = "consumer_key"
consumer_secret = "consumer_secret"
access_key = "access_key"
access_secret = "access_secret"


def get_all_tweets(screen_name):

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=10)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=20,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 25):
            break
        print "...%s tweets downloaded so far" % (len(alltweets))
       
    #create set to hold only extracted media file on twitter feed
    media_files = set()
    
    #for each tweet check if it contains media files and add them to the media_files set
    for status in alltweets:
        media = status.entities.get('media', [])
        if(len(media) > 0):
            media_files.add(media[0]['media_url'])
            print "...%s" % (media)
    if(len(media_files) == 0):    
        print"...ERROR: No media in tweeter feed !!" 
    else :
        print "...%s media tweets downloaded so far" % (len(media_files))
    
    #Download all media files found
    for media_file in media_files:
        wget.download(media_file, "./output")
     
def make_video():
        #use subprocess.call to make video from images using Ffmpeg
        subprocess.call("cd ./output && ffmpeg -pattern_type glob -framerate 6 -i '*.jpg' -vf 'scale=w=1280:h=720:force_original_aspect_ratio=1,pad=1280:720:(ow-iw)/2:(oh-ih)/2' -vcodec libx264 out.mp4", shell=True)
 
def lable_images(): 
    # google vision API to lable images in output folder
    client = vision.ImageAnnotatorClient()
    file = open("./output/imagelabels.txt","w")
    
    pictures = [pic for pic in listdir("./output") if pic.endswith('jpg')]
    for picture in pictures:
        file_name = os.path.join(os.path.dirname(__file__),"output",picture)

        # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
             content = image_file.read()
       
        image = types.Image(content=content)

        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations
       
        file.write('Lables for  '+i+'  :\n')
        print('Labels:')
        
        for label in labels:
           
           file.write(label.description+'\n')
           print(label.description)
        
    file.close()
     
if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("@twitterUsername")
    make_video()
    lable_images()
