# Ariel Core engine

# ##################IMPORTS################################
import os
import tensorflow as tf
import tensorboard
import csv
import numpy as np
from tensorflow import keras

import pandas as pd
from sklearn.model_selection import train_test_split

# def fileImport():
# print("Enter file path for the unstructured data.")
# userData = input("")
# print(tf.__version__)

# Reading the CSV
# filenames = ["/home/hunt3r/Desktop/USData1.csv"]
# record_defaults = [[0.0]] * 8
# dataset = tf.data.experimental.CsvDataset(filenames, record_defaults)


dataset_url = ' '
data = pd.read_csv(dataset_url)
print(data.head())

y = data.temp
x = data.drop('temp', axis=1)

X_train, X_test, Y_train, X_test = train_test_split(x, y, test_size=0.2)
print("\nX_train:\n")
print(X_train.head())
print(X_train.shape())

print("\nX_test:\n")
print(X_test.head())
print(X_test.shape)
# #############IF I NEED ANYTHING ELSE, ILL ADD IT#########3

# TO DO:
# BELOW IS THE FILE IMPORT. WE ARE IMPORTING ALL FILES
# IN A FOLDER ====> /PATH/TO/FOLDER/*   <====ALL FILES
