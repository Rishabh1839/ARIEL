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
print(data)
# condenses the information
data = data[['Adj. Open', 'Adj. High percent', 'Adj. Low Percent', 'Adj. Close', 'Adj.Volume']]
# creating new variable which is the high low percent
data['High Low Percent'] = (data['Adj. High'] - data['Adj. Close']) / data['Adj. Close'] * 100.0
# creating new variable which is the Percentage Change
data['Percent Change'] = (data['Adj. Close'] - data['Adj. Open']) / data['Adj. Open'] * 100.0

data = data[['Adj. Close', 'High Low Percent', 'Percent Change', 'Adj. Volume']]

# forecasting out dataset
forecastData = 'Adk. Close'
data.fillna(-99999, inplace=True)
# comment if necessary
# print(len(data))

forecastOut = int(math.ceil(0.02*len(data)))

data['Label'] = data[forecastData].shift(-forecastOut)
# print(data)

x = np.array(data.drop(['Label'], 1))
x = preprocessing.scale(x)
xLately = x[-forecastOut: ]
x = x[:-forecastOut]
data.dropna(inplace = True)
y = np.array(data['Label'])

trainX, testX, trainY, testY = cross_validation.train_test_split(x, y, test_size=0.2)

frameControl = LinearRegression(n_jobs=-1)

frameControl.fit(trainX, trainY)
with open('linearregression.pickle', 'wb') as a:
    pkl.dump(frameControl, a)

inPickle = open('linearregression.pickle', 'rb')
frameControl = pkl.load(inPickle)

accuracy = frameControl.score(testX, testY) * 100.0

setForecast = frameControl.predict(xLately)

data['Forecasting the Data'] = np.nan
last_date = data.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in setForecast:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    data.loc[next_date] = [np.nan for _ in range(len(data.columns) - 1)] + [i]

# plot the data for visualization
data['Adj. Close'].plot()
data['Forecasting'].plot()
data_plot.legend(loc=4)
data_plot.title('Stock Prediction for Tesla')
data_plot.xlabel('Date')
data_plot.ylabel('price')
data_plot.show()
print(accuracy)


writeFile = open("ARIELDataWriteModifiedData.txt", "w")
writeFile.write(str(data))
writeFile.close()
print(data)

