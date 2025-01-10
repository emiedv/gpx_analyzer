# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
from datetime import datetime
# import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
from math import cos, asin, sqrt, pi
from numpy.lib.stride_tricks import sliding_window_view

def read_gpx(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    # Namespace
    ns = {'gpx': 'http://www.topografix.com/GPX/1/1'}

    # Initialize lists to store data
    latitude = []
    longitude = []
    elevation = []
    time = []

    # Iterate through each track point
    for trkpt in root.findall('.//gpx:trkpt', ns):
        lat = float(trkpt.attrib['lat'])
        lon = float(trkpt.attrib['lon'])
        ele = float(trkpt.find('gpx:ele', ns).text)
        elev = float("{:.2f}".format(ele)) # round elevation to 2 decimal places
        time_str = trkpt.find('gpx:time', ns).text
        time.append(datetime.fromisoformat(time_str[:-1])) # remove 'Z' from end of string
        # time.append(datetime.strptime(time_actual.isoformat(), "%Y-%m-%dT%H:%M:%S.%f"))
        # time.append(dt.dt.fromisoformat.total_seconds(time_str[:-1]))

        latitude.append(lat)
        longitude.append(lon)
        elevation.append(elev)

    return latitude, longitude, elevation, time

# Init, ändra .gpx-fil till indata
latitude, longitude, elevation, time = read_gpx('Hafjell.gpx')


# Omvandlar värden från long/lat till meter-koordinater med 0 som lägasta värde
# Latitude; 1 degree = 110.574 km
# Longitude: 1 degree = 111.320*cos(latitude) km
latkm = [x * 110574 for x in latitude]
loncalc = 111320*cos(min(latitude))
lonkm = [x * loncalc for x in longitude]
latkmnorm = [x - min(latkm) for x in latkm]
lonkmnorm = [x - min(lonkm) for x in lonkm]



# Beräknar delta på alla koordinater, fixar array-längd med en initial nolla
dele = np.diff(elevation)
dele = np.concatenate([[0],dele])

dlat = np.diff(latkm)
dlat = np.concatenate([[0],dlat])

dlon = np.diff(lonkm)
dlon = np.concatenate([[0],dlon])

# Beräknar total vektor för rörelsen
dsum = np.sqrt(dele*dele + dlat*dlat + dlon*dlon)

# Beräknar delta för tid + beräknar hastighet. Lägger 1:a istället för 0:a för att slippa div0
dtim_raw = np.diff(time)
dtim = []
for dt in dtim_raw:
    dtim.append(dt.total_seconds())
dtim = np.concatenate([[1],dtim])
speed = 3.6*dsum/dtim

#Filtrerar hastighet
nwin = 2
fspeed = np.average(sliding_window_view(speed, window_shape = nwin), axis=1)
i = 1;
while i < nwin:
    fspeed = np.concatenate([[0],fspeed])
    i += 1

#Filtrerar elevation
nwin = 64
felev = np.average(sliding_window_view(elevation, window_shape = nwin), axis=1)
j = 1;
while j < nwin:
    felev = np.concatenate([[0],felev])
    j += 1

#Funktion som letar upp och returnerar segment som håller samma lutning
# def merge_pieces(pieces):
#     merged_pieces = []
#     if not pieces:
#         return merged_pieces
    
#     current_piece = [pieces[0][0]]
#     for i in range(len(pieces) - 1):
#         if pieces[i][1] == pieces[i+1][0]:
#             current_piece.append(pieces[i+1][1])
#         else:
#             merged_pieces.append(current_piece)
#             current_piece = [pieces[i+1][0]]
#     merged_pieces.append(current_piece)
    
#     return merged_pieces

# def split_graph(graph):
#     positive_pieces = []
#     negative_pieces = []
    
#     for i in range(len(graph) - 1):
#         slope = graph[i+1] - graph[i]
#         if slope > 0:
#             positive_pieces.append(graph[i:i+2])
#         elif slope < 0:
#             negative_pieces.append(graph[i:i+2])
    
#     return merge_pieces(positive_pieces), merge_pieces(negative_pieces)
#     return positive_pieces, negative_pieces

# positive_pieces, negative_pieces = split_graph(felev)

#Funktion som letar upp och returnerar segment som håller samma lutning + kopplar till tidsstämplar
def merge_pieces(pieces, time_piec):
    merged_pieces = []
    if not pieces:
        return merged_pieces
    
    current_piece = [pieces[0][0]]
    for i in range(len(pieces) - 1):
        if pieces[i][1] == pieces[i+1][0]:
            current_piece.append(pieces[i+1][1])
        else:
            merged_pieces.append(current_piece)
            current_piece = [pieces[i+1][0]]
    merged_pieces.append(current_piece)
    
    return merged_pieces

def split_graph(graph, time):
    positive_pieces = []
    negative_pieces = []
    pos_piec_time = []
    neg_piec_time = []
    
    for i in range(len(graph) - 1):
        slope = graph[i+1] - graph[i]
        if slope > 0:
            positive_pieces.append(graph[i:i+2])
            pos_piec_time.append(time[i:i+2])
        elif slope < 0:
            negative_pieces.append(graph[i:i+2])
            neg_piec_time.append(time[i:i+2])
    
    return merge_pieces(positive_pieces, pos_piec_time), merge_pieces(negative_pieces, neg_piece_time)

positive_pieces, negative_pieces = split_graph(felev, time)

# Plottar data
figure = plt.figure()
ax = figure.add_subplot(221, projection='3d')
ax.plot(lonkmnorm, latkmnorm, elevation)
plt.title('3D Full track')
plt.grid(True)
plt.subplot(222)
plt.plot(time, elevation)
plt.plot(time, felev)
plt.grid(True)
plt.title('Elevation vs time')
plt.subplot(223)
plt.plot(time, speed)
plt.plot(time, fspeed)
plt.grid(True)
plt.title('Speed vs time')
plt.subplot(224)
plt.plot(time, negative_pieces)
plt.grid(True)
plt.title('Filtered speed vs time')
plt.suptitle('Full track')
plt.show()
