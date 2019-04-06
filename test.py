import numpy as np
import pandas as pd
import pickle as pkl
import quandl, math, datetime
from sklearn import preprocessing
from sklearn.svm.libsvm import cross_validation
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as data_plot
from matplotlib import style

# using style
style.use('ggplot')

quandl.api_config.ApiConfig.api_key = 'h-FrEDCiZnh5cKM3Cuva'
# getting random data from the api's
data = quandl.get('WIKI/GOOGL')
# writing
writeFile = open("ARIELDataWrite.txt", "w")
writeFile.write(str(data))
writeFile.close()
print(type(data))
# condenses the information
data = data[['Adj. Open', 'Adj. High percent', 'Adj. Low Percent', 'Adj. Close', 'Adj.Volume']]
# creating new variable which is the high low percent
data['High Low Percent'] = (data['Adj. High'] - data['Adj. Close']) / data['Adj. Close'] * 100.0
# creating new variable which is the Percentage Change
data['Percent Change'] = (data['Adj. Close'] - data['Adj. Open']) / data['Adj. Open'] * 100.0

data = data[['Adj. Close', 'High Low Percent', 'Percent Change', 'Adj. Volume']]
