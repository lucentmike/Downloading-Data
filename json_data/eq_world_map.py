import json
from pprint import pprint
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'json_data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

#filter out dictonarys for each earthqule and the magnitudes
all_eq_dicts = all_eq_data['features']
mags, lats, longs, hover_texts = [], [], [], []

#sort through the earthquake dictonaries and pull the magnitues, lats and longs
for eq in all_eq_dicts:
    mags.append(eq['properties']['mag'])
    lats.append(eq['geometry']['coordinates'][1])
    longs.append(eq['geometry']['coordinates'][0])
    hover_texts.append(eq['properties']['title'])

#defines data sets, scatter map, the lats and longs, hover text. Marker makes the plots bigger for each mag, and sets a color gradiant
data = [{
    'type': 'scattergeo', 
    'lon': longs, 
    'lat': lats,
    'text': hover_texts,
    'marker' : {
        'size' : [5*mag for mag in mags],
        'color' : mags,
        'colorscale': 'Jet',
        'reversescale': False,
        'colorbar' : {'title': 'Magnitude'},
    },
}]

#creates a layout
my_layout = Layout(title='Global Earthquakes')

#creates a figure with the layout and data parameters. then plots
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'global_earthquakes.html')