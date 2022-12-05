# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EmployeeInformation.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EmployeeInformation(object):
    def setupUi(self, EmployeeInformation):
        EmployeeInformation.setObjectName("EmployeeInformation")
        EmployeeInformation.resize(872, 511)
        EmployeeInformation.setMinimumSize(QtCore.QSize(872, 511))
        EmployeeInformation.setMaximumSize(QtCore.QSize(872, 511))
        EmployeeInformation.setStyleSheet("QWidget#centralwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0.435644, y1:0.767, x2:1, y2:0, stop:0 rgba(69, 20, 68, 255), stop:1 rgba(255, 255, 255, 255))}")
        self.centralwidget = QtWidgets.QWidget(EmployeeInformation)
        self.centralwidget.setObjectName("centralwidget")
        self.FirstName_Label = QtWidgets.QLabel(self.centralwidget)
        self.FirstName_Label.setGeometry(QtCore.QRect(10, 90, 111, 20))
        self.FirstName_Label.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);")
        self.FirstName_Label.setObjectName("FirstName_Label")
        self.LastName_Label = QtWidgets.QLabel(self.centralwidget)
        self.LastName_Label.setGeometry(QtCore.QRect(10, 230, 101, 20))
        self.LastName_Label.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);")
        self.LastName_Label.setObjectName("LastName_Label")
        self.MiddleName_Label = QtWidgets.QLabel(self.centralwidget)
        self.MiddleName_Label.setGeometry(QtCore.QRect(10, 160, 461, 20))
        self.MiddleName_Label.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);")
        self.MiddleName_Label.setObjectName("MiddleName_Label")
        self.DOB_Label = QtWidgets.QLabel(self.centralwidget)
        self.DOB_Label.setGeometry(QtCore.QRect(10, 300, 121, 20))
        self.DOB_Label.setStyleSheet("font: 9pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);")
        self.DOB_Label.setObjectName("DOB_Label")
        self.StoreInformation_Label = QtWidgets.QLabel(self.centralwidget)
        self.StoreInformation_Label.setGeometry(QtCore.QRect(560, 29, 211, 31))
        self.StoreInformation_Label.setStyleSheet("font: 14pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);")
        self.StoreInformation_Label.setObjectName("StoreInformation_Label")
        self.SSN_Label = QtWidgets.QLabel(self.centralwidget)
        self.SSN_Label.setGeometry(QtCore.QRect(10, 370, 81, 20))
        self.SSN_Label.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);")
        self.SSN_Label.setObjectName("SSN_Label")
        self.PersonalInformation_Label = QtWidgets.QLabel(self.centralwidget)
        self.PersonalInformation_Label.setGeometry(QtCore.QRect(120, 30, 241, 20))
        self.PersonalInformation_Label.setStyleSheet("font: 14pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);")
        self.PersonalInformation_Label.setObjectName("PersonalInformation_Label")
        self.FirstName_input = QtWidgets.QLineEdit(self.centralwidget)
        self.FirstName_input.setGeometry(QtCore.QRect(130, 90, 221, 22))
        self.FirstName_input.setObjectName("FirstName_input")
        self.MiddleName_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.MiddleName_Input.setGeometry(QtCore.QRect(130, 160, 221, 22))
        self.MiddleName_Input.setObjectName("MiddleName_Input")
        self.LastName_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.LastName_Input.setGeometry(QtCore.QRect(130, 230, 221, 22))
        self.LastName_Input.setObjectName("LastName_Input")
        self.SSN_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.SSN_Input.setGeometry(QtCore.QRect(130, 370, 221, 22))
        self.SSN_Input.setText("")
        self.SSN_Input.setObjectName("SSN_Input")
        self.DOB_Input = QtWidgets.QDateEdit(self.centralwidget)
        self.DOB_Input.setGeometry(QtCore.QRect(130, 300, 91, 22))
        self.DOB_Input.setReadOnly(False)
        self.DOB_Input.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.DOB_Input.setObjectName("DOB_Input")
        self.Department_Input = QtWidgets.QComboBox(self.centralwidget)
        self.Department_Input.setGeometry(QtCore.QRect(620, 90, 151, 22))
        self.Department_Input.setObjectName("Department_Input")
        self.Department_Input.addItem("")
        self.Department_Input.addItem("")
        self.Department_Input.addItem("")
        self.Department_Input.addItem("")
        self.Department_Input.addItem("")
        self.Department_Input.addItem("")
        self.Department_Input.addItem("")
        self.Department_Label = QtWidgets.QLabel(self.centralwidget)
        self.Department_Label.setGeometry(QtCore.QRect(490, 90, 121, 20))
        self.Department_Label.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);")
        self.Department_Label.setObjectName("Department_Label")
        self.Title_Label = QtWidgets.QLabel(self.centralwidget)
        self.Title_Label.setGeometry(QtCore.QRect(490, 170, 121, 16))
        self.Title_Label.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);")
        self.Title_Label.setObjectName("Title_Label")
        self.Title_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.Title_Input.setGeometry(QtCore.QRect(620, 170, 151, 22))
        self.Title_Input.setObjectName("Title_Input")
        self.PayInformation_Label = QtWidgets.QLabel(self.centralwidget)
        self.PayInformation_Label.setGeometry(QtCore.QRect(560, 220, 181, 31))
        self.PayInformation_Label.setStyleSheet("font: 14pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);")
        self.PayInformation_Label.setObjectName("PayInformation_Label")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(630, 260, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(520, 260, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.Amount_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.Amount_Input.setGeometry(QtCore.QRect(620, 310, 151, 22))
        self.Amount_Input.setObjectName("Amount_Input")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(490, 310, 81, 16))
        self.label_11.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.SUBMIT = QtWidgets.QPushButton(self.centralwidget)
        self.SUBMIT.setGeometry(QtCore.QRect(660, 360, 111, 41))
        self.SUBMIT.setObjectName("SUBMIT")
        self.FirstName_Error = QtWidgets.QLabel(self.centralwidget)
        self.FirstName_Error.setGeometry(QtCore.QRect(100, 120, 251, 16))
        self.FirstName_Error.setStyleSheet("color: rgb(255, 0, 4);\n"
"font: 11pt \"Arial Rounded MT Bold\";")
        self.FirstName_Error.setText("")
        self.FirstName_Error.setObjectName("FirstName_Error")
        self.LastName_Error = QtWidgets.QLabel(self.centralwidget)
        self.LastName_Error.setGeometry(QtCore.QRect(100, 260, 251, 16))
        self.LastName_Error.setStyleSheet("color: rgb(255, 0, 4);\n"
"font: 11pt \"Arial Rounded MT Bold\";")
        self.LastName_Error.setText("")
        self.LastName_Error.setObjectName("LastName_Error")
        self.DOB_Error = QtWidgets.QLabel(self.centralwidget)
        self.DOB_Error.setGeometry(QtCore.QRect(100, 330, 251, 16))
        self.DOB_Error.setStyleSheet("color: rgb(255, 0, 4);\n"
"font: 11pt \"Arial Rounded MT Bold\";")
        self.DOB_Error.setText("")
        self.DOB_Error.setObjectName("DOB_Error")
        self.SSN_ERROR = QtWidgets.QLabel(self.centralwidget)
        self.SSN_ERROR.setGeometry(QtCore.QRect(100, 410, 251, 16))
        self.SSN_ERROR.setStyleSheet("color: rgb(255, 0, 4);\n"
"font: 11pt \"Arial Rounded MT Bold\";")
        self.SSN_ERROR.setText("")
        self.SSN_ERROR.setObjectName("SSN_ERROR")
        self.Amount_Error = QtWidgets.QLabel(self.centralwidget)
        self.Amount_Error.setGeometry(QtCore.QRect(490, 340, 251, 16))
        self.Amount_Error.setStyleSheet("color: rgb(255, 0, 4);\n"
"font: 11pt \"Arial Rounded MT Bold\";")
        self.Amount_Error.setText("")
        self.Amount_Error.setObjectName("Amount_Error")
        self.PayType_Error = QtWidgets.QLabel(self.centralwidget)
        self.PayType_Error.setGeometry(QtCore.QRect(490, 280, 251, 16))
        self.PayType_Error.setStyleSheet("color: rgb(255, 0, 4);\n"
"font: 11pt \"Arial Rounded MT Bold\";")
        self.PayType_Error.setText("")
        self.PayType_Error.setObjectName("PayType_Error")
        self.SUBMIT_2 = QtWidgets.QPushButton(self.centralwidget)
        self.SUBMIT_2.setGeometry(QtCore.QRect(510, 360, 111, 41))
        self.SUBMIT_2.setObjectName("SUBMIT_2")
        EmployeeInformation.setCentralWidget(self.centralwidget)

        self.retranslateUi(EmployeeInformation)
        QtCore.QMetaObject.connectSlotsByName(EmployeeInformation)

    def retranslateUi(self, EmployeeInformation):
        _translate = QtCore.QCoreApplication.translate
        EmployeeInformation.setWindowTitle(_translate("EmployeeInformation", "Employee Information"))
        self.FirstName_Label.setText(_translate("EmployeeInformation", "First Name:"))
        self.LastName_Label.setText(_translate("EmployeeInformation", "Last Name:"))
        self.MiddleName_Label.setText(_translate("EmployeeInformation", "Middle Name:                                                          (if applicable)"))
        self.DOB_Label.setText(_translate("EmployeeInformation", "DOB(m/d/yyyy):"))
        self.StoreInformation_Label.setText(_translate("EmployeeInformation", "Store Information"))
        self.SSN_Label.setText(_translate("EmployeeInformation", "SSN:"))
        self.PersonalInformation_Label.setText(_translate("EmployeeInformation", "Personal Information"))
        self.Department_Input.setItemText(0, _translate("EmployeeInformation", "Select"))
        self.Department_Input.setItemText(1, _translate("EmployeeInformation", "Grocery"))
        self.Department_Input.setItemText(2, _translate("EmployeeInformation", "Pharmacy"))
        self.Department_Input.setItemText(3, _translate("EmployeeInformation", "Bakery"))
        self.Department_Input.setItemText(4, _translate("EmployeeInformation", "Costumer Service"))
        self.Department_Input.setItemText(5, _translate("EmployeeInformation", "Front End"))
        self.Department_Input.setItemText(6, _translate("EmployeeInformation", "Warehouse"))
        self.Department_Label.setText(_translate("EmployeeInformation", "Department:"))
        self.Title_Label.setText(_translate("EmployeeInformation", "Position/Title:"))
        self.PayInformation_Label.setText(_translate("EmployeeInformation", "Pay Information"))
        self.radioButton.setText(_translate("EmployeeInformation", "Salary"))
        self.radioButton_2.setText(_translate("EmployeeInformation", "Hourly"))
        self.label_11.setText(_translate("EmployeeInformation", "Amount:"))
        self.SUBMIT.setText(_translate("EmployeeInformation", "SUBMIT"))
        self.SUBMIT_2.setText(_translate("EmployeeInformation", "CANCEL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EmployeeInformation = QtWidgets.QMainWindow()
    ui = Ui_EmployeeInformation()
    ui.setupUi(EmployeeInformation)
    EmployeeInformation.show()
    sys.exit(app.exec_())
