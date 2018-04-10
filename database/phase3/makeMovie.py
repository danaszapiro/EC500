#!/usr/bin/env python
# encoding: utf-8

import subprocess
from os import listdir

# Function definition to make video from images using Ffmpeg
def make_video():
        #uses subprocess.call to use the ffmpeg command, also crops images to fit within frame
        try:
            subprocess.call("cd ./output && ffmpeg -pattern_type glob -framerate 1/2 -i '*.jpg' -vf 'scale=w=1280:h=720:force_original_aspect_ratio=1,pad=1280:720:(ow-iw)/2:(oh-ih)/2' -vcodec libx264 video.mp4", shell=True)
        except (RuntimeError, TypeError,NameError):
            print ("ERROR: ffmpeg unable to to create video")
            pass
        else: 
            print("Video done. Saved as video.mp4")
