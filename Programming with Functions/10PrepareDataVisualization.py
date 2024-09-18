import pandas as pd
import matplotlib.pyplot as pyplot

#read datafram from a csv file
water_df = pd.read_csv('water.csv')

#this will grab all the rows in the meterNumber column with the M4103 meter
myMeter = water_df[ water_df['meterNumber'] == 'M4103']

#plot the data points as a bar graph and uses readDate column as x
# axis and usage column as y axis
myMeter.plot(kind='bar', x='readDate', y='usage')
myMeter.plot(kind='area', x='readDate', y='usage')

#shows the graph on screen
pyplot.show()