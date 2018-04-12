# Twitter APIs exrcise using Python

APIs and libraries used:
- tweepy to download user feed and extract media
- wget to download media files
- FFMPEG to convert .jpg files into a .mp4 video
    - implemented using the os and subprocess libraries. 
 - google vision API


## Installation

install the latest version of each one of the APIs
1) Install mongoDB
2) update python to the python3.6 version
3) pip3 install tweepy
4) brew install ffmpeg
5) pip3  install --upgrade google-cloud-vision
6) pip install pymongo
7) To set up the authentication credential for google cloud follow intructions on the following link: https://cloud.google.com/vision/docs/reference/libraries
8) clone git repository

## Usage

1) Replace twitter API credentials with actual tokens in the twitterFeed.py file
2) Run mongod on another tarminal shell to have the mongoDB deamon running on the background
3) The program will scan through the twitterfeed of 20 of the most popular twitter handles and download its media files
4) The GoogleVision API is used to analyze the media
5) All labels and scores from the analysis are stored in the database with the corresponding twitter handle, number of images analyzed and date accessed

###DataBase Format

{
     "handler" : handler,
     "date" : date,
     "labels" : [
                    {
                        "description" : description,
                        "score" : score
                    },
                    { 
                        "description" : description,
                        "score" : score
                    }
                ]
     "imageCount" : imageCount        
}
