"""
Module: tracker
Author: siralmat
"""
from model.gpslocator import GpsLocator
from model.waypoint import Waypoint
from model.observable import Observable

class Tracker (Observable, GpsLocator):
    """Maintains position along a route.
    Inherits from GpsLocator, which updates location via the locationReceived
    hook method.
    Tracker can register observers with associated events.
    Available events:
        LOCATION: new GPS location
        WAYPOINT: new target waypoint
        END: reached the last target
    All events pass the Tracker instance as an argument.
    Attributes:
        location: Last reported location (Waypoint)
        target: Next target on route (Waypoint)
        remaining: How much of the route is left to travel (Distance)
        current_segment: Current route segment
    """
    def __init__(self, route):
        """Initialise tracker with a route and set current location & target."""
        self._route = route
        self._segments = iter(route)
        self.location = None
        self.target = route.start
        self.current_segment = next(self._segments)
        self._remaining = self._route.distance
        super().__init__()

    @property
    def remaining(self):
        """Returns: remaining distance on route as a Distance"""
        if not self.location:
            return self._remaining
        return self._remaining + self.location.distanceFrom(self.target)

    @property
    def remaining_segment(self):
        """Returns: remaining distance until next target as a Distance, or None
        if current location is unavailable."""
        if not self.location:
            return None
        return self.location.distanceFrom(self.target)

    def locationReceived(self, latitude, longitude, altitude):
        """Hook method from parent class, called when GPS updates are received.
        May also be called to manually update (e.g. from user input).
        Args:
            latitude, longitude, altitude: last reported position.
        """
        self.location = Waypoint(latitude, longitude, altitude)
        self._notify("LOCATION", self)
        if self._atTarget():
            self.updateTarget()

    def _atTarget(self):
        diff = self.location.distanceFrom(self.target)
        if diff.horizontal < 10.0:
            if diff.descent < 2.0 and diff.ascent < 2.0:
                return True
        return False

    def updateTarget(self):
        """Mark current target as reached; move to next target. Does not update
        current location.
        """
        try:
            self._remaining = self._remaining - self.current_segment.distance
            self.current_segment = next(self._segments)
            self.target = self.current_segment.end
            self._notify("TARGET", self)
        except StopIteration:
            self._notify("END", self)
