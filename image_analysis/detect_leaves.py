from os import listdir, path
from detect_leaf import *

def detect_leaves(folder_path='/mnt/c/strawberries/Strawberry___Healthy'):
    
    # Get all jpg and png files in the folder
    image_names = [f for f in listdir(folder_path) if f.endswith('.jpg') or f.endswith('.png')]

    # Iterate through the image names and run the detect_leaf function on each one
    for image_name in image_names:
        full_image_path = path.join(folder_path, image_name)
        detect_leaf(full_image_path)


