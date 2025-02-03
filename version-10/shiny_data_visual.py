# Import useful libraries
import pandas as pd 
import numpy as np
from datetime import datetime 
import matplotlib.pyplot as plt
from shiny.express import render, ui, input
from shiny import reactive

# Import cleaned data for visualization

dataset = pd.read_csv('processed-analog-data.csv')



with ui.card(full_screen=True):
    ui.card_header("Figure")
    @render.plot
    def plot():
        import matplotlib.pyplot as plt
        plt.title('Temperature Vs. Time')
        plt.xlabel('Time')
        plt.ylabel('Temperature [Degrees C]')
        plt.ylim(0,30)
        plt.xticks([])
        return plt.plot(dataset['time'],dataset['Temperature [C]'],ls='-', label='Recorded Data')

with ui.card(full_screen=True):

        ui.input_action_button("action_button", "Action")  

        @render.text()
        @reactive.event(input.action_button)
        def counter():
            return f"{input.action_button()}"
    
with ui.card(full_screen=True):
        ui.card_header("DataFrame")
        @render.data_frame
        def table():
            return render.DataTable(dataset)


# Plot using matplotlib
#temp_time_chart = plt.figure(figsize=(15,6))


