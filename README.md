Program to Use @danaszapiro 's API
-----------------------------------
Anthony Pasquariello

app.py
 - This python application uses the API 3 times
 - Once to retrieve tweets from BU_Tweets. This works well!
 - Second time to check how it handles error handling. Works well!
 - Third to try and break it. 
 
 
Code Review
------------

Code review completed. All review issues are under the 'Issues' tab in this repo. Found 7 issues. Some small and some a bit larger. All in all a great API though!
 - Error handling of FFmpeg within python.
 - Manually have to create output folder
 - Running proram multiple times leaves behind old images
 - Saving video try catch block doesn't output ffmpeg errors
 - ffmpeg implementation only works with OSX
 - Performance - Syncronous, must wait until all of the images are computed to output keywords

Website
--------

I built my website using Flask for Python. The home page allows users to enter a Twitter handle and hit the submit button. The submit button runs the program with danaszapiro's API. When it completes it will redirect to the output.html page. This page will play the video that was created and list the descriptor words given by Google's Image recongnition.

Images of Website
------------------

![alt text](https://github.com/danaszapiro/EC500/blob/app/website-images/ec500-1.png)
![alt text](https://github.com/danaszapiro/EC500/blob/app/website-images/ec500-2.png)


Twitter APIs exrcise using Python
------------------------------------

APIs and libraries used:
- tweepy to download user feed and extract media
- wget to download media files
- FFMPEG to convert .jpg files into a .mp4 video
    - implemented using the os and subprocess libraries. 
 - google vision API


Installation
------------
install the latest version of each one of the APIs
1) update python to the python3.6 version
2) pip3 install tweepy
3) brew install ffmpeg
4) pip3  install --upgrade google-cloud-vision
5) To set up the authentication credential for google cloud follow intructions on the following link: https://cloud.google.com/vision/docs/reference/libraries
3) clone git repository

Usage
------------
1) place Twitter username to be scanned in main function
2) Replace twitter API credentials with actual tokens
4) create a folder named "output"
3) run the ./tweetAPIexercise.py file on terminal
4) all pictures will be downloaded into the output folder
6) an output file will be generate containing labels for each one of the images
5) A video file called out.mp4 will be created out of the images
    - The video's length depend on the number of pictures on the twitter feed. 
    - Each images displays for a duration of 10 sec. 
