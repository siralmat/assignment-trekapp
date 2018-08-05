"""
Module: appcontroller
Author: siralmat
"""
from controller.trackingcontroller import TrackingController
from model.tracker import Tracker

class AppController:
    """
    A controller for a view communicating with a route collection.
    Provides functionality to manipulate the collection.
    """
    def __init__(self, collection):
        """Initialise controller with the provided route collection and view.
        """
        self._collection = collection

    def register(self, view_func, event_type):
        """Pass through view registrations to the collection."""
        self._collection.register(view_func, event_type)

    def downloadAction(self):
        """Instruct route collection to retrieve updated routes from server."""
        self._collection.retrieveRoutes()

    def fileLoadAction(self, filename):
        """Instruct the route collection to (re)load routes from file.
        Args:
            filename: Location of route data"""
        self._collection.loadFromFile(filename)

    def get(self, name):
        """Return route matching the given name, or None if it doesn't exist."""
        return self._collection.get(name)

    def getAll(self):
        """Return a list of all routes."""
        return self._collection.getAll()

    def startNavigation(self, route_name):
        """Construct a tracking controller to manage a route.
        Returns: a new TrackingController, or None if unable to construct.
        """
        route = self._collection.get(route_name)
        if route:
            tracker = Tracker(route)
            controller = TrackingController(tracker)
            return controller
        return None
