# Import useful libraries
import pandas as pd 
import numpy as np
from datetime import datetime 
import matplotlib.pyplot as plt

# Import cleaned data for visualization

dataset = pd.read_csv('processed-analog-data.csv')


# Plot
plt.figure(1)
plt.title('Temperature Vs. Time')
plt.xlabel('Time')
plt.ylabel('Temperature [Degrees C]')
plt.ylim(0,30)
plt.xticks([])
plt.plot(dataset['time'],dataset['Temperature [C]'],ls='-', label='Recorded Data')
plt.savefig("plot")
print('Data is plotted!')




