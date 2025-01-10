Subfunction "ToMetric"
# Convert latitue and longitude to meters
input latitude, longitude
return latMet, longMet


#### Old ###
# Latitude; 1 degree = 110.574 km
# Longitude: 1 degree = 111.320*cos(latitude) km
latkm = [x * 110574 for x in latitude]
loncalc = 111320*cos(min(latitude))
lonkm = [x * loncalc for x in longitude]
