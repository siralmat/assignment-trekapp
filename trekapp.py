#!/usr/bin/env python3
"""
Module: trekapp
Author: siralmat
"""
import sys
from PyQt5.QtWidgets import QApplication
from controller.appcontroller import AppController
from model.routecollection import RouteCollection
from view.mainwindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    routes = RouteCollection()
    controller = AppController(routes)
    window = MainWindow(controller)
    window.show()
    sys.exit(app.exec_())
