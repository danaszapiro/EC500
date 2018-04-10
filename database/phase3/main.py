'''
Created on Apr 10, 2018

@author: danasz
'''
import twitterFeed as tw
import makeMovie as movie
import mongoDatabase as db
import cleanup as cl
import googleVision as ggl

import wget
import os
import shutil
import datetime
from pymongo import MongoClient

from google.cloud import vision

from google.cloud.vision import types

#outputfolder name
output = "./output"
imageLabels = []

def main():   

    twitterHandles = ["katyperry", "justinbieber", "barackobama",
                  "rihanna", "taylorswift13", "ladygaga",
                  "YouTube", "Cristiano", "realdonaldtrump",
                  "JeffBezos", "WIRED", "nytimes","FoxNews",
                  "CNN", "jimmyfallon", "Oprah", "BillGates",
                  "instagram", "NASA", "TheEconomist", "NatGeo"]
    
    for handle in twitterHandles:
        imageLabels[:] = []

        #make/clean output file
        if os.path.exists(output):
            shutil.rmtree(output)
        if not os.path.exists(output):
            os.mkdir(output)
    
            # pass in the username of the account you want to download feed from
        try:
            #download media from twitterFeed
            imageCount = tw.get_all_tweets(handle, output)
            # Only calls subsequent functions if media download from twitter feed was successful
            if (imageCount > 0):
                imageLabels.append(ggl.lable_images())
                movie.make_video()
                db.insertMongo(handle, datetime.datetime.now(), imageLabels, imageCount)
            else:
                print("ERROR: Unable ro run program for the selected twitter feed.\nPlease try again with another username")
        except Exception as e:
            print(str(e))
        else:
            print("Done. Program successful")
            
if __name__ == '__main__':
    main()