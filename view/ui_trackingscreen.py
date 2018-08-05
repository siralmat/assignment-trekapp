# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/trackingscreen.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TrackingScreen(object):
    def setupUi(self, TrackingScreen):
        TrackingScreen.setObjectName("TrackingScreen")
        TrackingScreen.resize(800, 600)
        self.here_btn = QtWidgets.QPushButton(TrackingScreen)
        self.here_btn.setGeometry(QtCore.QRect(630, 220, 81, 32))
        self.here_btn.setObjectName("here_btn")
        self.back_btn = QtWidgets.QPushButton(TrackingScreen)
        self.back_btn.setGeometry(QtCore.QRect(20, 550, 113, 32))
        self.back_btn.setFlat(False)
        self.back_btn.setObjectName("back_btn")
        self.segment_info = QtWidgets.QLabel(TrackingScreen)
        self.segment_info.setGeometry(QtCore.QRect(30, 230, 201, 91))
        self.segment_info.setAutoFillBackground(False)
        self.segment_info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.segment_info.setWordWrap(True)
        self.segment_info.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.segment_info.setObjectName("segment_info")
        self.remaining = QtWidgets.QFrame(TrackingScreen)
        self.remaining.setGeometry(QtCore.QRect(310, 270, 201, 201))
        self.remaining.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.remaining.setFrameShadow(QtWidgets.QFrame.Raised)
        self.remaining.setLineWidth(2)
        self.remaining.setObjectName("remaining")
        self.widget = QtWidgets.QWidget(self.remaining)
        self.widget.setGeometry(QtCore.QRect(30, 10, 152, 176))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.remaining_label = QtWidgets.QLabel(self.widget)
        self.remaining_label.setAlignment(QtCore.Qt.AlignCenter)
        self.remaining_label.setObjectName("remaining_label")
        self.verticalLayout.addWidget(self.remaining_label)
        self.dist_remaining = DistanceInfoBox(self.widget)
        self.dist_remaining.setMinimumSize(QtCore.QSize(150, 150))
        self.dist_remaining.setObjectName("dist_remaining")
        self.verticalLayout.addWidget(self.dist_remaining)
        self.widget1 = QtWidgets.QWidget(TrackingScreen)
        self.widget1.setGeometry(QtCore.QRect(30, 30, 741, 186))
        self.widget1.setObjectName("widget1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.curr_label = QtWidgets.QLabel(self.widget1)
        self.curr_label.setAlignment(QtCore.Qt.AlignCenter)
        self.curr_label.setObjectName("curr_label")
        self.gridLayout.addWidget(self.curr_label, 2, 0, 1, 1)
        self.curr_wp = WaypointInfoBox(self.widget1)
        self.curr_wp.setMinimumSize(QtCore.QSize(150, 150))
        self.curr_wp.setObjectName("curr_wp")
        self.gridLayout.addWidget(self.curr_wp, 3, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.target_label = QtWidgets.QLabel(self.widget1)
        self.target_label.setAlignment(QtCore.Qt.AlignCenter)
        self.target_label.setObjectName("target_label")
        self.gridLayout_2.addWidget(self.target_label, 2, 0, 1, 1)
        self.target_wp = WaypointInfoBox(self.widget1)
        self.target_wp.setMinimumSize(QtCore.QSize(150, 150))
        self.target_wp.setObjectName("target_wp")
        self.gridLayout_2.addWidget(self.target_wp, 3, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 2, 1, 1)

        self.retranslateUi(TrackingScreen)
        QtCore.QMetaObject.connectSlotsByName(TrackingScreen)

    def retranslateUi(self, TrackingScreen):
        _translate = QtCore.QCoreApplication.translate
        TrackingScreen.setWindowTitle(_translate("TrackingScreen", "Form"))
        self.here_btn.setText(_translate("TrackingScreen", "I\'m here!"))
        self.back_btn.setText(_translate("TrackingScreen", "Exit navigation"))
        self.segment_info.setText(_translate("TrackingScreen", "<html><head/><body><p><span style=\" font-style:italic;\">Make your way to the start of the route!</span></p></body></html>"))
        self.remaining_label.setText(_translate("TrackingScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Remaining</span></p></body></html>"))
        self.curr_label.setText(_translate("TrackingScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Current GPS location</span></p></body></html>"))
        self.target_label.setText(_translate("TrackingScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Target</span></p></body></html>"))

from view.distanceinfobox import DistanceInfoBox
from view.waypointinfobox import WaypointInfoBox
