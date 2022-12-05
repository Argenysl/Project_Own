# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Confirmation.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Confirmation(object):
    def setupUi(self, Confirmation):
        Confirmation.setObjectName("Confirmation")
        Confirmation.resize(313, 162)
        Confirmation.setMinimumSize(QtCore.QSize(313, 162))
        Confirmation.setMaximumSize(QtCore.QSize(313, 162))
        Confirmation.setStyleSheet("QWidget#centralwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0.435644, y1:0.767, x2:1, y2:0, stop:0 rgba(20, 19, 5, 255), stop:1 rgba(255, 255, 255, 255))}")
        self.centralwidget = QtWidgets.QWidget(Confirmation)
        self.centralwidget.setObjectName("centralwidget")
        self.Top_Label = QtWidgets.QLabel(self.centralwidget)
        self.Top_Label.setGeometry(QtCore.QRect(10, 0, 311, 51))
        self.Top_Label.setStyleSheet("font: 14pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);")
        self.Top_Label.setObjectName("Top_Label")
        self.TopBelow_Label = QtWidgets.QLabel(self.centralwidget)
        self.TopBelow_Label.setGeometry(QtCore.QRect(40, 40, 241, 21))
        self.TopBelow_Label.setStyleSheet("font: 8pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);")
        self.TopBelow_Label.setObjectName("TopBelow_Label")
        self.Confirm_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Confirm_Button.setGeometry(QtCore.QRect(190, 90, 81, 51))
        self.Confirm_Button.setObjectName("Confirm_Button")
        self.GoBack_Button = QtWidgets.QPushButton(self.centralwidget)
        self.GoBack_Button.setGeometry(QtCore.QRect(40, 90, 81, 51))
        self.GoBack_Button.setObjectName("GoBack_Button")
        Confirmation.setCentralWidget(self.centralwidget)

        self.retranslateUi(Confirmation)
        QtCore.QMetaObject.connectSlotsByName(Confirmation)

    def retranslateUi(self, Confirmation):
        _translate = QtCore.QCoreApplication.translate
        Confirmation.setWindowTitle(_translate("Confirmation", "MainWindow"))
        self.Top_Label.setText(_translate("Confirmation", "CONFIRM INFORMATION?"))
        self.TopBelow_Label.setText(_translate("Confirmation", "Please double check all information"))
        self.Confirm_Button.setText(_translate("Confirmation", "CONFIRM"))
        self.GoBack_Button.setText(_translate("Confirmation", "GO BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Confirmation = QtWidgets.QMainWindow()
    ui = Ui_Confirmation()
    ui.setupUi(Confirmation)
    Confirmation.show()
    sys.exit(app.exec_())