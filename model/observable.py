"""
Module: observable
Author: siralmat
"""
from collections import defaultdict
import weakref

class Observable(object):
    """A common 'interface' class for subjects/observables.
    Objects can register callbacks and an optional event name. By default,
    callbacks are registered for all events. When the event is triggered, a
    variable list of arguments will be sent to the function.
    """
    def __init__(self):
        """Initialise an empty set of callbacks."""
        self._callbacks = defaultdict(set)
        super().__init__()

    def register(self, callback, event_name="ALL"):
        """Register a new callback function with optional event type."""
        self._callbacks[event_name].add(weakref.WeakMethod(callback))

    def deregister(self, callback, event_name):
        """Deregister a callback from an event."""
        pass
        #todo

    def deregisterAll(self):
        """Deregister all callbacks."""
        self._callbacks = defaultdict(set)

    def _notify(self, event_name, *args):
        for func in self._callbacks[event_name]:
            func()(*args)
        for func in self._callbacks["ALL"]:
            func()(*args)
