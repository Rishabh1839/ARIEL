#SingularityIndustries
#Rishab Singh
#Amari Matthews
#AIEL import, read, and classify

# To Do:
# Test Data Import
# Test CSV read colums


#Goal:
# Import Data!
## Ensure that the data has been properly imported.
# Read Data!
##Ensure that the data runs through the full application.
# Return values!
##Tuning values returned by tensorflow.
# Plot on Tensorboard
##Plot data on Tensorboard and online.
import csv
import tensorflow as tf
import os

def engineCore():

  print("Eneter filepath for 2 CSV's.")
  print("")
  csvFile1 = input("File Path1 : ")
  print("")
  csvFile2 = input("File Path")

  #Open Both CSV
  Col1 = "ColumnName1"
  Col2 = "ColumnName2"
  Col3 = "ColumnName3"
  mydictionary = {Col1: [], Col2: [], Col3: []}

  csv.reader(open(csvFile1, "rb"))
  csv.reader(open(csvFile2, "rb"))
  for row in csvFile:
    mydictionary[Col1].append(row[0])
    mydictionary[Col2].append(row[1])
    mydictionary[Col3].append(row[2])


  filename_queue = tf.train.string_input_producer([csvFile1, csvFile2])

  reader = tf.TextLineReader()
  key, value = reader.read(filename_queue)

  # Default values, in case of empty columns. Also specifies the type of the
  # decoded result.
  record_defaults = [[1], [1], [1], [1], [1]]
  col1, col2, col3, col4, col5 = tf.decode_csv(
    value, record_defaults=record_defaults)
  features = tf.stack([col1, col2, col3, col4])

  with tf.Session() as sess:
    # Start populating the filename queue.
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)

    for i in range(1200):
      # Retrieve a single instance:
      example, label = sess.run([features, col5])

    coord.request_stop()
    coord.join(threads)
engineCore()

