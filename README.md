Twitter APIs exrcise using Python
------------------------------------

APIs and libraries used:
- tweepy to download user feed and extract media
- wget to download media files
- FFMPEG to convert .jpg files into a .mp4 video
    - implemented using the os and subprocess libraries. 


Installation
------------
install the latest version of each one of the APIs
1) use pip install tweepy
2) brew install ffmpeg
3) clone git repository

Usage
------------
1) place Twitter username to be scanned in main function
2) replace twitter API credentials with actual tokens
3) run the ./tweetAPIexercise.py file on terminal
4) all pictures will be downloaded into the folder (If no media files an error message will show in terminal)
5) A video file called out.mp4 will be created out of the images
    - The video's length depend on the number of pictures on the twitter feed. 
    - Each images displays for a duration of 10 sec. 
