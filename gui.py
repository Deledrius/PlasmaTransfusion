#!/usr/bin/env python

# This file is part of PlasmaTransfusion.
#
# PlasmaTransfusion is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PlasmaTransfusion is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PlasmaTransfusion.  If not, see <http://www.gnu.org/licenses/>.


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import uic
import configparser
import logging

import transfusion

class PlasmaTransfusionGUI(QMainWindow):

    def __init__(self, parent=None):
        super(PlasmaTransfusionGUI, self).__init__(parent)
        logging.basicConfig(filename='PlasmaTransfusion.log', level=logging.INFO)
        logging.info("starting")
        uic.loadUi("PlasmaTransfusionGUI.ui",self)
        self.connectEvents()
        self.fillComboBoxVersions()
        self.readSettings()

    def connectEvents(self):
        self.btnInputPath.clicked.connect(self.openAgeFile)
        self.btnOutputPath.clicked.connect(self.setOutputPath)
        self.btnConvertAge.clicked.connect(self.convertAge)

    def fillComboBoxVersions(self):
        userVersionNames = list(transfusion.versionNames.values())
        userVersionNames.remove("Unknown")
        self.cbVersion.clear()
        self.cbVersion.addItems(list(userVersionNames))

    def openAgeFile(self):
        ageFileName = QFileDialog.getOpenFileName(self, "Open Age File", "","Age Files(*.age)")
        inputDir = ageFileName[0].rpartition("/")[0]
        if ageFileName:
            self.txtInputDir.setText(inputDir)

        ageName = ageFileName[0].rpartition("/")[2]
        if ageName:
            self.txtOldAgeName.setText(ageName)


    def setOutputPath(self):
        outputDirectory = QFileDialog.getExistingDirectory(self,"Open Directory")
        if outputDirectory:
            self.txtOutputDir.setText(outputDirectory)

    def convertAge(self):
        self.saveSettings()
        inputDir = str(self.txtInputDir.text())
        oldAgeName = str(self.txtOldAgeName.text())
        outputDir = str(self.txtOutputDir.text())
        newAgeName = str(self.txtNewAgeName.text())
        try:
            newSequencePrefix = int(self.txtNewSequencePrefix.text())
        except:
            newSequencePrefix = None
        version = self.findKeyFromValue(transfusion.versionNames,self.cbVersion.currentText())

        if not newAgeName:
            newAgeName = oldAgeName
        self.setEnabled(False)
        app.processEvents()
        transfusion.doConvert(oldAgeName, inputDir, newAgeName, outputDir, newSequencePrefix, version)
        self.setEnabled(True)

    def findKeyFromValue(self,dictionary,value):
        for key,v in dictionary.items():
            if v == value:
                return key
        return None

    def saveSettings(self):
        config = configparser.ConfigParser()
        config['DEFAULT']['inputDir'] = self.txtInputDir.text()
        config['DEFAULT']['oldAgeName'] = self.txtOldAgeName.text()
        config['DEFAULT']['outputDir'] = self.txtOutputDir.text()
        config['DEFAULT']['newAgeName'] = self.txtNewAgeName.text()
        config['DEFAULT']['newSequencePrefix'] = self.txtNewSequencePrefix.text()
        config['DEFAULT']['version'] = self.cbVersion.currentText()

        with open('lastsession.cfg','w') as configfile:
            config.write(configfile)

    def readSettings(self):
        config = configparser.ConfigParser()
        if len(config.read("lastsession.cfg")) > 0:
            self.txtInputDir.setText(config['DEFAULT']['inputDir'])
            self.txtOldAgeName.setText(config['DEFAULT']['oldAgeName'])
            self.txtOutputDir.setText(config['DEFAULT']['outputDir'])
            self.txtNewAgeName.setText(config['DEFAULT']['newAgeName'])
            self.txtNewSequencePrefix.setText( config['DEFAULT']['newSequencePrefix'])
            index = self.cbVersion.findText(config['DEFAULT']['version'])
            self.cbVersion.setCurrentIndex(index)
            self.btnConvertAge.setFocus()

    def main(self):
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    plasmaTransfusionGUI = PlasmaTransfusionGUI()
    plasmaTransfusionGUI.main()
    app.exec_()
