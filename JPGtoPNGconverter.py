import sys
import os
from PIL import Image

# store relative path for new folder:
new_folder_path = './new'

# make program take cmd args:

arg1 = str(sys.argv[1])
arg2 = str(sys.argv[2])

# check if the new folder is existing, else create it:

if not(os.path.exists(new_folder_path)):
    os.mkdir(new_folder_path)

# loop through Pokedex dir, change file names and save to 'new' folder:

png_extension = 'png'

for file in os.listdir('./Pokedex'):
    if file.endswith('.jpg'):
        img = Image.open(os.path.join('./Pokedex/', file))

        png = file.replace('jpg', png_extension)

        os.chdir(new_folder_path)
        jpgImage_converted_to_png = img.save(png, 'png')
        os.chdir('..')

