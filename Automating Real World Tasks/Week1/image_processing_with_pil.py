#!/usr/bin/env python3
import os, glob
from PIL import Image
size = 128, 128
for f in glob.glob(os.getcwd()+"/images/ic_*"):
  im = Image.open(f).convert('RGB')
  print(f) # optional
  print(im.format) # optional
  new_name = os.path.basename(f) # Rename
  # Extract the images from zip file into "images" directory
  # Make sure you have created an empty directory "Processed_image" to store the  result images
  im.rotate(270).resize((size)).save(os.getcwd() + "/Processed_image/" + new_name, "JPEG")

