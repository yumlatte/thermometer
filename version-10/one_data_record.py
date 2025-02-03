# Import useful libraries

from datetime import datetime # Accurate date time 
import serial # Connect to arduino/read values
import csv # Exporting file
import time # Use in sampling
import numpy as np
import math

# Board Setup

arduino_port = "/dev/ttyACM0" # You can check your connections with /dev/tty*
baud = 9600 # Match this to arduino
sensor_data =[] #empty array for storing all the data

# Read Serial Port 
ser = serial.Serial(arduino_port, baud) # Read serial port
print("Connected to Arduino port:", arduino_port)

# Create a New File
fileName = 'analog-data.csv' # Can make this any file name or an user input
file = open(fileName, "a") # append fileName (will create new if no file exists)
print("File Created")


# Sampling 

time_between_samples = math.ceil(float(input('Enter seconds between samples: '))) # seconds (60 is 5 mins)
print(time_between_samples)
steps_input = int(input('Enter length of recording in seconds: '))
sensor_data = [] #store data

# Recording 
def record_data(steps):
    while steps > 0:
        serial_data=ser.readline()  # Read serial port
        decode_serial_data = serial_data.decode('UTF-8')
        clean_data = decode_serial_data[0:][:-2] # sig figs
        data_for_upload = datetime.now(),clean_data.split(" ") # saves the arduino recorded value and current datetime
        sensor_data.append(data_for_upload)
        time.sleep(time_between_samples)
        steps -= 1
        
record_data(steps_input)

# Store the data

with open(fileName, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(sensor_data)
file.close()

print("Data collection complete!")

