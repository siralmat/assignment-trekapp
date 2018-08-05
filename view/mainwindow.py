"""
Module: mainwindow
Author: siralmat
"""

from PyQt5 import QtWidgets as Qw
from PyQt5.QtCore import pyqtSlot
from view.ui_mainwindow import Ui_MainWindow
from view.routeselectscreen import RouteSelectScreen
from view.trackingscreen import TrackingScreen

class MainWindow(Qw.QMainWindow):
    """Primary view class for TrekApp.
    MainWindow instantiates widgets for each 'screen' in the app.
    Screens are drawn inside the main window.
    """

    def __init__(self, controller):
        """Set up the main window and initialise widgets.
        Args:
            controller: A route controller.
        """
        super().__init__()
        self._ct = controller
        self._widgets = {}
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._ui.about_action.triggered.connect(self.aboutInfo)
        self._ui.file_load_action.triggered.connect(self.fileLoadPrompt)
        self._ui.exit_btn.clicked.connect(self.close)
        self._ui.download_btn.clicked.connect(controller.downloadAction)
        self._ui.download_action.triggered.connect(controller.downloadAction)

        self._ct.register(self.startRouteSelect, "LOADED")
        self._ct.register(self.displayError, "ERROR")

    @pyqtSlot()
    def fileLoadPrompt(self):
        """Ask user to select a file, then pass the filename to controller."""
        filename, _ = Qw.QFileDialog.getOpenFileName(self, 'Route file', '/')
        if filename:
            self._ct.fileLoadAction(filename)

    @pyqtSlot()
    def aboutInfo(self):
        """Display a message with information about the program."""
        msg = "Hello, and welcome to my assignment!\n"\
              "For more information, please see readme.md in the main program "\
              "directory."
        Qw.QMessageBox.information(self, "About", msg)

    def startRouteSelect(self, route_collection):
        """Create and open the route selection screen.
        If route screen existed previously, it is destroyed.
        """
        stack = self._ui.screen_stack
        if "RouteSelectScreen" in self._widgets:
            stack.removeWidget(self._widgets["RouteSelectScreen"])
        screen = RouteSelectScreen(self, self._ct)
        self._widgets["RouteSelectScreen"] = screen
        stack.addWidget(screen)
        screen.routeSelected.connect(self.startTracking)
        stack.setCurrentWidget(self._widgets["RouteSelectScreen"])

    @pyqtSlot()
    def displayRouteSelect(self):
        """Called when a user finishes tracking a route."""
        self._ui.screen_stack.setCurrentWidget(self._widgets["RouteSelectScreen"])

    @pyqtSlot(str)
    def startTracking(self, route_name):
        """Create and open a tracking screen for the given route.
        If previously opened, destroy the original screen."""
        controller = self._ct.startNavigation(route_name)
        if not controller:
            self.displayError("Something went wrong while accessing the route :(")
        else:
            if "TrackingScreen" in self._widgets:
                self._ui.screen_stack.removeWidget(self._widgets["TrackingScreen"])
            screen = TrackingScreen(self, controller)
            screen.exitTracking.connect(self.displayRouteSelect)
            self._widgets["TrackingScreen"] = screen
            self._ui.screen_stack.addWidget(screen)
            self._ui.screen_stack.setCurrentWidget(screen)

    def closeEvent(self, event):
        """Handle a request to close the app with a confirmation prompt."""
        reply = Qw.QMessageBox.question(self, "Exit", "Really exit?",
                                        Qw.QMessageBox.Yes | Qw.QMessageBox.No,
                                        Qw.QMessageBox.No)
        if reply == Qw.QMessageBox.Yes:
            Qw.QApplication.instance().quit()
        else:
            event.ignore()

    @pyqtSlot(str)
    def displayError(self, message):
        """Print an error message to the user in a popup message box.
        Args:
            message: Full content of the error message to display.
        """
        msg = Qw.QMessageBox()
        msg.setText(message)
        msg.exec_()
