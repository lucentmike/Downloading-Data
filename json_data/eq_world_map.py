import json
from pprint import pprint
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'json_data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

#filter out dictonarys for each earthqule and the magnitudes
all_eq_dicts = all_eq_data['features']
mags, lats, longs = [], [], []

#sort through the earthquake dictonaries and pull the magnitues, lats and longs
for eq in all_eq_dicts:
    mags.append(eq['properties']['mag'])
    lats.append(eq['geometry']['coordinates'][1])
    longs.append(eq['geometry']['coordinates'][0])

data = [{
    'type': 'scattergeo', 
    'lon': longs, 
    'lat': lats
}]

my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'global_earthquakes.html')