"""
Module: routecollection
Author: siralmat
"""
import os
from controller.geoutils import retrieveRouteData
from model.routeparser import RouteParser, RouteFormatError
from model.observable import Observable

class RouteCollection(Observable):
    """
    A collection model of routes.
    Implements Observable. Available events and their arguments:
        LOADED (Route data has been (re)created): self
        ERROR (Exception raised during operation): message
    """
    def __init__(self):
        """Initialise an empty route collection."""
        super().__init__()
        self._routes = {}

    def get(self, route_name):
        """Return the route for the provided name, or None if not available.
        Args:
            route_name: Unique string identifier for a route.
        """
        return self._routes.get(route_name, None)

    def contains(self, route_name):
        """Check if the collection has a route by the provided name.
        Attributes:
            route_name: Unique string identifier for a route.
        """
        return route_name in self._routes

    def getAll(self):
        """Return a list of all route objects."""
        return self._routes.values()

    def loadFromFile(self, filename):
        """Attempt to load routes from file. Retrieved routes overwrite any
        existing routes."""
        try:
            if os.path.exists(filename):
                with open(filename, "r") as f:
                    self._loadRoutes(f.read())
        except IOError as e:
            msg = "An error occured while accesssing file.\n'{}'".format(e)
            self._notify("ERROR", msg)

    def retrieveRoutes(self):
        """Retrieve updated routes from server.
        Retrieved routes overwrite any existing routes.
        Raises:
            RouteFormatError: data was malformed/incomplete
            IOError: unable to access server
        """
        try:
            data = retrieveRouteData()
            if not data:
                self._notify("ERROR", "No routes found.")
            else:
                self._loadRoutes(data)
        except IOError as e:
            msg = "An error occured while retrieving routes.\n'{}'".format(e)
            self._notify("ERROR", msg)

    def _loadRoutes(self, data):
        try:
            parser = RouteParser(data)
            self._routes = parser.parse()
            self._notify("LOADED", self)
        except (RouteFormatError, ValueError) as e:
            msg = "An error occured while parsing routes.\n{}".format(e)
            self._notify("ERROR", msg)

    def __len__(self):
        return len(self._routes)

    def __iter__(self):
        return iter(self._routes)
