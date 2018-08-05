"""
Module: distanceinfobox
Author: siralmat
"""

from PyQt5 import QtWidgets as Qw
from view.ui_distanceinfobox import Ui_DistanceInfoBox

class DistanceInfoBox(Qw.QWidget):
    """Small widget to display information about a distance."""
    def __init__(self, parent):
        """Set up layout."""
        super().__init__()
        self._parent = parent
        self._ui = Ui_DistanceInfoBox()
        self._ui.setupUi(self)

    def update(self, distance):
        """Update distance values."""
        self._ui.horizontal.setText(format(distance.horizontal, ".2f"))
        self._ui.ascent.setText(format(distance.ascent, ".2f"))
        self._ui.descent.setText(format(distance.descent, ".2f"))
