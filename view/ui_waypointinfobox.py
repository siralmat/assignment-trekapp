# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/waypointinfobox.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WaypointInfoBox(object):
    def setupUi(self, WaypointInfoBox):
        WaypointInfoBox.setObjectName("WaypointInfoBox")
        WaypointInfoBox.resize(150, 150)
        self.layoutWidget = QtWidgets.QWidget(WaypointInfoBox)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 20, 151, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.long_label = QtWidgets.QLabel(self.layoutWidget)
        self.long_label.setScaledContents(False)
        self.long_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.long_label.setObjectName("long_label")
        self.gridLayout.addWidget(self.long_label, 1, 0, 1, 1)
        self.wp_lat = QtWidgets.QLabel(self.layoutWidget)
        self.wp_lat.setStyleSheet("")
        self.wp_lat.setScaledContents(False)
        self.wp_lat.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.wp_lat.setObjectName("wp_lat")
        self.gridLayout.addWidget(self.wp_lat, 0, 1, 1, 1)
        self.wp_alt = QtWidgets.QLabel(self.layoutWidget)
        self.wp_alt.setStyleSheet("")
        self.wp_alt.setScaledContents(False)
        self.wp_alt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.wp_alt.setObjectName("wp_alt")
        self.gridLayout.addWidget(self.wp_alt, 2, 1, 1, 1)
        self.alt_label = QtWidgets.QLabel(self.layoutWidget)
        self.alt_label.setScaledContents(False)
        self.alt_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.alt_label.setObjectName("alt_label")
        self.gridLayout.addWidget(self.alt_label, 2, 0, 1, 1)
        self.lat_label = QtWidgets.QLabel(self.layoutWidget)
        self.lat_label.setScaledContents(False)
        self.lat_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lat_label.setObjectName("lat_label")
        self.gridLayout.addWidget(self.lat_label, 0, 0, 1, 1)
        self.degrees1 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.degrees1.sizePolicy().hasHeightForWidth())
        self.degrees1.setSizePolicy(sizePolicy)
        self.degrees1.setMinimumSize(QtCore.QSize(5, 0))
        self.degrees1.setObjectName("degrees1")
        self.gridLayout.addWidget(self.degrees1, 1, 2, 1, 1)
        self.degrees2 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.degrees2.sizePolicy().hasHeightForWidth())
        self.degrees2.setSizePolicy(sizePolicy)
        self.degrees2.setMinimumSize(QtCore.QSize(5, 0))
        self.degrees2.setObjectName("degrees2")
        self.gridLayout.addWidget(self.degrees2, 0, 2, 1, 1)
        self.wp_long = QtWidgets.QLabel(self.layoutWidget)
        self.wp_long.setObjectName("wp_long")
        self.gridLayout.addWidget(self.wp_long, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)

        self.retranslateUi(WaypointInfoBox)
        QtCore.QMetaObject.connectSlotsByName(WaypointInfoBox)

    def retranslateUi(self, WaypointInfoBox):
        _translate = QtCore.QCoreApplication.translate
        WaypointInfoBox.setWindowTitle(_translate("WaypointInfoBox", "Form"))
        self.long_label.setText(_translate("WaypointInfoBox", "Longitude:"))
        self.wp_lat.setText(_translate("WaypointInfoBox", "000.00"))
        self.wp_alt.setText(_translate("WaypointInfoBox", "000.00"))
        self.alt_label.setText(_translate("WaypointInfoBox", "Altitude:"))
        self.lat_label.setText(_translate("WaypointInfoBox", "Latitude:"))
        self.degrees1.setText(_translate("WaypointInfoBox", "°"))
        self.degrees2.setText(_translate("WaypointInfoBox", "°"))
        self.wp_long.setText(_translate("WaypointInfoBox", "000.00"))

