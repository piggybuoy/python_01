import sys
import os
from PIL import Image

#grab 1st & 2nd args
image_folder = sys.argv[1]
output_folder = sys.argv[2]

#check if new\ exists, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#loop through image_depot fldr
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('Done!!!')

#convert images to png


#save to the new folder 