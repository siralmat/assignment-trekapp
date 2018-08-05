# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/routeselectscreen.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RouteSelectScreen(object):
    def setupUi(self, RouteSelectScreen):
        RouteSelectScreen.setObjectName("RouteSelectScreen")
        RouteSelectScreen.resize(800, 600)
        self.stack = QtWidgets.QStackedWidget(RouteSelectScreen)
        self.stack.setGeometry(QtCore.QRect(20, 10, 771, 471))
        self.stack.setObjectName("stack")
        self.route_page = QtWidgets.QWidget()
        self.route_page.setObjectName("route_page")
        self.gridLayout = QtWidgets.QGridLayout(self.route_page)
        self.gridLayout.setObjectName("gridLayout")
        self.route_label = QtWidgets.QLabel(self.route_page)
        self.route_label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.route_label.sizePolicy().hasHeightForWidth())
        self.route_label.setSizePolicy(sizePolicy)
        self.route_label.setMinimumSize(QtCore.QSize(0, 32))
        self.route_label.setAlignment(QtCore.Qt.AlignCenter)
        self.route_label.setObjectName("route_label")
        self.gridLayout.addWidget(self.route_label, 0, 1, 1, 1)
        self.route_table = QtWidgets.QTableWidget(self.route_page)
        self.route_table.setEnabled(True)
        self.route_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.route_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.route_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.route_table.setColumnCount(3)
        self.route_table.setObjectName("route_table")
        self.route_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.route_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.route_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.route_table.setHorizontalHeaderItem(2, item)
        self.route_table.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.route_table, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.stack.addWidget(self.route_page)
        self.info_page = QtWidgets.QWidget()
        self.info_page.setObjectName("info_page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.info_page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.name = QtWidgets.QLabel(self.info_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)
        self.name.setMinimumSize(QtCore.QSize(0, 32))
        self.name.setTextFormat(QtCore.Qt.AutoText)
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.gridLayout_2.addWidget(self.name, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.info_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 3)
        self.info_grid = QtWidgets.QGridLayout()
        self.info_grid.setContentsMargins(2, 2, 2, 2)
        self.info_grid.setVerticalSpacing(0)
        self.info_grid.setObjectName("info_grid")
        self.label = QtWidgets.QLabel(self.info_page)
        self.label.setObjectName("label")
        self.info_grid.addWidget(self.label, 1, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.distance_info = DistanceInfoBox(self.info_page)
        self.distance_info.setMinimumSize(QtCore.QSize(150, 150))
        self.distance_info.setObjectName("distance_info")
        self.info_grid.addWidget(self.distance_info, 2, 0, 1, 2)
        self.dest_label = QtWidgets.QLabel(self.info_page)
        self.dest_label.setObjectName("dest_label")
        self.info_grid.addWidget(self.dest_label, 4, 0, 1, 2)
        self.waypoint_info = WaypointInfoBox(self.info_page)
        self.waypoint_info.setMinimumSize(QtCore.QSize(150, 150))
        self.waypoint_info.setObjectName("waypoint_info")
        self.info_grid.addWidget(self.waypoint_info, 5, 0, 1, 2)
        self.gridLayout_2.addLayout(self.info_grid, 3, 0, 1, 1)
        self.segment_table = QtWidgets.QTableWidget(self.info_page)
        self.segment_table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.segment_table.setLineWidth(1)
        self.segment_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.segment_table.setDragDropOverwriteMode(False)
        self.segment_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.segment_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.segment_table.setTextElideMode(QtCore.Qt.ElideNone)
        self.segment_table.setObjectName("segment_table")
        self.segment_table.setColumnCount(4)
        self.segment_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.segment_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.segment_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.segment_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.segment_table.setHorizontalHeaderItem(3, item)
        self.segment_table.horizontalHeader().setDefaultSectionSize(80)
        self.segment_table.horizontalHeader().setMinimumSectionSize(20)
        self.segment_table.horizontalHeader().setSortIndicatorShown(False)
        self.segment_table.horizontalHeader().setStretchLastSection(True)
        self.segment_table.verticalHeader().setVisible(False)
        self.segment_table.verticalHeader().setDefaultSectionSize(26)
        self.segment_table.verticalHeader().setSortIndicatorShown(False)
        self.segment_table.verticalHeader().setStretchLastSection(False)
        self.gridLayout_2.addWidget(self.segment_table, 3, 1, 1, 2)
        self.back_btn = QtWidgets.QPushButton(self.info_page)
        self.back_btn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_btn.sizePolicy().hasHeightForWidth())
        self.back_btn.setSizePolicy(sizePolicy)
        self.back_btn.setMinimumSize(QtCore.QSize(0, 32))
        self.back_btn.setMaximumSize(QtCore.QSize(80, 30))
        self.back_btn.setIconSize(QtCore.QSize(8, 8))
        self.back_btn.setObjectName("back_btn")
        self.gridLayout_2.addWidget(self.back_btn, 2, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 2)
        self.stack.addWidget(self.info_page)
        self.go_btn = QtWidgets.QPushButton(RouteSelectScreen)
        self.go_btn.setGeometry(QtCore.QRect(700, 480, 81, 81))
        self.go_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/go-icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.go_btn.setIcon(icon)
        self.go_btn.setIconSize(QtCore.QSize(64, 64))
        self.go_btn.setShortcut("G")
        self.go_btn.setFlat(True)
        self.go_btn.setObjectName("go_btn")
        self.exit_btn = QtWidgets.QPushButton(RouteSelectScreen)
        self.exit_btn.setGeometry(QtCore.QRect(20, 550, 65, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.exit_btn.sizePolicy().hasHeightForWidth())
        self.exit_btn.setSizePolicy(sizePolicy)
        self.exit_btn.setMinimumSize(QtCore.QSize(0, 32))
        self.exit_btn.setObjectName("exit_btn")
        self.view_btn = QtWidgets.QPushButton(RouteSelectScreen)
        self.view_btn.setEnabled(True)
        self.view_btn.setGeometry(QtCore.QRect(710, 510, 72, 32))
        self.view_btn.setIconSize(QtCore.QSize(64, 64))
        self.view_btn.setShortcut("")
        self.view_btn.setAutoDefault(False)
        self.view_btn.setDefault(False)
        self.view_btn.setFlat(False)
        self.view_btn.setObjectName("view_btn")

        self.retranslateUi(RouteSelectScreen)
        self.stack.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(RouteSelectScreen)

    def retranslateUi(self, RouteSelectScreen):
        _translate = QtCore.QCoreApplication.translate
        RouteSelectScreen.setWindowTitle(_translate("RouteSelectScreen", "Form"))
        self.route_label.setText(_translate("RouteSelectScreen", "<html><head/><body><p><span style=\" font-style:italic;\">Select a route from the list to view more information.</span></p></body></html>"))
        self.route_table.setSortingEnabled(False)
        item = self.route_table.horizontalHeaderItem(0)
        item.setText(_translate("RouteSelectScreen", "Name"))
        item = self.route_table.horizontalHeaderItem(1)
        item.setText(_translate("RouteSelectScreen", "Distance (m)"))
        item = self.route_table.horizontalHeaderItem(2)
        item.setText(_translate("RouteSelectScreen", "Description"))
        self.name.setText(_translate("RouteSelectScreen", "Placeholder route name here"))
        self.label.setText(_translate("RouteSelectScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Distance</span></p></body></html>"))
        self.dest_label.setText(_translate("RouteSelectScreen", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Destination</span></p></body></html>"))
        self.segment_table.setSortingEnabled(False)
        item = self.segment_table.horizontalHeaderItem(0)
        item.setText(_translate("RouteSelectScreen", "Latitude"))
        item = self.segment_table.horizontalHeaderItem(1)
        item.setText(_translate("RouteSelectScreen", "Longitude"))
        item = self.segment_table.horizontalHeaderItem(2)
        item.setText(_translate("RouteSelectScreen", "Altitude (m)"))
        item = self.segment_table.horizontalHeaderItem(3)
        item.setText(_translate("RouteSelectScreen", "Description"))
        self.back_btn.setText(_translate("RouteSelectScreen", "Back"))
        self.back_btn.setShortcut(_translate("RouteSelectScreen", "Backspace"))
        self.exit_btn.setText(_translate("RouteSelectScreen", "Exit"))
        self.view_btn.setText(_translate("RouteSelectScreen", "View"))

from view.distanceinfobox import DistanceInfoBox
from view.waypointinfobox import WaypointInfoBox