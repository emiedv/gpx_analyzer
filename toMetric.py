# Subfunction "ToMetric"
# # Convert latitue and longitude to meters
# input latitude, longitude
# return latMet, longMet

import pyproj
from math import cos


def transform_lon_lat_old(longitude, latitude):
    # Latitude; 1 degree = 110.574 km
    # Longitude: 1 degree = 111.320*cos(latitude) km
    lon_km = [x * 110574 for x in latitude]
    lon_calc = 111320*cos(min(latitude))
    lat_km = [x * lon_calc for x in longitude]

    return lon_km, lat_km


def transform_lon_lat(longitude, latitude):
    # Define the source and target coordinate systems
    source_crs = pyproj.CRS("EPSG:4326")  # WGS84 GCS
    target_crs = pyproj.CRS("EPSG:3857")  # Web Mercator projection
    # Create a coordinate transformer
    transformer = pyproj.Transformer.from_crs(source_crs, target_crs, always_xy=True)

    counter = 0
    long_met = []
    lat_met = []
    while counter < len(longitude):
        # Convert a latitude-longitude coordinate to Web Mercator
        x, y = transformer.transform(longitude[counter], latitude[counter])
        long_met.append(x)
        lat_met.append(y)

        counter = counter + 1

    return long_met, lat_met
