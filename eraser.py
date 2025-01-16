import os
import datetime

filename_1 = str(datetime.date.today()) + "_1st" + ".png"
filename_2 = str(datetime.date.today()) + "_2nd" + ".png"
filename_3 = str(datetime.date.today()) + "_3rd" + ".png"
filename_4 = str(datetime.date.today()) + "_4th" + ".png"

file_list = [filename_1, filename_2, filename_3, filename_4]

def remove():
    
    for f in file_list:
       if os.path.isfile(f):
            os.remove(f)
            print(f"Removing {f}")
    else:
        print("All files deleted or they don't exist.")
       
#cleaner = remove()        