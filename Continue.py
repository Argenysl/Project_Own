# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Continue.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Continue(object):
    def setupUi(self, Continue):
        Continue.setObjectName("Continue")
        Continue.resize(313, 162)
        Continue.setMinimumSize(QtCore.QSize(313, 162))
        Continue.setMaximumSize(QtCore.QSize(313, 162))
        Continue.setStyleSheet("QWidget#centralwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0.435644, y1:0.767, x2:1, y2:0, stop:0 rgba(20, 19, 5, 255), stop:1 rgba(255, 255, 255, 255))}")
        self.centralwidget = QtWidgets.QWidget(Continue)
        self.centralwidget.setObjectName("centralwidget")
        self.Above_Label = QtWidgets.QLabel(self.centralwidget)
        self.Above_Label.setGeometry(QtCore.QRect(40, 10, 241, 51))
        self.Above_Label.setStyleSheet("font: 9pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);")
        self.Above_Label.setObjectName("Above_Label")
        self.Below_Label = QtWidgets.QLabel(self.centralwidget)
        self.Below_Label.setGeometry(QtCore.QRect(60, 40, 201, 51))
        self.Below_Label.setStyleSheet("font: 9pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);")
        self.Below_Label.setObjectName("Below_Label")
        self.New_Button = QtWidgets.QPushButton(self.centralwidget)
        self.New_Button.setGeometry(QtCore.QRect(200, 100, 81, 51))
        self.New_Button.setObjectName("New_Button")
        self.Exit_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Exit_Button.setGeometry(QtCore.QRect(40, 100, 81, 51))
        self.Exit_Button.setObjectName("Exit_Button")
        Continue.setCentralWidget(self.centralwidget)

        self.retranslateUi(Continue)
        QtCore.QMetaObject.connectSlotsByName(Continue)

    def retranslateUi(self, Continue):
        _translate = QtCore.QCoreApplication.translate
        Continue.setWindowTitle(_translate("Continue", "MainWindow"))
        self.Above_Label.setText(_translate("Continue", "The information has been saved."))
        self.Below_Label.setText(_translate("Continue", "Would you like to continue?"))
        self.New_Button.setText(_translate("Continue", "NEW"))
        self.Exit_Button.setText(_translate("Continue", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Continue = QtWidgets.QMainWindow()
    ui = Ui_Continue()
    ui.setupUi(Continue)
    Continue.show()
    sys.exit(app.exec_())