import pickle
import os
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity

from data import load
from model import embedding, model
from tensorflow.keras.preprocessing import image


def similar_output(first_name, second_name):
    if 'feature_extraction.pickle' not in os.listdir():
        a_index = load.confirm().index(first_name)
        b_index = load.confirm().index(second_name)
        image_features = embedding.extract_features(load._data(), model._get_model())
        image1_features = list(image_features.values())[a_index]
        image2_features = list(image_features.values())[b_index]
        similarity = cosine_similarity(image1_features, image2_features)[0][0]
        similarity = str(round((similarity * 100), 2)) + '%'
        print('<<<<< RESULT ON FIGURE >>>>>')
    
        # save feature extract dict
        with open('feature_extraction.pickle','wb') as fs:
            pickle.dump(image_features, fs)

        plt.figure(figsize=(10, 5))
        plt.subplot(121)
        plt.imshow(image.load_img(load._data()[a_index]))
        plt.yticks([])
        plt.xticks([])
        plt.subplot(122)
        plt.imshow(image.load_img(load._data()[b_index])) 
        plt.yticks([])
        plt.xticks([])
        plt.title(f"Similarity Between {first_name} & {second_name} : {similarity}")
        plt.show()

    else:
        # load feature extract dict
        with open('feature_extraction.pickle', 'rb') as fl:
            image_features = pickle.load(fl)

        a_index = load.confirm().index(first_name)
        b_index = load.confirm().index(second_name)
        image1_features = list(image_features.values())[a_index]
        image2_features = list(image_features.values())[b_index]
        similarity = cosine_similarity(image1_features, image2_features)[0][0]
        similarity = str(round((similarity * 100), 2)) + '%'
        print('<<<<< RESULT ON FIGURE >>>>>')
        
        plt.figure(figsize=(10, 5))
        plt.subplot(121)
        plt.imshow(image.load_img(load._data()[a_index]))
        plt.yticks([])
        plt.xticks([])
        plt.subplot(122)
        plt.imshow(image.load_img(load._data()[b_index])) 
        plt.yticks([])
        plt.xticks([])
        plt.title(f"Similarity Between {first_name} & {second_name} : {similarity}")
        plt.show()
        
