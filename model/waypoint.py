"""
Module:
Author: siralmat
Contents:
    Waypoint
    CoordinateError
"""
from controller.geoutils import calcMetresDistance
from model.distance import Distance

class Waypoint:
    """A 3D point in space with coordinates and an altitude.
    A waypoint can measure the distance between itself and another waypoint.
    Attributes:
        lat: Waypoint latitude as a float. Must be between -90.0 and 90.0
        long: Waypoint longitude as a float. Must be between -180.0 and 180.0.
        alt: Waypoint altitude in metres as a float. No validation rules.
    """
    def __init__(self, lat, long, alt):
        """Initialise a waypoint object with its coordinates and altitude.
        Raises:
            CoordinateError: latitude or longitude invalid"""
        try:
            lat = float(lat)
            long = float(long)
            alt = float(alt)
            if lat < -90.0 or lat > 90.0:
                raise CoordinateError("Latitude value '{}' outside accepted "\
                "range of -90.0° to 90.0°".format(lat))
            if long < -180.0 or long > 180.0:
                raise CoordinateError("Longitude value '{}' outside accepted "\
                             "range of -180.0° to 180.0°".format(long))
            self.lat = lat
            self.long = long
            self.alt = alt
        except TypeError:
            raise CoordinateError("Coordinates must be integer or real numbers.")

    def distanceFrom(self, waypoint):
        """Calculate the distance between self and another location.
        Args:
            waypoint: Another waypoint object.
        Returns: A distance object containing horizontal/vertical distance
        between locations.
        """
        dist = Distance()
        dist.horizontal += calcMetresDistance(self.lat, self.long,
                                              waypoint.lat, waypoint.long)
        vertical = self.alt - waypoint.alt
        if vertical > 0:
            dist.descent += vertical
        else:
            dist.ascent += abs(vertical)
        return dist


class CoordinateError(Exception):
    """
    Exception class raised by Waypoint.
    Indicates that coordinates do not fall within valid ranges, or are not
    valid numbers.
    """
    pass
