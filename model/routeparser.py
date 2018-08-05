"""
Module: routeparser
Author: siralmat
Contents:
    RouteParser: Creates a RouteCollection from a provided string of routes.
    RouteFormatError: Thrown by RouteParser when encountering invalid formatting.
"""
import re
from model.route import Route, Segment, SubrouteSegment
from model.waypoint import Waypoint, CoordinateError

class RouteParser:
    """Store and subsequently parse a raw string of route data into
    Waypoints, Segments, and Routes, stored in a dictionary.

    The route data must follow a specific format and may contain several routes.
    Leading/trailing whitespace is ignored.
    Route identifiers can contain alphanumeric characters or underscores, but
    cannot begin with a number.
    Component format (each separated by a newline:
        Start of route:      route-id description
        Segment:             [lat],[long],[alt],[segment description]
        Subroute:            [lat],[long],[alt],*[subroute identifier]
        End:                 [lat],[long],[alt]

    Attributes:
        raw: The raw route data provided at initialisation.
        route_dict: The dictionary populated with routes after parsing.
    """
    def __init__(self, raw):
        """Initialise RouteParser with raw data."""
        self.raw = raw
        self.route_dict = {}

    def parse(self):
        """Create and store Routes from the raw data.
        Returns:
            A dictionary containing all parsed routes.
        Raises:
            RouteFormatError: Raw data does not match expected format.
            """
        chunks = self._splitChunks()
        self._buildRoutes(chunks)
        return self.route_dict

    def _splitChunks(self):
        """Split the raw data into text chunks identifying each unique route,
        then return the list of chunks.
        Raises:
            RouteFormatError: Data ends unexpectedly, indicating malformed
                                or missing route information.
        """
        # Route splitting algorithm:
        #   1. Iterate through the lines of raw data:
        #     a. Strip whitespace from start/end.
        #     b. Append to the last element of the chunk list.
        #     c. If at the end of the route, create empty list for next route.
        #   2. Verify that the last list element is empty.
        #   3. Remove the empty element and return the list of route chunks.
        chunk_list = [[]]
        for line in self.raw.splitlines():
            line = line.strip()
            chunk_list[-1].append(line)
            # Check if last line of route (3 comma-separated decimals)
            if len(line.split(",")) == 3:
                if (line[0].isdigit()) or (line[0] == "-"):
                    chunk_list.append([])
        if chunk_list[-1]:
            raise RouteFormatError("Unexpected end of route data.")
        chunk_list.pop()
        return chunk_list

    def _buildRoutes(self, chunks):
        """Parse a list of text chunks into routes, building connections
        between them. As routes are created, they are stored in route_dict.
        Returns: none
        """
        # In order to build links between routes, any subroutes must already
        # exist. This is accomplished with a queue. If a route contains
        # subroutes that do not exist yet, it is returned to the queue.
        iter_limit = len(chunks) * len(chunks) # (very) lazy sanity check
        while chunks and (iter_limit > 0):
            current = chunks.pop(0)
            subroutes = self._findSubRoutes(current)
            if any([x for x in subroutes if not x in self.route_dict]):
                chunks.append(current)
            else:
                route = self._buildRoute(current)
                self.route_dict[route.name] = route
            iter_limit -= 1
        if iter_limit == 0:
            raise RouteFormatError("Route data contains invalid or circular "\
                                   "references")

    def _buildRoute(self, chunk):
        segment_list = []
        try:
            # First/last lines have special formatting. Need to process first
            route_id_line = chunk.pop(0).split(None, 1)
            route_name = route_id_line[0]
            route_desc = route_id_line[1]

            start_line = chunk.pop(0).split(",", 3)
            start = start_line[:3]
            desc = start_line[3]
            route_end = chunk.pop().split(",")
            for l in chunk:
                line = l.split(",", 3)
                end = line[:3]
                segment_list.append(self._buildSegment(start, end, desc))
                start = end
                desc = line[3]
            # build final segment using route end
            segment_list.append(self._buildSegment(start, route_end, desc))
            return Route(route_name, route_desc, segment_list)
        except IndexError:
            raise RouteFormatError("Unable to build route from raw data: " \
            "missing required information in block '{0}'".format(route_id_line[0]))

    def _buildSegment(self, start_coords, end_coords, description):
        """Create a route segment from the end waypoint and description.
        If the description indicates the start of a subroute, retrieve the
        route from the route_dict and link it to the segment.
        """
        start = self._buildWaypoint(start_coords)
        end = self._buildWaypoint(end_coords)
        if description.startswith("*"):
            subroute = self.route_dict.get(description[1:], None)
            if not subroute:
                msg = "Invalid subroute identifier '{}'".format(description)
                raise RouteFormatError(msg)
            return SubrouteSegment(start, end, subroute)
        return Segment(start, end, description)

    def _buildWaypoint(self, coords):
        """Create a waypoint from the given coordinates."""
        try:
            return Waypoint(coords[0], coords[1], coords[2])
        except CoordinateError as e:
            msg = "Unable to build waypoint from '{}': {}".format(coords, e)
            raise RouteFormatError(msg)

    def _findSubRoutes(self, route):
        """Check whether a route has any subroutes, then return their
        identifiers as a list.
        """
        subroute = re.compile(r'^((?:-?[\d]+(?:.[\d]+)?,){3})\*(\w*)$',
                              re.MULTILINE)
        return [m.group(2) for l in route for m in [re.match(subroute, l)] if m]

class RouteFormatError(Exception):
    """Exception class used by RouteParser.
    Indicates that the raw route data contained a formatting error or is
    incomplete.
    """
    pass
