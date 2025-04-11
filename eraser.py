import os

current_folder = "./"

def remove():
    
    print("Validating if there are old pictures to erase.\n")
    for filename in os.listdir(current_folder):
        if filename.endswith(".png") == True:
            file_erase = current_folder+filename
            os.remove(file_erase)
            print(f"Erasing {filename} !")
    
    print("There are no more old pictures!")        

#execute = remove()