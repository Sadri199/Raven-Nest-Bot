from PIL import Image
import os

main_directory = 'img/convert/'

for filename in os.listdir(main_directory):
    if filename.endswith(".jpg"):
        prefix = filename.split(".jpg")[0]
        im = Image.open(main_directory+filename)
        im.save('img/convert/'+prefix+'.png')
        erase = 'img/convert/'+prefix+'.jpg'
        os.remove(erase)
    elif filename.endswith(".webp"):
        prefix = filename.split(".webp")[0]
        im = Image.open(main_directory+filename)
        im.save('img/convert/'+prefix+'.png')
        erase = 'img/convert/'+prefix+'.webp'
        os.remove(erase)
    elif filename.endswith(".jpeg"):
        prefix = filename.split(".jpeg")[0]
        im = Image.open(main_directory+filename)
        im.save('img/convert/'+prefix+'.png')
        erase = 'img/convert/'+prefix+'.jpeg'
        os.remove(erase)
    else:
        print(f"Ending {filename} conversion.")
        continue


png_directory = 'img/convert/png/'

for filename in os.listdir(main_directory):
    if filename.endswith(".png"):
        prefix = filename.split(".png")[0]
        im = Image.open(main_directory+filename)
        new_size = im.resize(size=(260,284))
        new_size.save(png_directory+prefix+'.png')
        erase = 'img/convert/'+prefix+'.png'
        os.remove(erase)
    else:
        print(f"Ending {filename} resize.")
        continue    
    