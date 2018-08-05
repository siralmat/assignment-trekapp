"""
Module: routeselectscreen
Author: siralmat
"""

from PyQt5 import QtWidgets as Qw
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from view.ui_routeselectscreen import Ui_RouteSelectScreen

class RouteSelectScreen(Qw.QWidget):
    """
    Route selection screen.
    Displays a table of routes to the user. User may select a route to view more
    detailed information.
    Qt Signals:
        routeSelected: User has confirmed selection of a route.
    """
    routeSelected = pyqtSignal(str)

    def __init__(self, parent, controller):
        """Initialise route selection screen.
        Args:
            parent: Parent view.
            controller: Route controller.
        """
        super().__init__()
        self._parent = parent
        self._ct = controller
        self._ui = Ui_RouteSelectScreen()
        self._ui.setupUi(self)

        self._ui.exit_btn.clicked.connect(self._parent.close)
        self._ui.view_btn.clicked.connect(self.routeInfoEvent)
        self._ui.go_btn.clicked.connect(self.routeSelectEvent)
        self._ui.route_table.cellDoubleClicked.connect(self.routeInfoEvent)
        self._ui.segment_table.cellDoubleClicked.connect(self.routeSelectEvent)
        self._ui.back_btn.clicked.connect(self.displayRoutePage)

        self._buildRouteTable(self._ct.getAll())
        self.displayRoutePage()

    def _buildRouteTable(self, routes):
        data = [[r.name, round(r.distance.horizontal, 2), r.description] for r in routes]
        self._buildTable(self._ui.route_table, data)
        self._ui.route_table.setSortingEnabled(True)

    def _buildSegmentTable(self, route):
        data = [[s.start.lat, s.start.long, s.start.alt, s.description] for s in route]
        self._buildTable(self._ui.segment_table, data)

    def _buildTable(self, table, data):
        table.setRowCount(len(data))
        row = 0
        col = 0
        for line in data:
            for item in line:
                item = Qw.QTableWidgetItem(str(item))
                table.setItem(row, col, item)
                col += 1
            row += 1
            col = 0

    @pyqtSlot()
    def routeInfoEvent(self):
        """Called when user requests detailed information for a route.
        Fetches the route details and displays segments and other route info.
        """
        row = self._ui.route_table.currentRow()
        route_name = self._ui.route_table.item(row, 0).text()
        route = self._ct.get(route_name)

        self._ui.name.setText("Viewing route: <b>{}</b>".format(route_name))
        self._ui.distance_info.update(route.distance)
        self._ui.waypoint_info.update(route.end)
        self._buildSegmentTable(route)

        self._ui.go_btn.show()
        self._ui.view_btn.hide()
        self._ui.stack.setCurrentWidget(self._ui.info_page)

    @pyqtSlot()
    def routeSelectEvent(self):
        """Triggered when user selects a route from the table.
        Prompts user to confirm, then emits the routeSelected signal."""
        row = self._ui.route_table.currentRow()
        selection = self._ui.route_table.item(row, 0).text()
        msg = "You have selected the route '{}'.\n"\
              "Do you want to start your trek?".format(selection)
        reply = Qw.QMessageBox.question(self, "Select route", msg,
                                        Qw.QMessageBox.Yes | Qw.QMessageBox.No,
                                        Qw.QMessageBox.No)
        if reply == Qw.QMessageBox.Yes:
            self.routeSelected.emit(selection)

    def displayRoutePage(self):
        """Instructs the stack to display the table of available routes.
        Called when returning from the segment table or when route data has
        been reloaded.
        """
        self._ui.stack.setCurrentWidget(self._ui.route_page)
        self._ui.go_btn.hide()
        self._ui.view_btn.show()

    def displayInfoPage(self, route_name):
        """Instruct the stack to build a table of segments for the selected
        route, then display it."""
        self._buildSegmentTable(route_name)
        self._ui.stack.setCurrentWidget(self._ui.info_page)
        self._ui.go_btn.show()
        self._ui.view_btn.hide()
