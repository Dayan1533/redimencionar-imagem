# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtDesign/design.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(711, 541)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("font-weight: 900;\n"
"font-size: 15px")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.btnRedimensionar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRedimensionar.setObjectName("btnRedimensionar")
        self.gridLayout.addWidget(self.btnRedimensionar, 3, 5, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("color: rgb(32, 74, 135);\n"
"font-weight: 700;\n"
"font-size: 10px")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 1, 1, 1)
        self.inputAltura = QtWidgets.QLineEdit(self.centralwidget)
        self.inputAltura.setObjectName("inputAltura")
        self.gridLayout.addWidget(self.inputAltura, 3, 4, 1, 1)
        self.inputLargura = QtWidgets.QLineEdit(self.centralwidget)
        self.inputLargura.setObjectName("inputLargura")
        self.gridLayout.addWidget(self.inputLargura, 3, 1, 1, 1)
        self.btnOriginalImg = QtWidgets.QPushButton(self.centralwidget)
        self.btnOriginalImg.setObjectName("btnOriginalImg")
        self.gridLayout.addWidget(self.btnOriginalImg, 3, 6, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 693, 434))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelImg = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelImg.setText("")
        self.labelImg.setObjectName("labelImg")
        self.gridLayout_2.addWidget(self.labelImg, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 7)
        self.inputAbrirArquivo = QtWidgets.QLineEdit(self.centralwidget)
        self.inputAbrirArquivo.setObjectName("inputAbrirArquivo")
        self.gridLayout.addWidget(self.inputAbrirArquivo, 1, 0, 1, 5)
        self.btnEscolherArquivo = QtWidgets.QPushButton(self.centralwidget)
        self.btnEscolherArquivo.setObjectName("btnEscolherArquivo")
        self.gridLayout.addWidget(self.btnEscolherArquivo, 1, 5, 1, 2)
        self.btnSalvar = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalvar.setStyleSheet("font-weight: 700")
        self.btnSalvar.setObjectName("btnSalvar")
        self.gridLayout.addWidget(self.btnSalvar, 5, 5, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Redimensionar Imagem"))
        self.label_2.setText(_translate("MainWindow", "Altura"))
        self.label.setText(_translate("MainWindow", "Largura"))
        self.label_4.setText(_translate("MainWindow", "  >>>"))
        self.btnRedimensionar.setText(_translate("MainWindow", "Redimensionar"))
        self.label_3.setText(_translate("MainWindow", "Desenvolvido por Dayan Ramos Gomes."))
        self.btnOriginalImg.setText(_translate("MainWindow", "Original"))
        self.btnEscolherArquivo.setText(_translate("MainWindow", "Escolher Arquivo"))
        self.btnSalvar.setText(_translate("MainWindow", "Salvar"))
