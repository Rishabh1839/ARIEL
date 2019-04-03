
#Ariel Core engine


###################IMPORTS################################
import os
import tensorflow as tf
import tensorboard
import csv
import pandas as pd
#from __future__ import absolute_import, division, print_function
#import numpy as np 
#from tensorflow import kearas

##############IF I NEED ANYTHING ELSE, ILL ADD IT#########3
###########################################################
###########################################################

#TO DO:
#BELOW IS THE FILE IMPORT. WE ARE IMPORTING ALL FILES 
#IN A FOLDER ====> /PATH/TO/FOLDER/*   <====ALL FILES

def fileImport ():

  print("Eneter file path for the unstructured data.")
  userData = input("")
  print(tf.__version__)


  #Reading the CSV
  filenames = ["/tmp/top800.csv"]
  record_defaults = [[0.0]] * 8
  #Import the CSV-encoded training data with pandas for pre-processing.
  #TODO: parse and split up the dataset in this program after importing.
  #To encode the CSV file with only half of the dataset, do the following in a linux shell
  #  $ head -n 800 USDaata1.csv > top800.csv
  #  $ tail -n 800 USDaata1.csv > bottom800.csv
  csvfix = pd.read_csv(filenames)
  dataset = tf.data.experimental.CsvDataset(csvfix, record_defaults)
