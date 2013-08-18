# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlasmaTransfusionGUI.ui'
#
# Created: Sun Aug 18 17:15:09 2013
#      by: PyQt5 UI code generator 5.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PlasmaTransfusionGUI(object):
    def setupUi(self, PlasmaTransfusionGUI):
        PlasmaTransfusionGUI.setObjectName("PlasmaTransfusionGUI")
        PlasmaTransfusionGUI.resize(373, 426)
        self.centralwidget = QtWidgets.QWidget(PlasmaTransfusionGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 351, 121))
        self.groupBox.setObjectName("groupBox")
        self.txtInputDir = QtWidgets.QLineEdit(self.groupBox)
        self.txtInputDir.setGeometry(QtCore.QRect(10, 40, 231, 20))
        self.txtInputDir.setObjectName("txtInputDir")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 79, 16))
        self.label.setObjectName("label")
        self.btnInputPath = QtWidgets.QPushButton(self.groupBox)
        self.btnInputPath.setGeometry(QtCore.QRect(260, 40, 71, 23))
        self.btnInputPath.setObjectName("btnInputPath")
        self.txtOldAgeName = QtWidgets.QLineEdit(self.groupBox)
        self.txtOldAgeName.setGeometry(QtCore.QRect(10, 90, 231, 20))
        self.txtOldAgeName.setObjectName("txtOldAgeName")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.label_2.setObjectName("label_2")
        self.btnConvertAge = QtWidgets.QPushButton(self.centralwidget)
        self.btnConvertAge.setGeometry(QtCore.QRect(125, 370, 121, 23))
        self.btnConvertAge.setObjectName("btnConvertAge")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 150, 351, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.txtOutputDir = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtOutputDir.setGeometry(QtCore.QRect(10, 40, 231, 20))
        self.txtOutputDir.setObjectName("txtOutputDir")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label_3.setObjectName("label_3")
        self.btnOutputPath = QtWidgets.QPushButton(self.groupBox_2)
        self.btnOutputPath.setGeometry(QtCore.QRect(260, 40, 71, 23))
        self.btnOutputPath.setObjectName("btnOutputPath")
        self.txtNewAgeName = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtNewAgeName.setGeometry(QtCore.QRect(10, 120, 231, 20))
        self.txtNewAgeName.setObjectName("txtNewAgeName")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 129, 16))
        self.label_4.setObjectName("label_4")
        self.txtNewSequencePrefix = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtNewSequencePrefix.setGeometry(QtCore.QRect(260, 120, 71, 20))
        self.txtNewSequencePrefix.setObjectName("txtNewSequencePrefix")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(260, 80, 81, 41))
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.cbVersion = QtWidgets.QComboBox(self.groupBox_2)
        self.cbVersion.setGeometry(QtCore.QRect(115, 160, 121, 22))
        self.cbVersion.setObjectName("cbVersion")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(30, 160, 82, 16))
        self.label_6.setObjectName("label_6")
        PlasmaTransfusionGUI.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PlasmaTransfusionGUI)
        self.statusbar.setObjectName("statusbar")
        PlasmaTransfusionGUI.setStatusBar(self.statusbar)

        self.retranslateUi(PlasmaTransfusionGUI)
        QtCore.QMetaObject.connectSlotsByName(PlasmaTransfusionGUI)

    def retranslateUi(self, PlasmaTransfusionGUI):
        _translate = QtCore.QCoreApplication.translate
        PlasmaTransfusionGUI.setWindowTitle(_translate("PlasmaTransfusionGUI", "PlasmaTransfusion"))
        self.groupBox.setTitle(_translate("PlasmaTransfusionGUI", "Input"))
        self.label.setText(_translate("PlasmaTransfusionGUI", "Age Directory:"))
        self.btnInputPath.setText(_translate("PlasmaTransfusionGUI", "Browse..."))
        self.label_2.setText(_translate("PlasmaTransfusionGUI", "Old Age name:"))
        self.btnConvertAge.setText(_translate("PlasmaTransfusionGUI", "Convert Age"))
        self.groupBox_2.setTitle(_translate("PlasmaTransfusionGUI", "Output"))
        self.label_3.setText(_translate("PlasmaTransfusionGUI", "Directory:"))
        self.btnOutputPath.setText(_translate("PlasmaTransfusionGUI", "Browse..."))
        self.label_4.setText(_translate("PlasmaTransfusionGUI", "New Age name (optional):"))
        self.label_5.setText(_translate("PlasmaTransfusionGUI", "New Sequence prefix (optional):"))
        self.label_6.setText(_translate("PlasmaTransfusionGUI", "Plasma version:"))

