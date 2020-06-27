
#!/usr/bin/env python3

from PIL import Image
import os, glob

SIZE = 600, 400
EXT = "jpeg"

for file in glob.glob(os.getcwd() + "/supplier-data/images/0*"):
    print(file)
    img = Image.open(file).convert('RGB')
    name = os.path.basename(file)
    print(name)
    img.resize((SIZE)).save(os.getcwd() + "/supplier-data/images/" + name[:-4] + EXT)

