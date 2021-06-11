from gps import *
import geocoder
from math import radians, cos, sin, asin, sqrt
from tkinter import messagebox


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r


def gps():

    try:
        g = geocoder.ip('me')
####################################################################
############### Use Case GPS not WORKING############################
        # raise CouldnResolveIP

####################Correcting Accuracy##############################
        longitude = g.latlng[0] + 0.010
        latitude = g.latlng[1] + 0.0060

    except CouldnResolveIP:
        error = "Your Location Doesn't Found. Check your GPS!"
        messagebox.showerror("error", error)

    # print(g)
    # print(g.latlng)
    # print(longitude)
    # print(latitude)

    # measured center of PAPA 38.289153, 21.789814 with radius 0.73km
    center_point = [{'lat': 38.289153, 'lng': 21.789814}]
    radius = 0.73  # in kilometer

    test_point = [{'lat': longitude, 'lng': latitude}]

    lat1 = center_point[0]['lat']
    lon1 = center_point[0]['lng']
    lat2 = test_point[0]['lat']
    lon2 = test_point[0]['lng']

    distance = haversine(lon1, lat1, lon2, lat2)

    print('Distance (km) : ', distance)
    if distance <= radius:
        print('Inside the area of University of Patras')

    else:
        print('Outside the area of University of Patras')
        latitude, longitude = None, None

    return latitude, longitude,distance


class CouldnResolveIP(Exception):
    pass
