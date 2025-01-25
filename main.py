import schedule
import time
from eraser import remove
from image_creator import *
from twitter_connection import *
from bluesky_connection import *


def mrClean ():
    print("Entering first step.\n")
    remove()
    print("First step clear, going to the next step.\n")
        
def makeMeme ():
    print("Entering second step.\n")
    new_mission = Mission()
    print(f"New mission created: {new_mission.main_merge}")
    image_make_1(new_mission)
    image_make_2(new_mission)
    image_make_3(new_mission)
    image_make_4(new_mission)
    print("Images created correctly.")
    print("Second step clear, going to the next step.\n")
    
#Make step 3, call to apis
def etGoHome ():
    print("Entering final step.\n")
    process_pic = uploadPics()
    media_ids = list(process_pic)
    makeTweet(media_ids)
    print("\nTweet sent to Twitter.")
    time.sleep(1)
    open_now = opener()    
    pic_list = list(open_now)
    giveURL = blueskyPost(pic_list)
    print(giveURL)
    print("\nPost sent to Bluesky.")
    print("All steps clear, job is done.\n")
    
    
#Schedule for testing
schedule.every().day.at("18:45:10").do(mrClean)
schedule.every().day.at("18:45:20").do(makeMeme)
schedule.every().day.at("18:45:30").do(etGoHome)
#Real schedule at 18:00
schedule.every().day.at("18:00:10").do(mrClean)
schedule.every().day.at("18:00:20").do(makeMeme)
schedule.every().day.at("18:00:30").do(etGoHome)

while True:
    schedule.run_pending()
    time.sleep(1)