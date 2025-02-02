import tweepy
import datetime
import random
from keys import *


consumer_key = api_key_v2
consumer_secret = api_secret_v2
access_token = access_token_v1
access_token_secret = access_token_secret_v1


success_rate = random.randrange(1,99)

def uploadPics(): #Media upload is on V1 because i dont pay
    auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret)

    api = tweepy.API(auth) #saves the auth info
    
    print("Preparing pictures to be uploaded.")
    
    filename_1 = str(datetime.date.today()) + "_1st" + ".png"
    filename_2 = str(datetime.date.today()) + "_2nd" + ".png"
    filename_3 = str(datetime.date.today()) + "_3rd" + ".png"
    filename_4 = str(datetime.date.today()) + "_4th" + ".png"
    
    image1 = api.media_upload(filename_1)
    image2 = api.media_upload(filename_2)
    image3 = api.media_upload(filename_3)
    image4 = api.media_upload(filename_4)

    #print(api.verify_credentials().screen_name) #Just for testing
    print("Sending pics to Twitter queue.\n")
    return image1.media_id_string, image2.media_id_string, image3.media_id_string, image4.media_id_string

def makeTweet(media_ids): #The tweet itself is on V2 because i dont pay
    client = tweepy.Client(
        consumer_key=api_key_v2, consumer_secret=api_secret_v2,
        access_token=access_token_v1, access_token_secret=access_token_secret_v1
    ) #Auth with my account.

    response = client.create_tweet(media_ids=media_ids,
        text=f'Success Rate: {success_rate}%\nA new mission is available, Raven. Type "Yes" to accept or ignore it.'
    ) #Grab the auth and pass it with the Tweet itself

    print("Sending tweet.\n")
    print(f"https://twitter.com/user/status/{response.data['id']}")


#########Test#########
#processTweet = makeTweet()
#########Test#########
