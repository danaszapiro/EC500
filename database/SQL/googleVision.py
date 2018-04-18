import twitterFeed as tw
import makeMovie as movie
import wget
import os
import io
import databaseSQL as db

from google.cloud import vision

from google.cloud.vision import types
from os import listdir

# Function definition, uses google vision API to lable all images located in output folder
def lable_images(handle):
    # creates google vision API client
    client = vision.ImageAnnotatorClient()
    handleId = db.findId(handle)

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

        print('Lables:' + picture)

        for label in labels:
            keyword = str(label.description)
            score = str(label.score)
            db.insertLabels(handleId, keyword, score)

            print(label.description)

    