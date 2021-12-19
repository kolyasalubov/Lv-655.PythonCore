# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 256)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(0, 0, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(15)
        self.result.setFont(font)
        self.result.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result.setStyleSheet("background-color: rgb(70, 181, 255);")
        self.result.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Ukraine))
        self.result.setFrameShadow(QtWidgets.QFrame.Plain)
        self.result.setMidLineWidth(0)
        self.result.setText("")
        self.result.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.result.setObjectName("result")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(0, 50, 60, 50))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btn_plus.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Ukraine))
        self.btn_plus.setObjectName("btn_plus")
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(60, 50, 60, 50))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_minus.setFont(font)
        self.btn_minus.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btn_minus.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Ukraine))
        self.btn_minus.setObjectName("btn_minus")
        self.btn_mul = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mul.setGeometry(QtCore.QRect(120, 50, 60, 50))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_mul.setFont(font)
        self.btn_mul.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btn_mul.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Ukraine))
        self.btn_mul.setObjectName("btn_mul")
        self.btn_div = QtWidgets.QPushButton(self.centralwidget)
        self.btn_div.setGeometry(QtCore.QRect(180, 50, 60, 50))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_div.setFont(font)
        self.btn_div.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btn_div.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Ukraine))
        self.btn_div.setObjectName("btn_div")
        self.btn_ac = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ac.setGeometry(QtCore.QRect(240, 50, 60, 50))
        self.btn_backspace = QtWidgets.QPushButton(self.centralwidget)
        self.btn_backspace.setGeometry(QtCore.QRect(240, 100, 60, 50))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_ac.setFont(font)
        self.btn_ac.setStyleSheet("background-color: rgb(255, 62, 62);")
        self.btn_ac.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Ukraine))
        self.btn_ac.setObjectName("btn_ac")
        self.btn_backspace.setFont(font)
        self.btn_backspace.setStyleSheet("background-color: rgb(200, 62, 62);")
        self.btn_backspace.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Ukraine))
        self.btn_backspace.setObjectName("btn_backspace")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 100, 60, 50))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.btn_1.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Ukraine))
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(60, 100, 60, 50))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.btn_2.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Ukraine))
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(120, 100, 60, 50))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.btn_3.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Ukraine))
        self.btn_3.setObjectName("btn_3")
        self.btn_kvadrat = QtWidgets.QPushButton(self.centralwidget)
        self.btn_kvadrat.setGeometry(QtCore.QRect(180, 100, 60, 50))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_kvadrat.setFont(font)
        self.btn_kvadrat.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btn_kvadrat.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Ukraine))
        self.btn_kvadrat.setObjectName("btn_kvadrat")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(60, 150, 60, 50))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.btn_5.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Ukraine))
        self.btn_5.setObjectName("btn_5")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(180, 200, 60, 50))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.btn_0.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Ukraine))
        self.btn_0.setObjectName("btn_0")
        self.btn_div0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_div0.setGeometry(QtCore.QRect(180, 150, 60, 50))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_div0.setFont(font)
        self.btn_div0.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.btn_div0.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Ukraine))
        self.btn_div0.setObjectName("btn_div0")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(120, 150, 60, 50))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.btn_6.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Ukraine))
        self.btn_6.setObjectName("btn_6")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 150, 60, 50))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.btn_4.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Ukraine))
        self.btn_4.setObjectName("btn_4")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 200, 60, 50))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.btn_7.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Ukraine))
        self.btn_7.setObjectName("btn_7")
        self.btn_equel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equel.setGeometry(QtCore.QRect(240, 150, 60, 100))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_equel.setFont(font)
        self.btn_equel.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.btn_equel.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Ukraine))
        self.btn_equel.setObjectName("btn_equel")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(120, 200, 60, 50))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.btn_9.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Ukraine))
        self.btn_9.setObjectName("btn_9")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(60, 200, 60, 50))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.btn_8.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Ukraine))
        self.btn_8.setObjectName("btn_8")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_func()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_mul.setText(_translate("MainWindow", "*"))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn_ac.setText(_translate("MainWindow", "AC"))
        self.btn_backspace.setText(_translate("MainWindow", "bspace"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_kvadrat.setText(_translate("MainWindow", "**"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_div0.setText(_translate("MainWindow", f"%div"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_equel.setText(_translate("MainWindow", "="))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_8.setText(_translate("MainWindow", "8"))
    
    def add_func(self):
        self.btn_0.clicked.connect(lambda: self.write_number(self.btn_0.text()))
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
        self.btn_plus.clicked.connect(lambda: self.write_number(self.btn_plus.text()))
        self.btn_minus.clicked.connect(lambda: self.write_number(self.btn_minus.text()))
        self.btn_mul.clicked.connect(lambda: self.write_number(self.btn_mul.text()))
        self.btn_div.clicked.connect(lambda: self.write_number(self.btn_div.text()))
        self.btn_kvadrat.clicked.connect(lambda: self.write_number(self.btn_kvadrat.text()))
        self.btn_div0.clicked.connect(lambda: self.write_number("%"))
        
        self.btn_ac.clicked.connect(self.ac)
        self.btn_backspace.clicked.connect(self.backspace)
        self.btn_equel.clicked.connect(self.equel)
    

    def write_number(self, number):
        if self.result.text() == "0":
            self.result.setText(number)
        else:
            self.result.setText(self.result.text() + number)

    def equel(self):
        try:
            res = eval(self.result.text())
            self.result.setNum(res)
        except ZeroDivisionError as e:
            self.result.setText("")
            print(e)
        except SyntaxError as e:
            self.result.setText("")
            print(e)
    
    def ac(self):
        self.result.setText("")
    
    def backspace(self):
        back = self.result.text()
        b = str(back)[0:-1]
        self.result.setText(b)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
