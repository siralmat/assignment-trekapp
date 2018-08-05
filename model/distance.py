"""
Module: distance
Author: siralmat
"""

class Distance:
    """A simple class storing distance measurements and providing simple
    operations to manipulate them.
    Attributes:
        horizontal: Horizontal distance (in m).
        ascent: Vertical ascent (in m).
        descent: Vertical descent (in m).
    """
    def __init__(self, horizontal=0.0, ascent=0.0, descent=0.0):
        """Initialise a distance object with horizontal/vertical distances."""
        self.horizontal = float(horizontal)
        self.ascent = float(ascent)
        self.descent = float(descent)

    def addDistance(self, distance):
        """Add another distance to self.
        Args:
            distance: A Distance object.
        Returns: none
        """
        self.horizontal += distance.horizontal
        self.ascent += distance.ascent
        self.descent += distance.descent

    def subtractDistance(self, distance):
        """Subtract another distance from self.
        Args:
            distance: A Distance object.
        Returns: none
        """
        self.horizontal -= distance.horizontal
        self.ascent -= distance.ascent
        self.descent -= distance.descent

    def __add__(self, distance):
        out = Distance()
        out.horizontal = self.horizontal + distance.horizontal
        out.ascent = self.ascent + distance.ascent
        out.descent = self.descent + distance.descent
        return out

    def __sub__(self, distance):
        out = Distance()
        out.horizontal = self.horizontal - distance.horizontal
        out.ascent = self.ascent - distance.ascent
        out.descent = self.descent - distance.descent
        return out
