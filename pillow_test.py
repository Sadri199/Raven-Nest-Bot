from PIL import Image, ImageFont, ImageDraw
from missionCreator import *

newMission = Mission()

im = Image.open("1.png") #open a pic
#im.show() #opens a programa with the pic itself

draw1 = ImageDraw.Draw(im) #Instance to be able to add text
draw2 = ImageDraw.Draw(im) #Instance to be able to add text

# Define the text properties
fontTitle = ImageFont.truetype("Perfect DOS VGA 437 Win.ttf", 26) #The size is in pixels
textTitle = newMission.mainMerge
positionTitle = (120,480)
fontReward = ImageFont.truetype("Perfect DOS VGA 437 Win.ttf", 30) #The size is in pixels
textReward = newMission.reward
positionReward = (699,480)
text_color = (255,202,114) #RGB, so 0,0,0 is Black, 255,255,255 is White.

# Add text to the image
draw1.text(positionTitle, textTitle, font=fontTitle, fill=text_color)
draw2.text(positionReward, textReward, font=fontReward, fill=text_color)

im.save("edited.png") #This saves the pic


print(newMission.mainMerge)
print(im.format,im.size,im.mode)