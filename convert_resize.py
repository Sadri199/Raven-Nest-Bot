from PIL import Image
import os

main_directory = 'img/convert/'

for filename in os.listdir(main_directory):
    if filename.endswith(".jpg"):
        prefix = filename.split(".jpg")[0]
        im = Image.open(main_directory+filename)
        im.save('img/convert/'+prefix+'.png')
    elif filename.endswith(".webp"):
        prefix = filename.split(".webp")[0]
        im = Image.open(main_directory+filename)
        im.save('img/convert/'+prefix+'.png')    
    else:
        continue


png_directory = 'img/convert/'

for filename in os.listdir(png_directory):
    if filename.endswith(".png"):
        prefix = filename.split(".png")[0]
        im = Image.open(png_directory+filename)
        new_size = im.resize(size=(260,284))
        new_size.save('img/convert/png/'+prefix+'.png')
    else:
        continue    
    