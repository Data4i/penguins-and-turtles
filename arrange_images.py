import cv2 as cv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import json

def get_labels(direc = 'train'):
    with open(f'data/{direc}_annotations') as img_desc:
        labels = json.load(img_desc)

    label = list()
    for x in labels:
        label.append(x['category_id'])
    label = np.array(label)
    return label

train_labels = get_labels()
test_labels = get_labels(direc = 'valid')

