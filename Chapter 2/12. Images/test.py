import os
from PIL import Image
import numpy as np
import pandas as pd


def img_to_csv():
    parent_dir = "Data"
    data = pd.DataFrame()
    for folder in os.listdir(parent_dir):

        print(folder)
        
        if folder == "train":
            for f in os.listdir(parent_dir+"/"+folder):

                class_data = np.zeros(  ( len(os.listdir(parent_dir+"/"+folder+"/"+f) ), 785) )
                print(class_data.shape)

                for i, img_name in enumerate(os.listdir(parent_dir+"/"+folder+"/"+f)):

                    img = Image.open(parent_dir+"/"+folder+"/"+f+"/"+img_name)
                    img_arr = np.array(img, dtype=int)
                    img_arr = img_arr.flatten()
                    class_data[i,:784] = img_arr
                    class_data[i,784] = int(f)

                class_data = pd.DataFrame(class_data)
                data = pd.concat([data, class_data])
                print(data.shape)


data = pd.read_csv("mnist.csv")

x = data.values[:784]
y = data.values[784]
