import twitterAPIexercise


# Program One, Works well!
try:
    valid_tweetfeed = twitterAPIexercise.get_all_tweets("BU_Tweets")

    # Only calls subsequent functions if media download from twitter feed was successful
    if (valid_tweetfeed):
        twitterAPIexercise.lable_images()
        twitterAPIexercise.make_video()
except Exception as e:
    print(str(e))
else:
    if (valid_tweetfeed):
        print("Done. Program successful")
    else:
        print("ERROR: Unable ro run program for the selected twitter feed.\nPlease try again with another username")


# Program Two, Handles errors well!
try:
    valid_tweetfeed = twitterAPIexercise.get_all_tweets("fjsdalkfj")

    # Only calls subsequent functions if media download from twitter feed was successful
    if (valid_tweetfeed):
        twitterAPIexercise.lable_images()
        twitterAPIexercise.make_video()
except Exception as e:
    print(str(e))
else:
    if (valid_tweetfeed):
        print("Done. Program successful")
    else:
        print("ERROR: Unable ro run program for the selected twitter feed.\nPlease try again with another username")


#Program Three, Breaks when we run another twitter account without manually clearing the images
try:
    valid_tweetfeed = twitterAPIexercise.get_all_tweets("HWSColleges")

    # Only calls subsequent functions if media download from twitter feed was successful
    if (valid_tweetfeed):
        twitterAPIexercise.lable_images()
        twitterAPIexercise.make_video()
except Exception as e:
    print(str(e))
else:
    if (valid_tweetfeed):
        print("Done. Program successful")
    else:
        print("ERROR: Unable ro run program for the selected twitter feed.\nPlease try again with another username")
