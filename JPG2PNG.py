import sys
import os
from PIL import Image

image_folder = sys.argv[1]
new_folder = sys.argv[1]

#print(image_folder,output_folder)
#print(os.path.exists(output_folder))

if not os.path.exists(new_folder):
     os.makedirs(new_folder)

for filename in os.listdir(image_folder):
     img = Image.open(f'{image_folder}{filename}')
     clean_name = os.path.splitext(filename)[0]
    
     img.save(f'{new_folder}{filename}.png', 'png')
     print('all done!')



