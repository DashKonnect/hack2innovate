import os
from PIL import Image, ImageOps
size=60,60

path = "copy"
for file in os.listdir(path):
    f = open(path+"/"+file, 'rb+')
    image_data = Image.open(f)
    image_data = ImageOps.mirror(image_data)
    # image_data =	image_data.rotate()
    image_data.save(path+"/"+file,"JPEG")
  