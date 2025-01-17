import os
import datetime

filename_1 = str(datetime.date.today()) + "_1st" + ".png"
filename_2 = str(datetime.date.today()) + "_2nd" + ".png"
filename_3 = str(datetime.date.today()) + "_3rd" + ".png"
filename_4 = str(datetime.date.today()) + "_4th" + ".png"

yesterday_1 = str(datetime.date.today() - datetime.timedelta(days=1)) + "_1st" + ".png"
yesterday_2 = str(datetime.date.today() - datetime.timedelta(days=1)) + "_2nd" + ".png"
yesterday_3 = str(datetime.date.today() - datetime.timedelta(days=1)) + "_3rd" + ".png"
yesterday_4 = str(datetime.date.today() - datetime.timedelta(days=1)) + "_4th" + ".png"

file_list = [filename_1, filename_2, filename_3, filename_4]
past_list = [yesterday_1, yesterday_2, yesterday_3, yesterday_4]

def remove():
    
    print("Validating if there are old pictures.\n")
    for f in file_list:
       if os.path.isfile(f):
            os.remove(f)
            print(f"Removing {f}")
    else:
        print(f"There are no files from {datetime.date.today()}.\n")
    
    for i in past_list:
       if os.path.isfile(i):
            os.remove(i)
            print(f"Removing {i}")
    else:
        print(f"There are no files from yesterday.\n")        
       
#cleaner = remove()        