"""
Module: gpslocator
Author: siralmat
"""
import random
import time
import threading

class GpsLocator(object):
    """Test implementation of GpsLocator.
    Creates a fake GPS connection in a new thread and calls locationReceived()
    with preset coordinates at a regular interval.

    Assignment spec:
      This class is a partial implementation of the Template Method pattern[...]
      You may assume that constructing it is sufficient for it to set up a new
      thread, connect to the GPS reader hardware, and call the hook method
      whenever it receives new coordinates.
    """
    def __init__(self):
        self.gps = self.connectGps()
        self.gps.start()

    def locationReceived(self, latitude, longitude, altitude):
        """Hook method.
        Handle a set of coordinates. Implemented by child class(es)."""
        pass

    def connectGps(self):
        """Set up a thread for GPS communication."""
        gps = threading.Thread(target=self.runGps, args=())
        gps.daemon = True
        return gps

    def runGps(self):
        """Passes coordinates to locationReceived() every two seconds.
        Coordinates are read in from `coords.txt`."""
        coords = []
        with open("coords.txt", "r") as f:
            coords = [line.split(",")[0:3] for line in f.readlines()]

        for c in coords:
            self.locationReceived(c[0], c[1], c[2])
            time.sleep(2)
