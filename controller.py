from PyQt5.QtWidgets import *
from MainWindow import *
import csv


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.setupUi(self)
        self.Enter_button.clicked.connect(self.open_EmployeeInformation)

        from EmployeeInformation import Ui_EmployeeInformation
        self.window = QtWidgets.QMainWindow()
        self.ui_EmployeeInformation = Ui_EmployeeInformation()

        from Confirmation import Ui_Confirmation
        self.window_2 = QtWidgets.QMainWindow()
        self.ui_Confirmation = Ui_Confirmation()

        from Continue import Ui_Continue
        self.window_3 = QtWidgets.QMainWindow()
        self.ui_Continue = Ui_Continue()

    def open_EmployeeInformation(self):
        if self.ID_input.text() == 'UNO' and self.Password_input.text() == 'Omaha.402!':
            self.ui_EmployeeInformation.setupUi(self.window)
            self.window.show()
            self.Error_Label.clear()
            self.ID_input.clear()
            self.Password_input.clear()
            self.ui_EmployeeInformation.SUBMIT.clicked.connect(self.information_check)
            self.ui_EmployeeInformation.SUBMIT_2.clicked.connect(self.exit_window)
        else:
            self.Error_Label.setText('Password or ID is incorrect')

    def information_check(self):
        name = self.ui_EmployeeInformation.FirstName_input.text()
        last_name = self.ui_EmployeeInformation.LastName_Input.text()
        ssn = self.ui_EmployeeInformation.SSN_Input.text()
        amount = self.ui_EmployeeInformation.Amount_Input.text()

        if name == '' or last_name == '' or ssn == '' or amount == '':
            self.ui_EmployeeInformation.FirstName_Error.setText('This information is required')
            self.ui_EmployeeInformation.LastName_Error.setText('This information is required')
            self.ui_EmployeeInformation.DOB_Error.setText('This information is required')
            self.ui_EmployeeInformation.SSN_ERROR.setText('This information is required')
            self.ui_EmployeeInformation.Amount_Error.setText('This information is required')
            self.ui_EmployeeInformation.PayType_Error.setText('This information is required')
        else:
            import csvtester as x
            if x.SSN_Checker(f'{ssn}') is False:
                self.ui_EmployeeInformation.SSN_ERROR.setText('SSN ALREADY REGISTERED')
            else:
                self.ui_Confirmation.setupUi(self.window_2)
                self.window_2.show()
                self.ui_Confirmation.GoBack_Button.clicked.connect(self.exit_window_2)
                self.ui_Confirmation.Confirm_Button.clicked.connect(self.information)

    def information(self):
        name = self.ui_EmployeeInformation.FirstName_input.text()
        middle_name = self.ui_EmployeeInformation.MiddleName_Input.text()
        last_name = self.ui_EmployeeInformation.LastName_Input.text()
        DOB = self.ui_EmployeeInformation.DOB_Input.text()
        SSN = self.ui_EmployeeInformation.SSN_Input.text()
        department = self.ui_EmployeeInformation.Department_Input.currentText()
        title = self.ui_EmployeeInformation.Title_Input.text()

        if self.ui_EmployeeInformation.radioButton.isChecked():
            self.pay_type = 'salary'
        elif self.ui_EmployeeInformation.radioButton_2.isChecked():
            self.pay_type = 'hourly'
        pay_type = self.pay_type
        amount = self.ui_EmployeeInformation.Amount_Input.text()
        with open('information.csv', 'a', newline='') as csvfile:
            info = csv.writer(csvfile)
            data = (
            f'{name}', f'{middle_name}', f'{last_name}', f'{DOB}', f'{SSN}', f'{department}', f'{title}', f'{pay_type}', f'{amount}')
            info.writerow(data)
        self.ui_Continue.setupUi(self.window_3)
        self.window_3.show()
        self.ui_Continue.Exit_Button.clicked.connect(self.exit_program)
        self.ui_Continue.New_Button.clicked.connect(self.new)

    def new(self):
        self.window_3.close()
        self.window_2.close()
        self.window.close()
        self.Error_Label.setText("Enter Credentials to Continue")

    def exit_window(self):
        self.window.close()

    def exit_window_2(self):
        self.window_2.close()

    def exit_program(self):
        self.window.close()
        self.window_2.close()
        self.window_3.close()
        self.close()
