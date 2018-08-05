"""
Module: route
Author: siralmat
Contents:
    Route
    RouteCollection
    Segment
    SubrouteSegment
"""
from model.distance import Distance

class Route:
    """Class storing information about a route used by trekkers or climbers.
    A route is a composite structure consisting of segments and subroutes, with
    a start and end point. Subroutes may contain
    further subroutes.

    Attributes:
        name: Unique route identifier
        description: Text description
        start: Start of route (Waypoint)
        end: Final location on route (Waypoint)
        segments: List of segments and subroutes
        distance: Total distance traversed, including subroutes (Distance)
    """
    def __init__(self, name, desc, segments):
        """Initialise route with a name, description, and list of
        segments. During initialisation, calculate the total distance of the
        route and store as a Distance object.
        """
        self.name = name
        self.description = desc
        self.segments = segments
        self.start = segments[0].start
        self.end = segments[-1].end
        self.distance = self._calcTotalDistance()

    def _calcTotalDistance(self):
        """Calculate 3 measurements of distance from a route's segments:
        - total ascent
        - total descent
        - total horizontal distance
        Ascent and descent are 'net' totals from all segments. For example, if a
        segment finishes at a higher altitude, the difference between the start
        and end altitude is added to the ascent measurement.
        """
        dist = Distance()
        for s in self.segments:
            dist.addDistance(s.distance)
        return dist

    def __iter__(self):
        """Generator that steps through a route, recursively visiting any
        subroutes.
        Yields: Route segments
        """
        for s in self.segments:
            yield from iter(s)


class Segment:
    """Stores information about a segment/section on a route: its description
    and final waypoint.
    A segment is a 'leaf' in the composite Route structure.
    Attributes:
        start: Beginning location (Waypoint)
        end: Final location (Waypoint)
        description: Description of segment, eg: hazards, recommended gear
        distance: length of segment (Distance)
    """

    def __init__(self, start, end, desc):
        """Initialise a segment object with an end waypoint and a description."""
        self.start = start
        self.end = end
        self.description = desc
        self.distance = start.distanceFrom(end)

    def __iter__(self):
        """An attempted solution to composition issues.
        When called by the route generator, simply yields itself. This allows
        the route generator to treat segments and subroute segments equally.
        """
        yield self


class SubrouteSegment(Segment):
    """Stores information about a route segment that points to another route.
    A subroute segment is equivalent to a node in a composite structure.
    Attributes:
        subroute: the Route referenced by the segment
    """
    def __init__(self, start, end, subroute):
        """Initialise subroute segment with end waypoint and a subroute."""
        super().__init__(start, end, subroute.description)
        self.subroute = subroute
        self.distance = Distance() # things get a little weird otherwise

    def __iter__(self):
        """Generator that yields a full subroute, including its starting section.
        Yields: Itself and all segments included in the subroute.
        """
        yield from iter(self.subroute)
