"""
Module: geoutils
Author: siralmat
Contents:
    Stub methods to retrieve route data and calculate distance between sets of
    coordinates.
"""

import math

def retrieveRouteData(filename="sampleroutes.txt"):
    """Retrieve dummy route data from file."""
    with open(filename, "r") as f:
        return f.read()

def calcMetresDistance(lat1, long1, lat2, long2):
    """Calculate the distance between two sets of coordinates (badly)"""
    return (abs(lat1 - lat2) + abs(long1 - long2)) * 100
    # no, like, really badly

