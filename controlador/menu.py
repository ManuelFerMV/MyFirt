# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(757, 510)
        self.btnProcesar = QtWidgets.QPushButton(Form)
        self.btnProcesar.setGeometry(QtCore.QRect(170, 150, 62, 19))
        self.btnProcesar.setObjectName("btnProcesar")
        self.txtExpresion = QtWidgets.QLineEdit(Form)
        self.txtExpresion.setGeometry(QtCore.QRect(160, 40, 531, 61))
        self.txtExpresion.setObjectName("txtExpresion")
        self.txtRespuesta = QtWidgets.QTextEdit(Form)
        self.txtRespuesta.setGeometry(QtCore.QRect(70, 223, 581, 231))
        self.txtRespuesta.setObjectName("txtRespuesta")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnProcesar.setText(_translate("Form", "PushButton"))