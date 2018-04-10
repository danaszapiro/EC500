#!/usr/bin/env python
# encoding: utf-8

from pymongo import MongoClient

# function to connect to Mongodb initialize and update database
def InitializeMongo():
    client = MongoClient('localhost:27017')
    db = client.TwitterFeed
    
def updateMongo(query, field, value):
    client = MongoClient('localhost:27017')
    db = client.TwitterFeed
    updateValue = {field:value}
    db.TwitterFeeds.update_one(query, updateValue)
       
def insertMongo(handler, date, data, imageCount):
    client = MongoClient('localhost:27017')
    db = client.TwitterFeed
    post = {"handler" : handler,
            "date" : date,
            "labels" : data,
            "imageCount" : imageCount        
    }
    db.TwitterFeed.insert_one(post)
    