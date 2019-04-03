
#Ariel Core engine


###################IMPORTS################################
import os
import tensorflow as tf
import tensorboard
import csv
from __future__ import absolute_import, division, print_function
import numpy as np 
from tensorflow import kearas

##############IF I NEED ANYTHING ELSE, ILL ADD IT#########3
###########################################################
###########################################################

#TO DO:
#BELOW IS THE FILE IMPORT. WE ARE IMPORTING ALL FILES 
#IN A FOLDER ====> /PATH/TO/FOLDER/*   <====ALL FILES

def main():
  fileImport()
  learn_fn()
  trainTest()
main()

def fileImport ():

  print("Eneter file path for the unstructured data.")
  userData = input("")
  print(tf.__version__)


  #Reading the CSV
  filenames = ["/home/hunt3r/Desktop/USData1.csv"]
  record_defaults = [[0.0]] * 8
  dataset = tf.data.experimental.CsvDataset(filenames, record_defaults)

  

def learn_fn(dataset):
  incomeLevel = tf.feature_column.numeric_column("year")
    
    #defining the estimators
    #Estimators are how
    # 
    # tensorflow will look at the detail. The eyes
  ##return incomeLevel
    ###########Training##############################
  wordIndex(incomeLevel)
  dataset = tf.data.Dataset.from_sparse_tensor_slices((dict(incomeLevel))



trainData = keras.preprocessing.sequence.pad_sequnces(trainData, value=wordIndex["year"], padding='post', maxlen=256)
testData = kearas.preprocessing.sequence.pad_sequences(testData, value=wrodIndex["year"], paddin='post', maxlen=256)
len(trainData[0]) , len(testData[0])
print(trainData[0])


  #return trainedData.shuffle(1000).repeat()
  print(dataset[0])