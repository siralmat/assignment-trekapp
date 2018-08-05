"""
Module: waypointinfobox
Author: siralmat
"""

from PyQt5 import QtWidgets as Qw
from view.ui_waypointinfobox import Ui_WaypointInfoBox

class WaypointInfoBox(Qw.QWidget):
    """Small widget to display information about a waypoint."""
    def __init__(self, parent):
        super().__init__()
        self._parent = parent
        self._ui = Ui_WaypointInfoBox()
        self._ui.setupUi(self)

    def update(self, waypoint):
        """Update waypoint coordinates."""
        self._ui.wp_lat.setText(format(waypoint.lat, ".4f"))
        self._ui.wp_long.setText(format(waypoint.long, ".4f"))
        self._ui.wp_alt.setText(format(waypoint.alt, ".1f"))
