import pandas as pd
import datetime
import time


clean_dataset = pd.read_csv('processed-analog-data.csv')

html = clean_dataset.to_html()

# write html to file
text_file = open("data.html", "w")
text_file.write("<html>\n<head>\n<title> Data </title>\n<link rel='stylesheet' href='style.css'>\n</head> <body>\n<nav>\n<a href= 'main.html'>Main</a></nav> \n</body></html>")
text_file.write(html)
text_file.close()
print('Data Page Read')
