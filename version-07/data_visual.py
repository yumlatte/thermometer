# Import useful libraries
import pandas as pd 
import numpy as np
from datetime import datetime 
import matplotlib.pyplot as plt

# Import cleaned data for visualization

dataset = pd.read_csv('processed-analog-data.csv')


# Plot using matplotlib
temp_time_chart = plt.figure(figsize=(15,6))
plt.plot(dataset['time'],dataset['Temperature [C]'],ls='-', label='Recorded Data')

plt.title('Temperature Vs. Time')
plt.xlabel('Time of Reading')
plt.ylabel('Temperature [Degrees C]')

plt.ylim(0,30)
plt.xticks(rotation=90)
plt.legend(loc='lower right')

plt.show()
