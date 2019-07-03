# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 10:35:07 2019
This script unzips the Image folder and separtes the train, validation and test images
@author: souma
"""
#%% Import Libraries
import os
import shutil
import pandas as pd
import numpy as np
import zipfile

#%%
os.chdir('D:/Career Development/Analytics Vidhya/Game of Deep learning/Data')
os.getcwd()

#%% Unzip train
path_to_zip_file = os.getcwd() + '/' + str('train_2.zip')
directory_to_extract_to = os.getcwd() + '/' + str('Extracted Images')
zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
zip_ref.extractall(directory_to_extract_to)
zip_ref.close()

#%% Get train and test image labels
# Read train and test labels
test_labels = pd.read_csv(os.getcwd() + '/' + 'test.csv')
train_labels = pd.read_csv(directory_to_extract_to + '/' +  'train.csv')

#%% Transfer the Test Images to a different folder
test_image_labels = test_labels['image']
source_path = directory_to_extract_to + '/' + 'images'
destination_path = os.getcwd() + '/Test images/test'
for image_name in test_image_labels:
    source_file_name = source_path + '/' + str(image_name)
    destination_file_name = destination_path + '/' + str(image_name)
    shutil.move(source_file_name, destination_file_name)

#%% Similarly create the Train Images
train_image_labels = train_labels['image']
source_path = directory_to_extract_to + '/' + 'images'
destination_path = os.getcwd() + '/Train images/train'
for image_name in train_image_labels:
    source_file_name = source_path + '/' + str(image_name)
    destination_file_name = destination_path + '/' + str(image_name)
    shutil.move(source_file_name, destination_file_name)

#%% Also copy the train file as labels.csv
train_labels.to_csv(os.getcwd() + '/Train images/' + 'labels.csv', index = False)
