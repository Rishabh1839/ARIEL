# Ariel Core engine

# ##################IMPORTS################################
import os
import tensorflow as tf
import tensorboard
import csv
import numpy as np
from tensorflow import keras
# using pandas and sklearn for testing and training our data by splitting the data
import pandas as pd
# splits data into 2 parts
from sklearn.model_selection import train_test_split

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = dir_path + "training.csv"

features = tf.placeholder(tf.int32, shape=[3], name='features')
country = tf.placeholder(tf.string, name='country')
indicator = tf.placeholder(tf.string, name='indicator')
total = tf.reduce_sum(features, name='total')

printerop = tf.print(total, [country, features, indicator, total], name='printerop')

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    with open(filename) as inf:
        # skip the header
        next(inf)
        for line in inf:
            # reading our data using python into our features
            country_name, indicator_name = line.strip(), line.split(", ")
            total = sess.run(printerop, feed_dict={features: [country, indicator], country: country_name})
            print(country_name, indicator_name)


def create_file_reader(filename_queue):
    reader = tf.TextLineReader(skip_header_line=1)
    _, csv_row = reader.read(filename_queue)
    record_defaults = [[""], [""], [0], [0], [0], [0]]
    country_name, country_code, indicator_name = tf.decode_csv(csv_row, record_defaults=record_defaults)
    features = tf.pack([country_name, country_code, indicator_name])
    return features, country


filename_queue = tf.train.string_input_producer(filename, num_epocs=1, shuffle=False)
example, country, = create_file_reader(filename_queue)

with tf.Session() as sess:
    tf.global_variables_initializer().run()
    coordinate = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coordinate=coordinate)
    while True:
        try:
            example_data, country_name = sess.run([example, country])
            print(example_data, country_name)
        except tf.errors.OutOfRangeError:
            break

# def fileImport():
# print("Enter file path for the unstructured data.")
# userData = input("")
# print(tf.__version__)

# Reading the CSV
# filenames = ["/home/hunt3r/Desktop/USData1.csv"]
# record_defaults = [[0.0]] * 8
# dataset = tf.data.experimental.CsvDataset(filenames, record_defaults)


# dataset_url = ' '
# data = pd.read_csv(dataset_url)
# print(data.head())

# dataset_url = ' '
# data = pd.read_csv('training.csv')
# print(data.head())


# y = data.temp
# x = data.drop('temp', axis=1)

# X_train, X_test, Y_train, X_test = train_test_split(x, y, test_size=0.2)
# print("\nX_train:\n")
# print(X_train.head())
# print(X_train.shape())

# print("\nX_test:\n")
# print(X_test.head())
# print(X_test.shape)
# #############IF I NEED ANYTHING ELSE, ILL ADD IT#########3

# TO DO:
# BELOW IS THE FILE IMPORT. WE ARE IMPORTING ALL FILES
# IN A FOLDER ====> /PATH/TO/FOLDER/*   <====ALL FILES
