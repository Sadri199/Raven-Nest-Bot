import schedule
import time
import random
from eraser import remove
from image_creator import *
from twitter_connection import *
from bluesky_connection import *

success_rate = random.randrange(1,99)

def mrClean ():
    print("Initializing jobs!")
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
    
def etGoHome ():
    print("Entering final step.\n")
    process_pic = uploadPics()
    media_ids = list(process_pic)
    makeTweet(media_ids,success_rate)
    print("\nTweet sent to Twitter.")
    time.sleep(1)
    open_now = opener()    
    pic_list = list(open_now)
    giveURL = blueskyPost(pic_list,success_rate)
    print(giveURL)
    print("\nPost sent to Bluesky.")
    print("All steps clear, job is done.\n")
    
    
###################Schedule Version###################
#schedule.every().day.at("02:20:10").do(mrClean)
#schedule.every().day.at("02:20:20").do(makeMeme)
#schedule.every().day.at("02:20:30").do(etGoHome)
#
##Real schedule at 09:00
#schedule.every().day.at("09:00:10").do(mrClean)
#schedule.every().day.at("09:00:20").do(makeMeme)
#schedule.every().day.at("09:00:30").do(etGoHome)
##Real schedule at 12:00
#schedule.every().day.at("12:00:10").do(mrClean)
#schedule.every().day.at("12:00:20").do(makeMeme)
#schedule.every().day.at("12:00:30").do(etGoHome)
##Real schedule at 18:00
#schedule.every().day.at("18:00:10").do(mrClean)
#schedule.every().day.at("18:00:20").do(makeMeme)
#schedule.every().day.at("18:00:30").do(etGoHome)
#
#while True:
#    
#    s = schedule.idle_seconds()
#    minutes = s // 60
#    if s == 0:
#        print("Starting job!")
#        break
#    elif s > 0:
#        print(f"Waiting for next schedule! Next schedule in aproximate {minutes} minutes!")
#        time.sleep(s)
#    schedule.run_pending()
#    
###################Schedule Version#################

###################Batch Version###################

delete = mrClean()
time.sleep(10)
create = makeMeme()
time.sleep(10)
post = etGoHome()

###################Batch Version###################