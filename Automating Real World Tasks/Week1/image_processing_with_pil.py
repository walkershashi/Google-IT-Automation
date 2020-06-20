#!/usr/bin/env python3
import os, glob
from PIL import Image
size = 128, 128
for f in glob.glob(os.getcwd()+"/images/ic_*"):
  im = Image.open(f).convert('RGB')
  print(f)
  print(im.format)
  new_name = os.path.basename(f)
  im.rotate(270).resize((size)).save(os.getcwd() + "/Processed_image/" + new_name, "JPEG")

