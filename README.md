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
