import schedule
import time
from eraser import remove
from image_creator import *

def mrClean ():
    print("Entering first step.\n")
    remove()
    print("First step clear, going to the next step.\n")
        
def makeMeme ():
    print("Entering second step.\n")
    new_mission = Mission()
    print(new_mission.main_merge)
    image_make_1(new_mission)
    image_make_2(new_mission)
    image_make_3(new_mission)
    image_make_4(new_mission)
    print("Second step clear, going to the next step.\n")
    
#Make step 3, call to apis
#Configure the correct hours for this cron to work, i think everything could be done between 18:00 and 18:05      
schedule.every(20).seconds.do(mrClean)
schedule.every(30).seconds.do(makeMeme)

while True:
    schedule.run_pending()
    time.sleep(1)