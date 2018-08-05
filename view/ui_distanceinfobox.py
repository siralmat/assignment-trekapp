# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/distanceinfobox.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DistanceInfoBox(object):
    def setupUi(self, DistanceInfoBox):
        DistanceInfoBox.setObjectName("DistanceInfoBox")
        DistanceInfoBox.resize(157, 150)
        self.gridLayout = QtWidgets.QGridLayout(DistanceInfoBox)
        self.gridLayout.setContentsMargins(6, 14, 6, 14)
        self.gridLayout.setObjectName("gridLayout")
        self.label_horizontal = QtWidgets.QLabel(DistanceInfoBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_horizontal.sizePolicy().hasHeightForWidth())
        self.label_horizontal.setSizePolicy(sizePolicy)
        self.label_horizontal.setWordWrap(True)
        self.label_horizontal.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_horizontal.setObjectName("label_horizontal")
        self.gridLayout.addWidget(self.label_horizontal, 0, 0, 1, 1)
        self.horizontal = QtWidgets.QLabel(DistanceInfoBox)
        self.horizontal.setScaledContents(False)
        self.horizontal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.horizontal.setWordWrap(False)
        self.horizontal.setIndent(-1)
        self.horizontal.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.horizontal.setObjectName("horizontal")
        self.gridLayout.addWidget(self.horizontal, 0, 1, 1, 1)
        self.metres_label = QtWidgets.QLabel(DistanceInfoBox)
        self.metres_label.setObjectName("metres_label")
        self.gridLayout.addWidget(self.metres_label, 0, 2, 1, 1)
        self.label_ascent = QtWidgets.QLabel(DistanceInfoBox)
        self.label_ascent.setWordWrap(True)
        self.label_ascent.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_ascent.setObjectName("label_ascent")
        self.gridLayout.addWidget(self.label_ascent, 1, 0, 1, 1)
        self.ascent = QtWidgets.QLabel(DistanceInfoBox)
        self.ascent.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ascent.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.ascent.setObjectName("ascent")
        self.gridLayout.addWidget(self.ascent, 1, 1, 1, 1)
        self.metres_label_2 = QtWidgets.QLabel(DistanceInfoBox)
        self.metres_label_2.setObjectName("metres_label_2")
        self.gridLayout.addWidget(self.metres_label_2, 1, 2, 1, 1)
        self.label_descent = QtWidgets.QLabel(DistanceInfoBox)
        self.label_descent.setWordWrap(True)
        self.label_descent.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_descent.setObjectName("label_descent")
        self.gridLayout.addWidget(self.label_descent, 2, 0, 1, 1)
        self.descent = QtWidgets.QLabel(DistanceInfoBox)
        self.descent.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.descent.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.descent.setObjectName("descent")
        self.gridLayout.addWidget(self.descent, 2, 1, 1, 1)
        self.metres_label_3 = QtWidgets.QLabel(DistanceInfoBox)
        self.metres_label_3.setObjectName("metres_label_3")
        self.gridLayout.addWidget(self.metres_label_3, 2, 2, 1, 1)

        self.retranslateUi(DistanceInfoBox)
        QtCore.QMetaObject.connectSlotsByName(DistanceInfoBox)

    def retranslateUi(self, DistanceInfoBox):
        _translate = QtCore.QCoreApplication.translate
        DistanceInfoBox.setWindowTitle(_translate("DistanceInfoBox", "Form"))
        self.label_horizontal.setText(_translate("DistanceInfoBox", "Horizontal:"))
        self.horizontal.setText(_translate("DistanceInfoBox", "0000.0"))
        self.metres_label.setText(_translate("DistanceInfoBox", "m"))
        self.label_ascent.setText(_translate("DistanceInfoBox", "Ascent:"))
        self.ascent.setText(_translate("DistanceInfoBox", "0000.0"))
        self.metres_label_2.setText(_translate("DistanceInfoBox", "m"))
        self.label_descent.setText(_translate("DistanceInfoBox", "Descent:"))
        self.descent.setText(_translate("DistanceInfoBox", "0000.0"))
        self.metres_label_3.setText(_translate("DistanceInfoBox", "m"))

