# Form implementation generated from reading ui file 'ui_zakaz1.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_zakaz(object):
    def setupUi(self, zakaz):
        zakaz.setObjectName("zakaz")
        zakaz.resize(400, 503)
        self.buttonBox = QtWidgets.QDialogButtonBox(zakaz)
        self.buttonBox.setGeometry(QtCore.QRect(220, 380, 151, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.progressBar = QtWidgets.QProgressBar(zakaz)
        self.progressBar.setGeometry(QtCore.QRect(60, 340, 161, 21))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.textEdit_2 = QtWidgets.QTextEdit(zakaz)
        self.textEdit_2.setGeometry(QtCore.QRect(60, 190, 321, 61))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(zakaz)
        self.textEdit_3.setGeometry(QtCore.QRect(60, 260, 321, 61))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label = QtWidgets.QLabel(zakaz)
        self.label.setGeometry(QtCore.QRect(10, 110, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(zakaz)
        self.label_2.setGeometry(QtCore.QRect(10, 210, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(zakaz)
        self.label_3.setGeometry(QtCore.QRect(10, 280, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(zakaz)
        self.textEdit.setGeometry(QtCore.QRect(60, 90, 321, 91))
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(zakaz)
        self.lineEdit.setGeometry(QtCore.QRect(60, 60, 121, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(zakaz)
        self.label_4.setGeometry(QtCore.QRect(70, 40, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(zakaz)
        self.label_5.setGeometry(QtCore.QRect(200, 40, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(zakaz)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 60, 71, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(zakaz)
        self.label_6.setGeometry(QtCore.QRect(300, 40, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(zakaz)
        self.lineEdit_3.setGeometry(QtCore.QRect(290, 60, 91, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(zakaz)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(zakaz)
        self.lineEdit_4.setGeometry(QtCore.QRect(60, 10, 151, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(zakaz)
        self.pushButton.setGeometry(QtCore.QRect(60, 380, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(zakaz)
        self.label_8.setGeometry(QtCore.QRect(230, 10, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.checkBox = QtWidgets.QCheckBox(zakaz)
        self.checkBox.setGeometry(QtCore.QRect(230, 330, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(zakaz)
        self.checkBox_2.setGeometry(QtCore.QRect(230, 350, 141, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(zakaz)
        self.lineEdit_5.setGeometry(QtCore.QRect(270, 10, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.textEdit_4 = QtWidgets.QTextEdit(zakaz)
        self.textEdit_4.setGeometry(QtCore.QRect(160, 420, 221, 71))
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_9 = QtWidgets.QLabel(zakaz)
        self.label_9.setGeometry(QtCore.QRect(70, 430, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(zakaz)
        self.label_10.setGeometry(QtCore.QRect(60, 450, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.retranslateUi(zakaz)
        self.buttonBox.accepted.connect(zakaz.accept)
        self.buttonBox.rejected.connect(zakaz.reject)
        QtCore.QMetaObject.connectSlotsByName(zakaz)

    def retranslateUi(self, zakaz):
        _translate = QtCore.QCoreApplication.translate
        zakaz.setWindowTitle(_translate("zakaz", "Замовлення"))
        self.label.setText(_translate("zakaz", "10x15"))
        self.label_2.setText(_translate("zakaz", "13x20"))
        self.label_3.setText(_translate("zakaz", "20x30"))
        self.label_4.setText(_translate("zakaz", "номер (телефон)"))
        self.label_5.setText(_translate("zakaz", "сад (школа)"))
        self.label_6.setText(_translate("zakaz", "група (клас)"))
        self.label_7.setText(_translate("zakaz", "Ім\'я"))
        self.pushButton.setText(_translate("zakaz", "konovalov.top"))
        self.label_8.setText(_translate("zakaz", "свято"))
        self.checkBox.setText(_translate("zakaz", "відео"))
        self.checkBox_2.setText(_translate("zakaz", "відео в коробці"))
        self.label_9.setText(_translate("zakaz", "примітки"))
        self.label_10.setText(_translate("zakaz", "(якщо потрібно)"))