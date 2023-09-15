import sys
import os

from data import load

def _data():
    root_dir = "./data/images/"
    files =  os.path.join(root_dir)
    File_names = os.listdir(files)

    image_paths = []
    for i in File_names:
        image_paths.append(root_dir + i)

    return image_paths


def confirm():
    confirm_name = [x.split('/')[-1][:-4] for x in load._data()]
    
    return confirm_name

