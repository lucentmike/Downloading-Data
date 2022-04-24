import csv
from datetime import datetime
import matplotlib.pyplot as plt

#get headers of csv
filename = "csv_data/sitka_weather_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

#get high temperatures from csv, and grab and creates date objects
    highs, dates = [], []
    for row in reader:
        highs.append(int(row[5]))   
        dates.append(datetime.strptime(row[2], '%Y-%m-%d'))



plt.style.use('seaborn')

fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

ax.set_title('Daily High Temperatues, 2018', fontsize=24)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel('Temeperature (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()