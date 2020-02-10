import os
import glob
from PIL import Image 

IMG_DIR="original"
OUT_DIR="croppedImages"
# Usage:
# 1.) Put images in an directory called 'original' in the same folder as this python file
# 2.) Start this script


def cropImg(img):
    width, height = img.size
    distance = 15
    left = 0
    top = distance
    right = 0
    bottom = distance 

    croppedImg = img.crop((left, top, width - right, height - bottom)) 
    return croppedImg


# Create output directory if it doesn't exist
if not os.path.isdir(OUT_DIR):
    os.mkdir(OUT_DIR)

# Recursively search for jpg files and create structure for output images
for fname in glob.glob(IMG_DIR+'\**\*.jpg', recursive=True):
    img = Image.open(fname) 
    TMP_DIR = ""
    newString = fname[len(IMG_DIR):]
    x = fname.split("\\")
    for lvl in x:
        if lvl==IMG_DIR or ".jpg" in lvl:
            pass
        else:
            TMP_DIR = TMP_DIR + "\\" + lvl
            #print(OUT_DIR+TMP_DIR)
            if not os.path.isdir(OUT_DIR + TMP_DIR):
                os.mkdir(OUT_DIR + TMP_DIR)
    croppedImg = cropImg(img)
    croppedImg.save(OUT_DIR+newString)

def getInfo(img):
    width, height = img.size
    print("Image width (horizontal axis):", width, "Image length (vertical axis):", height)
