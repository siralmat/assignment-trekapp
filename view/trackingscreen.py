"""
Module: trackingscreen
Author: siralmat
"""
from PyQt5 import QtWidgets as Qw
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from view.ui_trackingscreen import Ui_TrackingScreen

class TrackingScreen(Qw.QWidget):
    """View for tracking progress through a route.
    Qt signals:
        exitTracking: User has finished the route.
    """
    trackingFinished = pyqtSignal()
    exitTracking = pyqtSignal()
    targetReached = pyqtSignal()

    def __init__(self, parent, controller):
        """Initialise screen with its parent window and a controller."""
        super().__init__()
        self._parent = parent
        self._ct = controller
        self._ui = Ui_TrackingScreen()
        self._ui.setupUi(self)

        controller.register(self.updateCurrent, "LOCATION")
        controller.register(self.updateTarget, "TARGET")
        controller.register(self.endReached, "END")
        self._ui.here_btn.clicked.connect(controller.targetReached)
        self._ui.back_btn.clicked.connect(self.exitTracking)
        self.trackingFinished.connect(self.finishTracking)

        # Set initial target
        self._ui.target_wp.update(controller.tracker.target)

    def endReached(self, update):
        """Triggered when the tracker indicates that the user has reached the
        end of the route."""
        self.trackingFinished.emit()

    @pyqtSlot()
    def finishTracking(self):
        """Print a message to the user then signal to main window and controller
        that tracking has concluded."""
        msg = "You finished the route!\nPress 'OK' to return to the route "\
              "selection screen."
        Qw.QMessageBox.information(self, "Congratulations!", msg)
        self._ct.trackingFinished()
        self.exitTracking.emit()

    def updateCurrent(self, update):
        """Triggered when current coordinates have changed."""
        self._ui.curr_wp.update(update.location)
        self._ui.dist_remaining.update(update.remaining)

    def updateTarget(self, update):
        """Triggered when target coordinates have changed."""
        self._ui.segment_info.setText(update.current_segment.description)
        self._ui.target_wp.update(update.target)
        self._ui.dist_remaining.update(update.remaining)
