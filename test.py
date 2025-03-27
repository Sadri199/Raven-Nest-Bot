from dicts import *
from PIL import Image, ImageFont, ImageDraw
import random

objective_list = ["Goku (Mid)", "Shadow the Hedgehog", "Obama"]
objective = random.randrange (0, len(objective_list))
picture_test = objective_list[objective]

organization_list = ["Raven's Nest"]
org = organization_list[0]

requester_list = ["Miles 'Tails' Prower"]
requ = requester_list[0]
#print(picture_test)

def imageChooser(picture):
    if picture in char_dict:
        correct_path = char_dict.get(picture)
        print("Yes")
        print(correct_path)
        return correct_path
    elif picture in org_dict:
        correct_path = org_dict.get(picture)
        print("Yes")
        print(correct_path)
        return correct_path
    elif picture in req_dict:
        correct_path = req_dict.get(picture)
        print("Yes")
        print(correct_path)
        return correct_path
    elif picture in extra_dict:
        correct_path = extra_dict.get(picture)
        print("Yes")
        print(correct_path)
        return correct_path
    elif picture in loc_dict:
        correct_path = loc_dict.get(picture)
        print("Yes")
        print(correct_path)
        return correct_path
    else:
        print("No")
        correct_path = "img/unknown.png"
        print(correct_path)
        return correct_path
                    
give = imageChooser("Kame House")
#test_pic = Image.open(get_pic)
#test_pic.show()

