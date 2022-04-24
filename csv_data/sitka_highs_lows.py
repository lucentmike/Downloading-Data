import csv
from datetime import datetime
import matplotlib.pyplot as plt

#get headers of csv
filename = "csv_data/sitka_weather_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

#get high temperatures from csv, and grab and creates date objects
    highs, lows, dates = [], [], []
    for row in reader:
        highs.append(int(row[5]))   
        lows.append(int(row[6]))
        dates.append(datetime.strptime(row[2], '%Y-%m-%d'))


plt.style.use('seaborn')

fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha =0.1)
ax.set_title('Daily High-Low Temperatues, Sitka 2018', fontsize=24)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel('Temeperature (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()