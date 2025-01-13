from PIL import Image, ImageFont, ImageDraw
from mission_creator import *
import datetime
import textwrap

#################General Information#################
new_mission = Mission()

print(new_mission.main_merge)

def mission_wrapper(text):
    wrapped = textwrap.fill(text, width=32)
    return  wrapped    
#################General Information#################

#################First Template#################
def image_make_1 ():
    image_1 = Image.open("templates/first_template.png") #open a pic

    draw_title = ImageDraw.Draw(image_1) #Instance to be able to add Mission Title
    draw_reward = ImageDraw.Draw(image_1) #Instance to be able to add Reward

    # Define the text properties
    font_title = ImageFont.truetype("Perfect DOS VGA 437 Win.ttf", 36) #The size is in pixels
    text_title = new_mission.main_merge #I should try wrapping the text or making it smaller
    position_title = (120,475)

    font_reward = ImageFont.truetype("Perfect DOS VGA 437 Win.ttf", 40) #The size is in pixels
    text_reward = new_mission.reward
    position_reward = (670,475)

    text_color_1 = (255,202,114) #RGB, so 0,0,0 is Black, 255,255,255 is White. 255,202,114 is the specific color of that yellowish font.

    # Add text to the image
    draw_title.text(position_title, text_title, font=font_title, fill=text_color_1)
    draw_reward.text(position_reward, text_reward, font=font_reward, fill=text_color_1)

    filename_1 = str(datetime.date.today()) + "_first" + ".png" #I prefer to use the current date as a filename.
    image_1.save(filename_1) #This saves the pic
    
    print(image_1.format,image_1.size,image_1.mode)
#################First Template#################

#################Second Template#################
def image_make_2():

    image_2 = Image.open("templates/second_template.png")

    draw_req = ImageDraw.Draw(image_2) #Instance to be able to add Requester
    draw_advance = ImageDraw.Draw(image_2) #Instance to be able to add Advance
    draw_success = ImageDraw.Draw(image_2) #Instance to be able to add Upon Success

    font_second =  ImageFont.truetype("Perfect DOS VGA 437 Win.ttf", 43) #Ideeal font size for everything!

    text_req = new_mission.main_req
    position_req = (378,405)

    text_advance = new_mission.advance
    position_advance = (378,456)

    text_success = new_mission.success
    position_success = (378,504)

    text_color_2 = (186,185,185)

    draw_req.text(position_req, text_req, font=font_second, fill=text_color_2)
    draw_advance.text(position_advance, text_advance, font=font_second, fill=text_color_2)
    draw_success.text(position_success, text_success, font=font_second, fill=text_color_2)

    filename_2 = str(datetime.date.today()) + "_second" + ".png" #I prefer to use the current date as a filename.
    image_2.save(filename_2) #This saves the pic
    
    print(image_2.format,image_2.size,image_2.mode)
#################Second Template#################

#################Third Template#################
def image_make_3():
    
    image_3 = Image.open("templates/third_template.png")

    draw_brief = ImageDraw.Draw(image_3) #Instance to be able to add Mission Brief

    font_third =  ImageFont.truetype("Perfect DOS VGA 437 Win.ttf", 43)

    text_brief = new_mission.mission_text
    wrapped = mission_wrapper(text_brief)
    #wrapped = textwrap.wrap(text_brief)
    position_brief = (50,435)
    text_color_3 = (184,184,184)

    draw_brief.text(position_brief, wrapped, font=font_third, fill=text_color_3, anchor="ls") #(image_width, image_height)
    #draw_brief.multiline_text(position_brief, wrapped, font=font_third, fill=text_color_3)

    filename_3 = str(datetime.date.today()) + "_third" + ".png" #I prefer to use the current date as a filename.
    image_3.save(filename_3)
    
    print(image_3.format,image_3.size,image_3.mode)
#################Third Template#################

#Configure fourth template!

#################Test#################
meme_1 = image_make_1()
meme_2 = image_make_2()
meme_3 = image_make_3()

#################Test#################