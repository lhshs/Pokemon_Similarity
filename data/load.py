import sys
import os
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image

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


def show_image(index1, index2):
    plt.figure(figsize=(10, 5))
    plt.subplot(121)
    plt.imshow(image.load_img(load._data()[index1]))
    plt.yticks([])
    plt.xticks([])
    plt.subplot(122)
    plt.imshow(image.load_img(load._data()[index2])) 
    plt.yticks([])
    plt.xticks([])
    plt.show()

