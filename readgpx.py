# Subfunction "ReadGPX"
# # Imports gpx file from Maprika and populates arrays:
# input file.gpx
# return latitude,longitude, elevation, time

import xml.etree.ElementTree as ET
from datetime import datetime


def read_gpx(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    # Namespace
    ns = {'gpx': 'http://www.topografix.com/GPX/1/1'}

    # Initialize lists to store data
    longitude = []
    latitude = []
    elevation = []
    time = []

    # Iterate through each track point
    for trkpt in root.findall('.//gpx:trkpt', ns):
        lon = float(trkpt.attrib['lon'])
        lat = float(trkpt.attrib['lat'])
        ele = float(trkpt.find('gpx:ele', ns).text)
        elev = float("{:.2f}".format(ele)) # round elevation to 2 decimal places
        time_str = trkpt.find('gpx:time', ns).text
        time.append(datetime.fromisoformat(time_str[:-1])) # remove 'Z' from end of string
        # time.append(datetime.strptime(time_actual.isoformat(), "%Y-%m-%dT%H:%M:%S.%f"))
        # time.append(dt.dt.fromisoformat.total_seconds(time_str[:-1]))

        longitude.append(lon)
        latitude.append(lat)
        elevation.append(elev)

    return longitude, latitude , elevation, time
