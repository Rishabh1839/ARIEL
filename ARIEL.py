# Ariel Core engine

##################IMPORTS################################
import os
import tensorflow as tf
import tensorboard
import csv
import numpy as np
from tensorflow import keras
# using pandas and sklearn for testing and training our data by splitting the data
def csvImport():
  print("ARIEL Start")
  print("DEBUG: Starting User Input")
  csvPath = input("Please supply the path to the CSV: ")

  dataset = tf.contrib.data.make_csv_dataset(csvPath, batch_size=32)
  iter = dataset.make_one_shot_iterator()
  next = iter.get_next()
  print(next)
  
  inputs, labels = next['country'], next['year']

  with tf.Session() as sess:
    sess.run([inputs, labels])
csvImport()

  ########################Creating an Initialiuzable Iterator##################################
  #This will update the data at runtime making tesnorflow come alive.
def iterator(dataset):
    
    x = tf.placeholder(tf.float32, shape=[None,2])
    dataset = tf.data.Dataset.from_sparse_tensor_slices(x)
    
    data = np.random.sample((200, 2))

    with tf.Session() as sess:
      sess.run(iter.initializer, feed_dict={x: data})
      print(sess.run(el))

    #Initializable Iterator to switch between the datasets
    EPOCHS = 10

    x, y = tf.placeholder(tf.flot32, shape=[None,2]),
    tf.placeholder(tf.float32, shape=[None,1])
    dataset = tf.data.Dataset.from_tensor_slices((x, y))

    train_data = (np.random.sample((100,2))), np.random.sample((100,1))
    test_data = (np.array([[1,2]]) np.array([[0]])
    iter = dataset.make_initializable_iterator()
     el = iter.get_next()
iterator()

