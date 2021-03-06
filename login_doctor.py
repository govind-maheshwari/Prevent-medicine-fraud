# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_doctor.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_doctor(object):
    
    def submitCheck(self):
        username = self.u_name_lineEdit.text()
        password = self.password_lineEdit.text()
        patient_name = self.p_name_lineEdit.text()
        patient_age = self.p_age_lineEdit.text()
        patient_gender = self.p_gender_lineEdit.text()
        patient_aadhar = self.p_aadhar_lineEdit.text()
        medicine = self.medicine_textEdit.toPlainText()
        doctor_name = self.d_name_lineEdit.text()
        status = 'True'
        shopkeeper = 'null'
        code = 123456
        connection = sqlite3.connect("govind.db")
        result = connection.execute("SELECT * FROM DOCTOR WHERE USERNAME = ? AND PASSWORD = ?",(username,password))
        #print (result)
        if (len(result.fetchall())>0):
            connection.execute("INSERT INTO PATIENT VALUES(?,?,?,?,?,?,?,?,?)",(patient_name,patient_age,patient_gender,patient_aadhar,medicine,doctor_name,status,shopkeeper,code))
            connection.commit()
            print("Form submitted!!")
        else:
            print("WRONG CREDENTIALS!!")
        connection.close()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(185, 228, 194, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(49, 59, 571, 381))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.p_name_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.p_name_lineEdit.setObjectName("p_name_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.p_name_lineEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.p_age_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.p_age_lineEdit.setObjectName("p_age_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.p_age_lineEdit)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.p_gender_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.p_gender_lineEdit.setObjectName("p_gender_lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.p_gender_lineEdit)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.p_aadhar_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.p_aadhar_lineEdit.setObjectName("p_aadhar_lineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.p_aadhar_lineEdit)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.d_name_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.d_name_lineEdit.setObjectName("d_name_lineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.d_name_lineEdit)
        self.u_name_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.u_name_lineEdit.setObjectName("u_name_lineEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.u_name_lineEdit)
        self.password_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.password_lineEdit)
        self.medicine_textEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.medicine_textEdit.setObjectName("medicine_textEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.medicine_textEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 470, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        #####################Event###################
        self.pushButton.clicked.connect(self.submitCheck)
        #############################################
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Patient\'s Name"))
        self.label_2.setText(_translate("MainWindow", "Patient\'s Age"))
        self.label_3.setText(_translate("MainWindow", "Patient\'s Gender"))
        self.label_4.setText(_translate("MainWindow", "Patient\'s Aadhar"))
        self.label_5.setText(_translate("MainWindow", "Medicines"))
        self.label_6.setText(_translate("MainWindow", "Doctor\'s Name"))
        self.label_7.setText(_translate("MainWindow", "Username"))
        self.label_8.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "SUBMIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_doctor()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
