"""
Module: trackingcontroller
Author: siralmat
"""

class TrackingController:
    """A controller class that interacts with a tracker object.
    Attributes:
        tracker: Tracker passed in at creation.
    """
    def __init__(self, tracker):
        """Initialise controller with a Tracker object.
        """
        self.tracker = tracker

    def targetReached(self):
        """Instruct the tracker to mark a target as reached."""
        self.tracker.updateTarget()

    def trackingFinished(self):
        """Deregister all events from tracker."""
        self.tracker.deregisterAll()

    def register(self, view_func, event_name):
        """Pass through a view registration event to the tracker"""
        self.tracker.register(view_func, event_name)
