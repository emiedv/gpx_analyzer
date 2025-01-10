


### Old ###

import xml.etree.ElementTree as ET
from datetime import datetime

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
