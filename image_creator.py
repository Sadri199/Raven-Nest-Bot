from PIL import Image, ImageFont, ImageDraw
from mission_creator import *
import datetime
import textwrap

#################General Information#################
#new_mission = Mission()
#print(new_mission.main_merge)

def mission_wrapper(text):
    wrapped = textwrap.fill(text, width=32)
    return  wrapped    
#################General Information#################

#################First Template#################
def image_make_1 (new_mission):
    image_1 = Image.open("ac1_templates/first_template.png") #open a pic

    draw_title = ImageDraw.Draw(image_1) #Instance to be able to add Mission Title
    draw_reward = ImageDraw.Draw(image_1) #Instance to be able to add Reward

    # Define the text properties
    font_title = ImageFont.truetype("ac1_templates/Perfect DOS VGA 437 Win.ttf", 35) #The size is in pixels
    text_title = new_mission.main_merge #I should try wrapping the text or making it smaller
    position_title = (116,475)

    font_reward = ImageFont.truetype("ac1_templates/Perfect DOS VGA 437 Win.ttf", 39) #The size is in pixels
    text_reward = new_mission.reward
    position_reward = (678,475)

    text_color_1 = (255,202,114) #RGB, so 0,0,0 is Black, 255,255,255 is White. 255,202,114 is the specific color of that yellowish font.

    # Add text to the image
    draw_title.text(position_title, text_title, font=font_title, fill=text_color_1)
    draw_reward.text(position_reward, text_reward, font=font_reward, fill=text_color_1)

    filename_1 = str(datetime.date.today()) + "_1st" + ".png" #I prefer to use the current date as a filename.
    image_1.save(filename_1) #This saves the pic
    
    print(image_1.format,image_1.size,image_1.mode)
#################First Template#################

#################Second Template#################
def image_make_2(new_mission):

    image_2 = Image.open("ac1_templates/second_template.png")

    draw_req = ImageDraw.Draw(image_2) #Instance to be able to add Requester
    draw_advance = ImageDraw.Draw(image_2) #Instance to be able to add Advance
    draw_success = ImageDraw.Draw(image_2) #Instance to be able to add Upon Success

    font_second =  ImageFont.truetype("ac1_templates/Perfect DOS VGA 437 Win.ttf", 43) #Ideeal font size for everything!

    text_req = new_mission.main_req
    position_req = (372,405)

    text_advance = new_mission.advance
    position_advance = (372,456)

    text_success = new_mission.success
    position_success = (372,504)

    text_color_2 = (186,185,185)

    draw_req.text(position_req, text_req, font=font_second, fill=text_color_2)
    draw_advance.text(position_advance, text_advance, font=font_second, fill=text_color_2)
    draw_success.text(position_success, text_success, font=font_second, fill=text_color_2)

    filename_2 = str(datetime.date.today()) + "_2nd" + ".png" #I prefer to use the current date as a filename.
    image_2.save(filename_2) #This saves the pic
    
    print(image_2.format,image_2.size,image_2.mode)
#################Second Template#################

#################Third Template#################
def image_make_3(new_mission):
    
    image_3 = Image.open("ac1_templates/third_template.png")

    draw_brief = ImageDraw.Draw(image_3) #Instance to be able to add Mission Brief

    font_third =  ImageFont.truetype("ac1_templates/Perfect DOS VGA 437 Win.ttf", 43)

    text_brief = new_mission.mission_text
    wrapped = mission_wrapper(text_brief)
    #wrapped = textwrap.wrap(text_brief)
    position_brief = (50,435)
    text_color_3 = (184,184,184)

    draw_brief.text(position_brief, wrapped, font=font_third, fill=text_color_3, anchor="ls") #(image_width, image_height)
    #draw_brief.multiline_text(position_brief, wrapped, font=font_third, fill=text_color_3)

    filename_3 = str(datetime.date.today()) + "_3rd" + ".png" #I prefer to use the current date as a filename.
    image_3.save(filename_3)
    
    print(image_3.format,image_3.size,image_3.mode)
#################Third Template#################

def image_make_4(new_mission):
    
    image_4 = Image.open("ac1_templates/fourth_template.png")

    draw_final_loc = ImageDraw.Draw(image_4)
    draw_final_ext = ImageDraw.Draw(image_4)
    draw_cond_success = ImageDraw.Draw(image_4)

    font_final =  ImageFont.truetype("ac1_templates/Perfect DOS VGA 437 Win.ttf", 42)
    
    text_location = new_mission.main_loc
    position_location = (161,456) #?
    text_color_final = (167,167,167)
    text_color_alt_final = (168,17,2)
    extra_color = text_color_final

    text_extras = new_mission.extra_enemies
    if text_extras == "Unknown":
        extra_color = text_color_alt_final
    else:
        extra_color = text_color_final 
        
    position_extras = (350,504)
    
    text_cond_success = new_mission.condition 
    position_cond_success = (161,604)
    
    draw_final_loc.text(position_location, text_location, font=font_final, fill=text_color_final)
    draw_final_ext.text(position_extras, text_extras, font=font_final, fill=extra_color)
    draw_cond_success.text(position_cond_success, text_cond_success, font=font_final, fill=text_color_final)
    
    filename_4 = str(datetime.date.today()) + "_4th" + ".png" #I prefer to use the current date as a filename.
    image_4.save(filename_4)
    
    print(image_4.format,image_4.size,image_4.mode)
#################Test#################
#new_mission = Mission()

#image_make_1(new_mission)
#image_make_2(new_mission)
#image_make_3(new_mission)
#image_make_4(new_mission)
#################Test#################