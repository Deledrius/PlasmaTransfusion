# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlasmaTransfusionGUI.ui'
#
# Created: Sun Aug 18 21:09:28 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PlasmaTransfusionGUI(object):
    def setupUi(self, PlasmaTransfusionGUI):
        PlasmaTransfusionGUI.setObjectName(_fromUtf8("PlasmaTransfusionGUI"))
        PlasmaTransfusionGUI.resize(373, 426)
        self.centralwidget = QtGui.QWidget(PlasmaTransfusionGUI)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 351, 121))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.txtInputDir = QtGui.QLineEdit(self.groupBox)
        self.txtInputDir.setGeometry(QtCore.QRect(10, 40, 231, 20))
        self.txtInputDir.setObjectName(_fromUtf8("txtInputDir"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 79, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.btnInputPath = QtGui.QPushButton(self.groupBox)
        self.btnInputPath.setGeometry(QtCore.QRect(260, 40, 71, 23))
        self.btnInputPath.setObjectName(_fromUtf8("btnInputPath"))
        self.txtOldAgeName = QtGui.QLineEdit(self.groupBox)
        self.txtOldAgeName.setGeometry(QtCore.QRect(10, 90, 231, 20))
        self.txtOldAgeName.setObjectName(_fromUtf8("txtOldAgeName"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btnConvertAge = QtGui.QPushButton(self.centralwidget)
        self.btnConvertAge.setGeometry(QtCore.QRect(125, 370, 121, 23))
        self.btnConvertAge.setObjectName(_fromUtf8("btnConvertAge"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 150, 351, 201))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.txtOutputDir = QtGui.QLineEdit(self.groupBox_2)
        self.txtOutputDir.setGeometry(QtCore.QRect(10, 40, 231, 20))
        self.txtOutputDir.setObjectName(_fromUtf8("txtOutputDir"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.btnOutputPath = QtGui.QPushButton(self.groupBox_2)
        self.btnOutputPath.setGeometry(QtCore.QRect(260, 40, 71, 23))
        self.btnOutputPath.setObjectName(_fromUtf8("btnOutputPath"))
        self.txtNewAgeName = QtGui.QLineEdit(self.groupBox_2)
        self.txtNewAgeName.setGeometry(QtCore.QRect(10, 120, 231, 20))
        self.txtNewAgeName.setObjectName(_fromUtf8("txtNewAgeName"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 129, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.txtNewSequencePrefix = QtGui.QLineEdit(self.groupBox_2)
        self.txtNewSequencePrefix.setGeometry(QtCore.QRect(260, 120, 71, 20))
        self.txtNewSequencePrefix.setObjectName(_fromUtf8("txtNewSequencePrefix"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(260, 80, 81, 41))
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.cbVersion = QtGui.QComboBox(self.groupBox_2)
        self.cbVersion.setGeometry(QtCore.QRect(115, 160, 121, 22))
        self.cbVersion.setObjectName(_fromUtf8("cbVersion"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(30, 160, 82, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        PlasmaTransfusionGUI.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(PlasmaTransfusionGUI)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PlasmaTransfusionGUI.setStatusBar(self.statusbar)

        self.retranslateUi(PlasmaTransfusionGUI)
        QtCore.QMetaObject.connectSlotsByName(PlasmaTransfusionGUI)

    def retranslateUi(self, PlasmaTransfusionGUI):
        PlasmaTransfusionGUI.setWindowTitle(_translate("PlasmaTransfusionGUI", "PlasmaTransfusion", None))
        self.groupBox.setTitle(_translate("PlasmaTransfusionGUI", "Input", None))
        self.label.setText(_translate("PlasmaTransfusionGUI", "Age Directory:", None))
        self.btnInputPath.setText(_translate("PlasmaTransfusionGUI", "Browse...", None))
        self.label_2.setText(_translate("PlasmaTransfusionGUI", "Old Age name:", None))
        self.btnConvertAge.setText(_translate("PlasmaTransfusionGUI", "Convert Age", None))
        self.groupBox_2.setTitle(_translate("PlasmaTransfusionGUI", "Output", None))
        self.label_3.setText(_translate("PlasmaTransfusionGUI", "Directory:", None))
        self.btnOutputPath.setText(_translate("PlasmaTransfusionGUI", "Browse...", None))
        self.label_4.setText(_translate("PlasmaTransfusionGUI", "New Age name (optional):", None))
        self.label_5.setText(_translate("PlasmaTransfusionGUI", "New Sequence prefix (optional):", None))
        self.label_6.setText(_translate("PlasmaTransfusionGUI", "Plasma version:", None))

