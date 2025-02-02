import datetime
import random
from atproto import Client
from keys import *

user = username_blue
secret = password_blue

filename_1 = str(datetime.date.today()) + "_1st" + ".png"
filename_2 = str(datetime.date.today()) + "_2nd" + ".png"
filename_3 = str(datetime.date.today()) + "_3rd" + ".png"
filename_4 = str(datetime.date.today()) + "_4th" + ".png"

success_rate = random.randrange(1,99)

def opener():
    
    with open (filename_1,"rb") as image_1:
        img_data_1 = image_1.read()
        
    with open (filename_2,"rb") as image_2:
        img_data_2 = image_2.read()
        
    with open (filename_3,"rb") as image_3:
        img_data_3 = image_3.read()
        
    with open (filename_4,"rb") as image_4:
        img_data_4 = image_4.read()
    
    return img_data_1, img_data_2, img_data_3, img_data_4
        
client = Client()

def blueskyPost(pic_list):
    print("Preparing upload to Bluesky.")
    client.login(user,secret)

    new_post = client.send_images(text=f'Success Rate: {success_rate}%\nA new mission is available, Raven. Type "Yes" to accept or ignore it.', images=pic_list)
    raw_url = new_post.uri
    splitted = raw_url.split("/")
    url = "https://bsky.app/profile/ravennestboard.bsky.social/post/" + splitted[-1] #If everything works fine, here i can see the URI of the post.
    
    print("Sending post to Bluesky.\n")
    return url

#create_post = blueskyPost()
#print(create_post)
