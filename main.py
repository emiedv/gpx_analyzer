from readgpx import read_gpx
from toMetric import transform_lon_lat, transform_lon_lat_old
from pprint import pprint

# Init, ändra .gpx-fil till indata
longitude, latitude, elevation, time = read_gpx('Hafjell.gpx')
long_met, lat_met = transform_lon_lat(longitude, latitude)
long_km, lat_km = transform_lon_lat_old(longitude, latitude)


