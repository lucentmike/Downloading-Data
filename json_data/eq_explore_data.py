import json
from pprint import pprint

#open json file and LOAD it into python usable format
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

pprint(mags[:5])
pprint(lats[:5])
pprint(longs[:5])