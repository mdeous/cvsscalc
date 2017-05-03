# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1115, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1115, 720))
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.toolBox.setFont(font)
        self.toolBox.setObjectName("toolBox")
        self.baseScorePage = QtWidgets.QWidget()
        self.baseScorePage.setGeometry(QtCore.QRect(0, 0, 1097, 575))
        self.baseScorePage.setObjectName("baseScorePage")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.baseScorePage)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.baseScoreLabel = QtWidgets.QLabel(self.baseScorePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.baseScoreLabel.sizePolicy().hasHeightForWidth())
        self.baseScoreLabel.setSizePolicy(sizePolicy)
        self.baseScoreLabel.setTextFormat(QtCore.Qt.RichText)
        self.baseScoreLabel.setScaledContents(False)
        self.baseScoreLabel.setObjectName("baseScoreLabel")
        self.verticalLayout_9.addWidget(self.baseScoreLabel)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.avGroupBox = QtWidgets.QGroupBox(self.baseScorePage)
        self.avGroupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    margin-top: 0.5em;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.avGroupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.avGroupBox.setFlat(False)
        self.avGroupBox.setObjectName("avGroupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.avGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.avnPushButton = QtWidgets.QPushButton(self.avGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.avnPushButton.sizePolicy().hasHeightForWidth())
        self.avnPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.avnPushButton.setFont(font)
        self.avnPushButton.setStatusTip("")
        self.avnPushButton.setCheckable(True)
        self.avnPushButton.setAutoExclusive(True)
        self.avnPushButton.setFlat(False)
        self.avnPushButton.setObjectName("avnPushButton")
        self.horizontalLayout.addWidget(self.avnPushButton)
        self.avaPushButton = QtWidgets.QPushButton(self.avGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.avaPushButton.sizePolicy().hasHeightForWidth())
        self.avaPushButton.setSizePolicy(sizePolicy)
        self.avaPushButton.setStatusTip("")
        self.avaPushButton.setCheckable(True)
        self.avaPushButton.setAutoExclusive(True)
        self.avaPushButton.setObjectName("avaPushButton")
        self.horizontalLayout.addWidget(self.avaPushButton)
        self.avlPushButton = QtWidgets.QPushButton(self.avGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.avlPushButton.sizePolicy().hasHeightForWidth())
        self.avlPushButton.setSizePolicy(sizePolicy)
        self.avlPushButton.setStatusTip("")
        self.avlPushButton.setCheckable(True)
        self.avlPushButton.setAutoExclusive(True)
        self.avlPushButton.setObjectName("avlPushButton")
        self.horizontalLayout.addWidget(self.avlPushButton)
        self.avpPushButton = QtWidgets.QPushButton(self.avGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.avpPushButton.sizePolicy().hasHeightForWidth())
        self.avpPushButton.setSizePolicy(sizePolicy)
        self.avpPushButton.setStatusTip("")
        self.avpPushButton.setCheckable(True)
        self.avpPushButton.setAutoExclusive(True)
        self.avpPushButton.setObjectName("avpPushButton")
        self.horizontalLayout.addWidget(self.avpPushButton)
        self.verticalLayout_2.addWidget(self.avGroupBox)
        self.acGroupBox = QtWidgets.QGroupBox(self.baseScorePage)
        self.acGroupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    margin-top: 0.5em;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.acGroupBox.setObjectName("acGroupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.acGroupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.aclPushButton = QtWidgets.QPushButton(self.acGroupBox)
        self.aclPushButton.setStatusTip("")
        self.aclPushButton.setCheckable(True)
        self.aclPushButton.setAutoExclusive(True)
        self.aclPushButton.setObjectName("aclPushButton")
        self.horizontalLayout_4.addWidget(self.aclPushButton)
        self.achPushButton = QtWidgets.QPushButton(self.acGroupBox)
        self.achPushButton.setStatusTip("")
        self.achPushButton.setCheckable(True)
        self.achPushButton.setAutoExclusive(True)
        self.achPushButton.setObjectName("achPushButton")
        self.horizontalLayout_4.addWidget(self.achPushButton)
        self.verticalLayout_2.addWidget(self.acGroupBox)
        self.prGroupBox = QtWidgets.QGroupBox(self.baseScorePage)
        self.prGroupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    margin-top: 0.5em;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.prGroupBox.setObjectName("prGroupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.prGroupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.prnPushButton = QtWidgets.QPushButton(self.prGroupBox)
        self.prnPushButton.setStatusTip("")
        self.prnPushButton.setCheckable(True)
        self.prnPushButton.setAutoExclusive(True)
        self.prnPushButton.setObjectName("prnPushButton")
        self.horizontalLayout_5.addWidget(self.prnPushButton)
        self.prlPutton = QtWidgets.QPushButton(self.prGroupBox)
        self.prlPutton.setStatusTip("")
        self.prlPutton.setCheckable(True)
        self.prlPutton.setAutoExclusive(True)
        self.prlPutton.setObjectName("prlPutton")
        self.horizontalLayout_5.addWidget(self.prlPutton)
        self.prhPushButton = QtWidgets.QPushButton(self.prGroupBox)
        self.prhPushButton.setStatusTip("")
        self.prhPushButton.setCheckable(True)
        self.prhPushButton.setAutoExclusive(True)
        self.prhPushButton.setObjectName("prhPushButton")
        self.horizontalLayout_5.addWidget(self.prhPushButton)
        self.verticalLayout_2.addWidget(self.prGroupBox)
        self.uiGroupBox = QtWidgets.QGroupBox(self.baseScorePage)
        self.uiGroupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    margin-top: 0.5em;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.uiGroupBox.setObjectName("uiGroupBox")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.uiGroupBox)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.uinPushButton = QtWidgets.QPushButton(self.uiGroupBox)
        self.uinPushButton.setStatusTip("")
        self.uinPushButton.setCheckable(True)
        self.uinPushButton.setAutoExclusive(True)
        self.uinPushButton.setObjectName("uinPushButton")
        self.horizontalLayout_6.addWidget(self.uinPushButton)
        self.uirPushButton = QtWidgets.QPushButton(self.uiGroupBox)
        self.uirPushButton.setStatusTip("")
        self.uirPushButton.setCheckable(True)
        self.uirPushButton.setAutoExclusive(True)
        self.uirPushButton.setObjectName("uirPushButton")
        self.horizontalLayout_6.addWidget(self.uirPushButton)
        self.verticalLayout_2.addWidget(self.uiGroupBox)
        self.horizontalLayout_26.addLayout(self.verticalLayout_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.sGroupBox = QtWidgets.QGroupBox(self.baseScorePage)
        self.sGroupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    margin-top: 0.5em;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.sGroupBox.setFlat(True)
        self.sGroupBox.setCheckable(False)
        self.sGroupBox.setChecked(False)
        self.sGroupBox.setObjectName("sGroupBox")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.sGroupBox)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.suPushButton = QtWidgets.QPushButton(self.sGroupBox)
        self.suPushButton.setCheckable(True)
        self.suPushButton.setAutoExclusive(True)
        self.suPushButton.setObjectName("suPushButton")
        self.horizontalLayout_7.addWidget(self.suPushButton)
        self.scPushButton = QtWidgets.QPushButton(self.sGroupBox)
        self.scPushButton.setCheckable(True)
        self.scPushButton.setAutoExclusive(True)
        self.scPushButton.setObjectName("scPushButton")
        self.horizontalLayout_7.addWidget(self.scPushButton)
        self.verticalLayout_6.addWidget(self.sGroupBox)
        self.cGroupBox = QtWidgets.QGroupBox(self.baseScorePage)
        self.cGroupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    margin-top: 0.5em;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.cGroupBox.setObjectName("cGroupBox")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.cGroupBox)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.cnPushButton = QtWidgets.QPushButton(self.cGroupBox)
        self.cnPushButton.setCheckable(True)
        self.cnPushButton.setAutoExclusive(True)
        self.cnPushButton.setObjectName("cnPushButton")
        self.horizontalLayout_8.addWidget(self.cnPushButton)
        self.clPushButton = QtWidgets.QPushButton(self.cGroupBox)
        self.clPushButton.setCheckable(True)
        self.clPushButton.setAutoExclusive(True)
        self.clPushButton.setObjectName("clPushButton")
        self.horizontalLayout_8.addWidget(self.clPushButton)
        self.chPushButton = QtWidgets.QPushButton(self.cGroupBox)
        self.chPushButton.setCheckable(True)
        self.chPushButton.setAutoExclusive(True)
        self.chPushButton.setObjectName("chPushButton")
        self.horizontalLayout_8.addWidget(self.chPushButton)
        self.verticalLayout_6.addWidget(self.cGroupBox)
        self.iGroupBox = QtWidgets.QGroupBox(self.baseScorePage)
        self.iGroupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    margin-top: 0.5em;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.iGroupBox.setObjectName("iGroupBox")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.iGroupBox)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.inPushButton = QtWidgets.QPushButton(self.iGroupBox)
        self.inPushButton.setCheckable(True)
        self.inPushButton.setAutoExclusive(True)
        self.inPushButton.setObjectName("inPushButton")
        self.horizontalLayout_9.addWidget(self.inPushButton)
        self.ilPushButton = QtWidgets.QPushButton(self.iGroupBox)
        self.ilPushButton.setCheckable(True)
        self.ilPushButton.setAutoExclusive(True)
        self.ilPushButton.setObjectName("ilPushButton")
        self.horizontalLayout_9.addWidget(self.ilPushButton)
        self.ihPushButton = QtWidgets.QPushButton(self.iGroupBox)
        self.ihPushButton.setCheckable(True)
        self.ihPushButton.setAutoExclusive(True)
        self.ihPushButton.setObjectName("ihPushButton")
        self.horizontalLayout_9.addWidget(self.ihPushButton)
        self.verticalLayout_6.addWidget(self.iGroupBox)
        self.aGroupBox = QtWidgets.QGroupBox(self.baseScorePage)
        self.aGroupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    margin-top: 0.5em;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.aGroupBox.setObjectName("aGroupBox")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.aGroupBox)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.anPushButton = QtWidgets.QPushButton(self.aGroupBox)
        self.anPushButton.setCheckable(True)
        self.anPushButton.setAutoExclusive(True)
        self.anPushButton.setObjectName("anPushButton")
        self.horizontalLayout_10.addWidget(self.anPushButton)
        self.alPushButton = QtWidgets.QPushButton(self.aGroupBox)
        self.alPushButton.setCheckable(True)
        self.alPushButton.setAutoExclusive(True)
        self.alPushButton.setObjectName("alPushButton")
        self.horizontalLayout_10.addWidget(self.alPushButton)
        self.ahPushButton = QtWidgets.QPushButton(self.aGroupBox)
        self.ahPushButton.setCheckable(True)
        self.ahPushButton.setAutoExclusive(True)
        self.ahPushButton.setObjectName("ahPushButton")
        self.horizontalLayout_10.addWidget(self.ahPushButton)
        self.verticalLayout_6.addWidget(self.aGroupBox)
        self.horizontalLayout_26.addLayout(self.verticalLayout_6)
        self.verticalLayout_9.addLayout(self.horizontalLayout_26)
        self.toolBox.addItem(self.baseScorePage, "")
        self.temporalScorePage = QtWidgets.QWidget()
        self.temporalScorePage.setGeometry(QtCore.QRect(0, 0, 1097, 575))
        self.temporalScorePage.setObjectName("temporalScorePage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.temporalScorePage)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.temporalScoreLabel = QtWidgets.QLabel(self.temporalScorePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temporalScoreLabel.sizePolicy().hasHeightForWidth())
        self.temporalScoreLabel.setSizePolicy(sizePolicy)
        self.temporalScoreLabel.setObjectName("temporalScoreLabel")
        self.verticalLayout_4.addWidget(self.temporalScoreLabel)
        self.eGroupBox = QtWidgets.QGroupBox(self.temporalScorePage)
        self.eGroupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    margin-top: 0.5em;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.eGroupBox.setObjectName("eGroupBox")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.eGroupBox)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.exPushButton = QtWidgets.QPushButton(self.eGroupBox)
        self.exPushButton.setCheckable(True)
        self.exPushButton.setAutoExclusive(True)
        self.exPushButton.setObjectName("exPushButton")
        self.horizontalLayout_12.addWidget(self.exPushButton)
        self.euPushButton = QtWidgets.QPushButton(self.eGroupBox)
        self.euPushButton.setCheckable(True)
        self.euPushButton.setAutoExclusive(True)
        self.euPushButton.setObjectName("euPushButton")
        self.horizontalLayout_12.addWidget(self.euPushButton)
        self.epPushButton = QtWidgets.QPushButton(self.eGroupBox)
        self.epPushButton.setCheckable(True)
        self.epPushButton.setAutoExclusive(True)
        self.epPushButton.setObjectName("epPushButton")
        self.horizontalLayout_12.addWidget(self.epPushButton)
        self.efPushButton = QtWidgets.QPushButton(self.eGroupBox)
        self.efPushButton.setCheckable(True)
        self.efPushButton.setAutoExclusive(True)
        self.efPushButton.setObjectName("efPushButton")
        self.horizontalLayout_12.addWidget(self.efPushButton)
        self.ehPushButton = QtWidgets.QPushButton(self.eGroupBox)
        self.ehPushButton.setCheckable(True)
        self.ehPushButton.setAutoExclusive(True)
        self.ehPushButton.setObjectName("ehPushButton")
        self.horizontalLayout_12.addWidget(self.ehPushButton)
        self.verticalLayout_4.addWidget(self.eGroupBox)
        self.rlGroupBox = QtWidgets.QGroupBox(self.temporalScorePage)
        self.rlGroupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    margin-top: 0.5em;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.rlGroupBox.setObjectName("rlGroupBox")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.rlGroupBox)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.rlxPushButton = QtWidgets.QPushButton(self.rlGroupBox)
        self.rlxPushButton.setCheckable(True)
        self.rlxPushButton.setAutoExclusive(True)
        self.rlxPushButton.setObjectName("rlxPushButton")
        self.horizontalLayout_13.addWidget(self.rlxPushButton)
        self.rloPushButton = QtWidgets.QPushButton(self.rlGroupBox)
        self.rloPushButton.setCheckable(True)
        self.rloPushButton.setAutoExclusive(True)
        self.rloPushButton.setObjectName("rloPushButton")
        self.horizontalLayout_13.addWidget(self.rloPushButton)
        self.rltPushButton = QtWidgets.QPushButton(self.rlGroupBox)
        self.rltPushButton.setCheckable(True)
        self.rltPushButton.setAutoExclusive(True)
        self.rltPushButton.setObjectName("rltPushButton")
        self.horizontalLayout_13.addWidget(self.rltPushButton)
        self.rlwPushButton = QtWidgets.QPushButton(self.rlGroupBox)
        self.rlwPushButton.setCheckable(True)
        self.rlwPushButton.setAutoExclusive(True)
        self.rlwPushButton.setObjectName("rlwPushButton")
        self.horizontalLayout_13.addWidget(self.rlwPushButton)
        self.rluPushButton = QtWidgets.QPushButton(self.rlGroupBox)
        self.rluPushButton.setCheckable(True)
        self.rluPushButton.setAutoExclusive(True)
        self.rluPushButton.setObjectName("rluPushButton")
        self.horizontalLayout_13.addWidget(self.rluPushButton)
        self.verticalLayout_4.addWidget(self.rlGroupBox)
        self.rcGroupBox = QtWidgets.QGroupBox(self.temporalScorePage)
        self.rcGroupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    margin-top: 0.5em;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.rcGroupBox.setObjectName("rcGroupBox")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.rcGroupBox)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.rcxPushButton = QtWidgets.QPushButton(self.rcGroupBox)
        self.rcxPushButton.setCheckable(True)
        self.rcxPushButton.setAutoExclusive(True)
        self.rcxPushButton.setObjectName("rcxPushButton")
        self.horizontalLayout_14.addWidget(self.rcxPushButton)
        self.rcuPushButton = QtWidgets.QPushButton(self.rcGroupBox)
        self.rcuPushButton.setCheckable(True)
        self.rcuPushButton.setAutoExclusive(True)
        self.rcuPushButton.setObjectName("rcuPushButton")
        self.horizontalLayout_14.addWidget(self.rcuPushButton)
        self.rcrPushButton = QtWidgets.QPushButton(self.rcGroupBox)
        self.rcrPushButton.setCheckable(True)
        self.rcrPushButton.setAutoExclusive(True)
        self.rcrPushButton.setObjectName("rcrPushButton")
        self.horizontalLayout_14.addWidget(self.rcrPushButton)
        self.rccPushButton = QtWidgets.QPushButton(self.rcGroupBox)
        self.rccPushButton.setCheckable(True)
        self.rccPushButton.setAutoExclusive(True)
        self.rccPushButton.setObjectName("rccPushButton")
        self.horizontalLayout_14.addWidget(self.rccPushButton)
        self.verticalLayout_4.addWidget(self.rcGroupBox)
        self.toolBox.addItem(self.temporalScorePage, "")
        self.environmentalScorePage = QtWidgets.QWidget()
        self.environmentalScorePage.setGeometry(QtCore.QRect(0, 0, 1097, 575))
        self.environmentalScorePage.setObjectName("environmentalScorePage")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.environmentalScorePage)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.environmentalScoreLabel = QtWidgets.QLabel(self.environmentalScorePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.environmentalScoreLabel.sizePolicy().hasHeightForWidth())
        self.environmentalScoreLabel.setSizePolicy(sizePolicy)
        self.environmentalScoreLabel.setObjectName("environmentalScoreLabel")
        self.verticalLayout_5.addWidget(self.environmentalScoreLabel)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.crGroupBox = QtWidgets.QGroupBox(self.environmentalScorePage)
        self.crGroupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    margin-top: 0.5em;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.crGroupBox.setObjectName("crGroupBox")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.crGroupBox)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.crxPushButton = QtWidgets.QPushButton(self.crGroupBox)
        self.crxPushButton.setCheckable(True)
        self.crxPushButton.setAutoExclusive(True)
        self.crxPushButton.setObjectName("crxPushButton")
        self.horizontalLayout_15.addWidget(self.crxPushButton)
        self.crlPushButton = QtWidgets.QPushButton(self.crGroupBox)
        self.crlPushButton.setCheckable(True)
        self.crlPushButton.setAutoExclusive(True)
        self.crlPushButton.setObjectName("crlPushButton")
        self.horizontalLayout_15.addWidget(self.crlPushButton)
        self.crmPushButton = QtWidgets.QPushButton(self.crGroupBox)
        self.crmPushButton.setCheckable(True)
        self.crmPushButton.setAutoExclusive(True)
        self.crmPushButton.setObjectName("crmPushButton")
        self.horizontalLayout_15.addWidget(self.crmPushButton)
        self.crhPushButton = QtWidgets.QPushButton(self.crGroupBox)
        self.crhPushButton.setCheckable(True)
        self.crhPushButton.setAutoExclusive(True)
        self.crhPushButton.setObjectName("crhPushButton")
        self.horizontalLayout_15.addWidget(self.crhPushButton)
        self.verticalLayout_7.addWidget(self.crGroupBox)
        self.irGroupBox = QtWidgets.QGroupBox(self.environmentalScorePage)
        self.irGroupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    margin-top: 0.5em;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.irGroupBox.setObjectName("irGroupBox")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.irGroupBox)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.irxPushButton = QtWidgets.QPushButton(self.irGroupBox)
        self.irxPushButton.setCheckable(True)
        self.irxPushButton.setAutoExclusive(True)
        self.irxPushButton.setObjectName("irxPushButton")
        self.horizontalLayout_16.addWidget(self.irxPushButton)
        self.irlPushButton = QtWidgets.QPushButton(self.irGroupBox)
        self.irlPushButton.setCheckable(True)
        self.irlPushButton.setAutoExclusive(True)
        self.irlPushButton.setObjectName("irlPushButton")
        self.horizontalLayout_16.addWidget(self.irlPushButton)
        self.irmPushButton = QtWidgets.QPushButton(self.irGroupBox)
        self.irmPushButton.setCheckable(True)
        self.irmPushButton.setAutoExclusive(True)
        self.irmPushButton.setObjectName("irmPushButton")
        self.horizontalLayout_16.addWidget(self.irmPushButton)
        self.irhPushButton = QtWidgets.QPushButton(self.irGroupBox)
        self.irhPushButton.setCheckable(True)
        self.irhPushButton.setAutoExclusive(True)
        self.irhPushButton.setObjectName("irhPushButton")
        self.horizontalLayout_16.addWidget(self.irhPushButton)
        self.verticalLayout_7.addWidget(self.irGroupBox)
        self.arGroupBox = QtWidgets.QGroupBox(self.environmentalScorePage)
        self.arGroupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    margin-top: 0.5em;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.arGroupBox.setObjectName("arGroupBox")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.arGroupBox)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.arxPushButton = QtWidgets.QPushButton(self.arGroupBox)
        self.arxPushButton.setCheckable(True)
        self.arxPushButton.setAutoExclusive(True)
        self.arxPushButton.setObjectName("arxPushButton")
        self.horizontalLayout_17.addWidget(self.arxPushButton)
        self.arlPushButton = QtWidgets.QPushButton(self.arGroupBox)
        self.arlPushButton.setCheckable(True)
        self.arlPushButton.setAutoExclusive(True)
        self.arlPushButton.setObjectName("arlPushButton")
        self.horizontalLayout_17.addWidget(self.arlPushButton)
        self.armPushButton = QtWidgets.QPushButton(self.arGroupBox)
        self.armPushButton.setCheckable(True)
        self.armPushButton.setAutoExclusive(True)
        self.armPushButton.setObjectName("armPushButton")
        self.horizontalLayout_17.addWidget(self.armPushButton)
        self.arhPushButton = QtWidgets.QPushButton(self.arGroupBox)
        self.arhPushButton.setCheckable(True)
        self.arhPushButton.setAutoExclusive(True)
        self.arhPushButton.setObjectName("arhPushButton")
        self.horizontalLayout_17.addWidget(self.arhPushButton)
        self.verticalLayout_7.addWidget(self.arGroupBox)
        self.horizontalLayout_11.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.mavGroupBox = QtWidgets.QGroupBox(self.environmentalScorePage)
        self.mavGroupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    margin-top: 0.5em;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.mavGroupBox.setObjectName("mavGroupBox")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.mavGroupBox)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.mavxPushButton = QtWidgets.QPushButton(self.mavGroupBox)
        self.mavxPushButton.setCheckable(True)
        self.mavxPushButton.setAutoExclusive(True)
        self.mavxPushButton.setObjectName("mavxPushButton")
        self.horizontalLayout_18.addWidget(self.mavxPushButton)
        self.mavnPushButton = QtWidgets.QPushButton(self.mavGroupBox)
        self.mavnPushButton.setCheckable(True)
        self.mavnPushButton.setAutoExclusive(True)
        self.mavnPushButton.setObjectName("mavnPushButton")
        self.horizontalLayout_18.addWidget(self.mavnPushButton)
        self.mavaPushButton = QtWidgets.QPushButton(self.mavGroupBox)
        self.mavaPushButton.setCheckable(True)
        self.mavaPushButton.setAutoExclusive(True)
        self.mavaPushButton.setObjectName("mavaPushButton")
        self.horizontalLayout_18.addWidget(self.mavaPushButton)
        self.mavlPushButton = QtWidgets.QPushButton(self.mavGroupBox)
        self.mavlPushButton.setCheckable(True)
        self.mavlPushButton.setAutoExclusive(True)
        self.mavlPushButton.setObjectName("mavlPushButton")
        self.horizontalLayout_18.addWidget(self.mavlPushButton)
        self.mavpPushButton = QtWidgets.QPushButton(self.mavGroupBox)
        self.mavpPushButton.setCheckable(True)
        self.mavpPushButton.setAutoExclusive(True)
        self.mavpPushButton.setObjectName("mavpPushButton")
        self.horizontalLayout_18.addWidget(self.mavpPushButton)
        self.verticalLayout_8.addWidget(self.mavGroupBox)
        self.macGroupBox = QtWidgets.QGroupBox(self.environmentalScorePage)
        self.macGroupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    margin-top: 0.5em;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.macGroupBox.setObjectName("macGroupBox")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.macGroupBox)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.macxPushButton = QtWidgets.QPushButton(self.macGroupBox)
        self.macxPushButton.setCheckable(True)
        self.macxPushButton.setAutoExclusive(True)
        self.macxPushButton.setObjectName("macxPushButton")
        self.horizontalLayout_19.addWidget(self.macxPushButton)
        self.maclPushButton = QtWidgets.QPushButton(self.macGroupBox)
        self.maclPushButton.setCheckable(True)
        self.maclPushButton.setAutoExclusive(True)
        self.maclPushButton.setObjectName("maclPushButton")
        self.horizontalLayout_19.addWidget(self.maclPushButton)
        self.machPushButton = QtWidgets.QPushButton(self.macGroupBox)
        self.machPushButton.setCheckable(True)
        self.machPushButton.setAutoExclusive(True)
        self.machPushButton.setObjectName("machPushButton")
        self.horizontalLayout_19.addWidget(self.machPushButton)
        self.verticalLayout_8.addWidget(self.macGroupBox)
        self.mprGroupBox = QtWidgets.QGroupBox(self.environmentalScorePage)
        self.mprGroupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    margin-top: 0.5em;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.mprGroupBox.setObjectName("mprGroupBox")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.mprGroupBox)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.mprxPushButton = QtWidgets.QPushButton(self.mprGroupBox)
        self.mprxPushButton.setCheckable(True)
        self.mprxPushButton.setAutoExclusive(True)
        self.mprxPushButton.setObjectName("mprxPushButton")
        self.horizontalLayout_20.addWidget(self.mprxPushButton)
        self.mprnPushButton = QtWidgets.QPushButton(self.mprGroupBox)
        self.mprnPushButton.setCheckable(True)
        self.mprnPushButton.setAutoExclusive(True)
        self.mprnPushButton.setObjectName("mprnPushButton")
        self.horizontalLayout_20.addWidget(self.mprnPushButton)
        self.mprlPushButton = QtWidgets.QPushButton(self.mprGroupBox)
        self.mprlPushButton.setCheckable(True)
        self.mprlPushButton.setAutoExclusive(True)
        self.mprlPushButton.setObjectName("mprlPushButton")
        self.horizontalLayout_20.addWidget(self.mprlPushButton)
        self.mprhPushButton = QtWidgets.QPushButton(self.mprGroupBox)
        self.mprhPushButton.setCheckable(True)
        self.mprhPushButton.setAutoExclusive(True)
        self.mprhPushButton.setObjectName("mprhPushButton")
        self.horizontalLayout_20.addWidget(self.mprhPushButton)
        self.verticalLayout_8.addWidget(self.mprGroupBox)
        self.muiGroupBox = QtWidgets.QGroupBox(self.environmentalScorePage)
        self.muiGroupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    margin-top: 0.5em;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.muiGroupBox.setObjectName("muiGroupBox")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.muiGroupBox)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.muixPushButton = QtWidgets.QPushButton(self.muiGroupBox)
        self.muixPushButton.setCheckable(True)
        self.muixPushButton.setAutoExclusive(True)
        self.muixPushButton.setObjectName("muixPushButton")
        self.horizontalLayout_21.addWidget(self.muixPushButton)
        self.muinPushButton = QtWidgets.QPushButton(self.muiGroupBox)
        self.muinPushButton.setCheckable(True)
        self.muinPushButton.setAutoExclusive(True)
        self.muinPushButton.setObjectName("muinPushButton")
        self.horizontalLayout_21.addWidget(self.muinPushButton)
        self.muirPushButton = QtWidgets.QPushButton(self.muiGroupBox)
        self.muirPushButton.setCheckable(True)
        self.muirPushButton.setAutoExclusive(True)
        self.muirPushButton.setObjectName("muirPushButton")
        self.horizontalLayout_21.addWidget(self.muirPushButton)
        self.verticalLayout_8.addWidget(self.muiGroupBox)
        self.msGroupBox = QtWidgets.QGroupBox(self.environmentalScorePage)
        self.msGroupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    margin-top: 0.5em;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.msGroupBox.setObjectName("msGroupBox")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.msGroupBox)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.msxPushButton = QtWidgets.QPushButton(self.msGroupBox)
        self.msxPushButton.setCheckable(True)
        self.msxPushButton.setAutoExclusive(True)
        self.msxPushButton.setObjectName("msxPushButton")
        self.horizontalLayout_22.addWidget(self.msxPushButton)
        self.msuPushButton = QtWidgets.QPushButton(self.msGroupBox)
        self.msuPushButton.setCheckable(True)
        self.msuPushButton.setAutoExclusive(True)
        self.msuPushButton.setObjectName("msuPushButton")
        self.horizontalLayout_22.addWidget(self.msuPushButton)
        self.mscPushButton = QtWidgets.QPushButton(self.msGroupBox)
        self.mscPushButton.setCheckable(True)
        self.mscPushButton.setAutoExclusive(True)
        self.mscPushButton.setObjectName("mscPushButton")
        self.horizontalLayout_22.addWidget(self.mscPushButton)
        self.verticalLayout_8.addWidget(self.msGroupBox)
        self.mcGroupBox = QtWidgets.QGroupBox(self.environmentalScorePage)
        self.mcGroupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    margin-top: 0.5em;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.mcGroupBox.setObjectName("mcGroupBox")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.mcGroupBox)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.mcxPushButton = QtWidgets.QPushButton(self.mcGroupBox)
        self.mcxPushButton.setCheckable(True)
        self.mcxPushButton.setAutoExclusive(True)
        self.mcxPushButton.setObjectName("mcxPushButton")
        self.horizontalLayout_23.addWidget(self.mcxPushButton)
        self.mcnPushButton = QtWidgets.QPushButton(self.mcGroupBox)
        self.mcnPushButton.setCheckable(True)
        self.mcnPushButton.setAutoExclusive(True)
        self.mcnPushButton.setObjectName("mcnPushButton")
        self.horizontalLayout_23.addWidget(self.mcnPushButton)
        self.mclPushButton = QtWidgets.QPushButton(self.mcGroupBox)
        self.mclPushButton.setCheckable(True)
        self.mclPushButton.setAutoExclusive(True)
        self.mclPushButton.setObjectName("mclPushButton")
        self.horizontalLayout_23.addWidget(self.mclPushButton)
        self.mchPushButton = QtWidgets.QPushButton(self.mcGroupBox)
        self.mchPushButton.setCheckable(True)
        self.mchPushButton.setAutoExclusive(True)
        self.mchPushButton.setObjectName("mchPushButton")
        self.horizontalLayout_23.addWidget(self.mchPushButton)
        self.verticalLayout_8.addWidget(self.mcGroupBox)
        self.miGroupBox = QtWidgets.QGroupBox(self.environmentalScorePage)
        self.miGroupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    margin-top: 0.5em;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.miGroupBox.setObjectName("miGroupBox")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.miGroupBox)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.mixPushButton = QtWidgets.QPushButton(self.miGroupBox)
        self.mixPushButton.setCheckable(True)
        self.mixPushButton.setAutoExclusive(True)
        self.mixPushButton.setObjectName("mixPushButton")
        self.horizontalLayout_24.addWidget(self.mixPushButton)
        self.minPushButton = QtWidgets.QPushButton(self.miGroupBox)
        self.minPushButton.setCheckable(True)
        self.minPushButton.setAutoExclusive(True)
        self.minPushButton.setObjectName("minPushButton")
        self.horizontalLayout_24.addWidget(self.minPushButton)
        self.milPushButton = QtWidgets.QPushButton(self.miGroupBox)
        self.milPushButton.setCheckable(True)
        self.milPushButton.setAutoExclusive(True)
        self.milPushButton.setObjectName("milPushButton")
        self.horizontalLayout_24.addWidget(self.milPushButton)
        self.mihPushButton = QtWidgets.QPushButton(self.miGroupBox)
        self.mihPushButton.setCheckable(True)
        self.mihPushButton.setAutoExclusive(True)
        self.mihPushButton.setObjectName("mihPushButton")
        self.horizontalLayout_24.addWidget(self.mihPushButton)
        self.verticalLayout_8.addWidget(self.miGroupBox)
        self.maGroupBox = QtWidgets.QGroupBox(self.environmentalScorePage)
        self.maGroupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    margin-top: 0.5em;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.maGroupBox.setObjectName("maGroupBox")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.maGroupBox)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.maxPushButton = QtWidgets.QPushButton(self.maGroupBox)
        self.maxPushButton.setCheckable(True)
        self.maxPushButton.setAutoExclusive(True)
        self.maxPushButton.setObjectName("maxPushButton")
        self.horizontalLayout_25.addWidget(self.maxPushButton)
        self.manPushButton = QtWidgets.QPushButton(self.maGroupBox)
        self.manPushButton.setCheckable(True)
        self.manPushButton.setAutoExclusive(True)
        self.manPushButton.setObjectName("manPushButton")
        self.horizontalLayout_25.addWidget(self.manPushButton)
        self.malPushButton = QtWidgets.QPushButton(self.maGroupBox)
        self.malPushButton.setCheckable(True)
        self.malPushButton.setAutoExclusive(True)
        self.malPushButton.setObjectName("malPushButton")
        self.horizontalLayout_25.addWidget(self.malPushButton)
        self.mahPushButton = QtWidgets.QPushButton(self.maGroupBox)
        self.mahPushButton.setCheckable(True)
        self.mahPushButton.setAutoExclusive(True)
        self.mahPushButton.setObjectName("mahPushButton")
        self.horizontalLayout_25.addWidget(self.mahPushButton)
        self.verticalLayout_8.addWidget(self.maGroupBox)
        self.horizontalLayout_11.addLayout(self.verticalLayout_8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.toolBox.addItem(self.environmentalScorePage, "")
        self.verticalLayout.addWidget(self.toolBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CVSS Calculator"))
        self.baseScoreLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">MISSING METRICS</span></p></body></html>"))
        self.avGroupBox.setTitle(_translate("MainWindow", "Attack Vector (AV)"))
        self.avnPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>A vulnerability exploitable with network access means the vulnerable component is bond to the network stack and the attacker\'s path is through OSI layer 3 (the network layer). Such a vulnerability is often termed &quot;remotely exploitable&quot; and can be thought of as an attack being exploitable one or more network hops away (e.g. across layer 3 boundaries from routers). An example of a network attack is an attacker causing a denial of service (DoS) by sending a specially crafted TCP packet from across the public Internet (e.g. CVE-2004-0230).</p></body></html>"))
        self.avnPushButton.setText(_translate("MainWindow", "Network (N)"))
        self.avaPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>A vulnerability exploitable with adjacent network access means the vulnerable component is bound to the network stack, however the attack is limited to the same shared physical (e.g. Bluetooth, IEEE 802.11), or logical (e.g. local IP subnet) network, and cannot be performed across an OSI layer 3 boundary (e.g. a router). An example of an Adjacent attack would be an ARP (IPv4) or neighbor discovery (IPv6) flood leading to a denial of service on the local LAN segment. See also CVE-2013-6014.</p></body></html>"))
        self.avaPushButton.setText(_translate("MainWindow", "Adjacent (A)"))
        self.avlPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>A vulnerability exploitable with Local access means that the vulnerable component is not bound to the network stack, and the attacker\'s path is via read/write/execute capabilities. In some cases, the attacker may be logged in locally in order to exploit the vulnerability, otherwise, she may rely on User Interaction to execute a malicious file.</p></body></html>"))
        self.avlPushButton.setText(_translate("MainWindow", "Local (L)"))
        self.avpPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>A vulnerability exploitable with Physical access requires the attacker to physically touch or manipulate the vulnerable component. Physical interaction may be brief (e.g. evil maid attack) or persistent. An example of such an attack is a cold boot attack which allows an attacker to access to disk encryption keys after gaining physical access to the system, or peripheral attacks such as Firewire/USB Direct Memory Access attacks.</p></body></html>"))
        self.avpPushButton.setText(_translate("MainWindow", "Physical (P)"))
        self.acGroupBox.setTitle(_translate("MainWindow", "Attack Complexity (AC)"))
        self.aclPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Specialized access conditions or extenuating circumstances do not exist. An attacker can expect repeatable success against the vulnerable component.</p></body></html>"))
        self.aclPushButton.setText(_translate("MainWindow", "Low (L)"))
        self.achPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>A successful attack depends on conditions beyond the attacker\'s control. That is, a successful attack cannot be accomplished at will, but requires the attacker to invest in some measurable amount of effort in preparation or execution against the vulnerable component before a successful attack can be expected. For example, a successful attack may depend on an attacker overcoming any of the following conditions:</p>\n"
"<ul>\n"
"<li><p>The attacker must conduct target-specific reconnaissance. For example, on target configuration settings, sequence numbers, shared secrets, etc.</p></li>\n"
"<li><p>The attacker must prepare the target environment to improve exploit reliability. For example, repeated exploitation to win a race condition, or overcoming advanced exploit mitigation techniques. </p></li>\n"
"<li><p>The attacker must inject herself into the logical network path between the target and the resource requested by the victim in order to read and/or modify network communications (e.g. man in the middle attack).</p></li>\n"
"</ul></body></html>"))
        self.achPushButton.setText(_translate("MainWindow", "High (H)"))
        self.prGroupBox.setTitle(_translate("MainWindow", "Privileges Required (PR)"))
        self.prnPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>The attacker is unauthorized prior to attack, and therefore does not require any access to settings or files to carry out an attack.</p></body></html>"))
        self.prnPushButton.setText(_translate("MainWindow", "None (N)"))
        self.prlPutton.setToolTip(_translate("MainWindow", "<html><head/><body><p>The attacker is authorized with (i.e. requires) privileges that provide basic user capabilities that could normally affect only settings and files owned by a user. Alternatively, an attacker with Low privileges may have the ability to cause an impact only to non-sensitive resources.</p></body></html>"))
        self.prlPutton.setText(_translate("MainWindow", "Low (L)"))
        self.prhPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>The attacker is authorized with (i.e. requires) privileges that provide significant (e.g. administrative) control over the vulnerable component that could affect component-wide settings and files.</p></body></html>"))
        self.prhPushButton.setText(_translate("MainWindow", "High (H)"))
        self.uiGroupBox.setTitle(_translate("MainWindow", "User Interaction (UI)"))
        self.uinPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>The vulnerable system can be exploited without interaction from any user.</p></body></html>"))
        self.uinPushButton.setText(_translate("MainWindow", "None (N)"))
        self.uirPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Successful exploitation of this vulnerability requires a user to take some action before the vulnerability can be exploited. For example, a successful exploit may only be possible during the installation of an application by a system administrator.</p></body></html>"))
        self.uirPushButton.setText(_translate("MainWindow", "Required (R)"))
        self.sGroupBox.setTitle(_translate("MainWindow", "Scope (S)"))
        self.suPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>An exploited vulnerability can only affect resources managed by the same authority. In this case the vulnerable component and the impacted component are the same.</p></body></html>"))
        self.suPushButton.setText(_translate("MainWindow", "Unchanged (U)"))
        self.scPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>An exploited vulnerability can affect resources beyond the authorization privileges intended by the vulnerable component. In this case the vulnerable component and the impacted component are different.</p></body></html>"))
        self.scPushButton.setText(_translate("MainWindow", "Changed (C)"))
        self.cGroupBox.setTitle(_translate("MainWindow", "Confidentiality (C)"))
        self.cnPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>There is no loss of confidentiality within the impacted component.</p></body></html>"))
        self.cnPushButton.setText(_translate("MainWindow", "None (N)"))
        self.clPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>There is some loss of confidentiality. Access to some restricted information is obtained, but the attacker does not have control over what information is obtained, or the amount or kind of loss is constrained. The information disclosure does not cause a direct, serious loss to the impacted component.</p></body></html>"))
        self.clPushButton.setText(_translate("MainWindow", "Low (L)"))
        self.chPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>There is total loss of confidentiality, resulting in all resources within the impacted component being divulged to the attacker. Alternatively, access to only some restricted information is obtained, but the disclosed information presents a direct, serious impact. For example, an attacker steals the administrator\'s password, or private encryption keys of a web server.</p></body></html>"))
        self.chPushButton.setText(_translate("MainWindow", "High (H)"))
        self.iGroupBox.setTitle(_translate("MainWindow", "Integrity (I)"))
        self.inPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>There is no loss of integrity within the impacted component.</p></body></html>"))
        self.inPushButton.setText(_translate("MainWindow", "None (N)"))
        self.ilPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Modification of data is possible, but the attacker does not have control over the consequence of a modification, or the amount of modification is constrained. The data modification does not have a direct, serious impact on the impacted component.</p></body></html>"))
        self.ilPushButton.setText(_translate("MainWindow", "Low (L)"))
        self.ihPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>There is a total loss of integrity, or a complete loss of protection. For example, the attacker is able to modify any/all files protected by the impacted component. Alternatively, only some files can be modified, but malicious modification would present a direct, serious consequence to the impacted component.</p></body></html>"))
        self.ihPushButton.setText(_translate("MainWindow", "High (H)"))
        self.aGroupBox.setTitle(_translate("MainWindow", "Availability (A)"))
        self.anPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>There is no impact to availability within the impacted component.</p></body></html>"))
        self.anPushButton.setText(_translate("MainWindow", "None (N)"))
        self.alPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>There is reduced performance or interruptions in resource availability. Even if repeated exploitation of the vulnerability is possible, the attacker does not have the ability to completely deny service to legitimate users. The resources in the impacted component are either partially available all of the time, or fully available only some of the time, but overall there is no direct, serious consequence to the impacted component.</p></body></html>"))
        self.alPushButton.setText(_translate("MainWindow", "Low (L)"))
        self.ahPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>There is total loss of availability, resulting in the attacker being able to fully deny access to resources in the impacted component; this loss is either sustained (while the attacker continues to deliver the attack) or persistent (the condition persists even after the attack has completed). Alternatively, the attacker has the ability to deny some availability, but the loss of availability presents a direct, serious consequence to the impacted component (e.g., the attacker cannot disrupt existing connections, but can prevent new connections; the attacker can repeatedly exploit a vulnerability that, in each instance of a successful attack, leaks a only small amount of memory, but after repeated exploitation causes a service to become completely unavailable).</p></body></html>"))
        self.ahPushButton.setText(_translate("MainWindow", "High (H)"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.baseScorePage), _translate("MainWindow", "Base Score"))
        self.temporalScoreLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">MISSING METRICS</span></p></body></html>"))
        self.eGroupBox.setTitle(_translate("MainWindow", "Exploit Code Maturity (E)"))
        self.exPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Assigning this value to the metric will not influence the score. It is a signal to a scoring equation to skip this metric.</p></body></html>"))
        self.exPushButton.setText(_translate("MainWindow", "Not Defined (X)"))
        self.euPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>No exploit code is available, or an exploit is theoretical.</p></body></html>"))
        self.euPushButton.setText(_translate("MainWindow", "Unproven (U)"))
        self.epPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Proof-of-concept exploit code is available, or an attack demonstration is not practical for most systems. The code or technique is not functional in all situations and may require substantial modification by a skilled attacker.</p></body></html>"))
        self.epPushButton.setText(_translate("MainWindow", "Proof-of-Concept (P)"))
        self.efPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Functional exploit code is available. The code works in most situations where the vulnerability exists.</p></body></html>"))
        self.efPushButton.setText(_translate("MainWindow", "Functional (F)"))
        self.ehPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Functional autonomous code exists, or no exploit is required (manual trigger) and details are widely available. Exploit code works in every situation, or is actively being delivered via an autonomous agent (such as a worm or virus). Network-connected systems are likely to encounter scanning or exploitation attempts. Exploit development has reached the level of reliable, widely-available, easy-to-use automated tools.</p></body></html>"))
        self.ehPushButton.setText(_translate("MainWindow", "High (H)"))
        self.rlGroupBox.setTitle(_translate("MainWindow", "Remediation Level (RL)"))
        self.rlxPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Assigning this value to the metric will not influence the score. It is a signal to a scoring equation to skip this metric.</p></body></html>"))
        self.rlxPushButton.setText(_translate("MainWindow", "Not Defined (X)"))
        self.rloPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>A complete vendor solution is available. Either the vendor has issued an official patch, or an upgrade is available.</p></body></html>"))
        self.rloPushButton.setText(_translate("MainWindow", "Official Fix (O)"))
        self.rltPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>There is an official but temporary fix available. This includes instances where the vendor issues a temporary hotfix, tool, or workaround.</p></body></html>"))
        self.rltPushButton.setText(_translate("MainWindow", "Temporary Fix (T)"))
        self.rlwPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>There is an unofficial, non-vendor solution available. In some cases, users of the affected technology will create a patch of their own or provide steps to work around or otherwise mitigate the vulnerability.</p></body></html>"))
        self.rlwPushButton.setText(_translate("MainWindow", "Workaround (W)"))
        self.rluPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>There is either no solution available or it is impossible to apply.</p></body></html>"))
        self.rluPushButton.setText(_translate("MainWindow", "Unavailable (U)"))
        self.rcGroupBox.setTitle(_translate("MainWindow", "Report Confidence (RC)"))
        self.rcxPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Assigning this value to the metric will not influence the score. It is a signal to a scoring equation to skip this metric.</p></body></html>"))
        self.rcxPushButton.setText(_translate("MainWindow", "Not Defined (X)"))
        self.rcuPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>There are reports of impacts that indicate a vulnerability is present. The reports indicate that the cause of the vulnerability is unknown, or reports may differ on the cause or impacts of the vulnerability. Reporters are uncertain of the true nature of the vulnerability, and there is little confidence in the validity of the reports or whether a static Base score can be applied given the differences described. An example is a bug report which notes that an intermittent but non-reproducible crash occurs, with evidence of memory corruption suggesting that denial of service, or possible more serious impacts, may result.</p></body></html>"))
        self.rcuPushButton.setText(_translate("MainWindow", "Unknown (U)"))
        self.rcrPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Significant details are published, but researchers either do not have full confidence in the root cause, or do not have access to source code to fully confirm all of the interactions that may lead to the result. Reasonable confidence exists, however, that the bug is reproducible and at least one impact is able to be verified (proof-of-concept exploits may provide this). An example is a detailed write-up of research into a vulnerability with an explanation (possibly obfuscated or &quot;left as an exercise to the reader&quot;) that gives assurances on how to reproduce the results.</p></body></html>"))
        self.rcrPushButton.setText(_translate("MainWindow", "Reasonable (R)"))
        self.rccPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Detailed reports exist, or functional reproduction is possible (functional exploits may provide this). Source code is available to independently verify the assertions of the research, or the author or vendor of the affected code has confirmed the presence of the vulnerability.</p></body></html>"))
        self.rccPushButton.setText(_translate("MainWindow", "Confirmed (C)"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.temporalScorePage), _translate("MainWindow", "Temporal Score"))
        self.environmentalScoreLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">MISSING METRICS</span></p></body></html>"))
        self.crGroupBox.setTitle(_translate("MainWindow", "Confidentiality Requirement (CR)"))
        self.crxPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Assigning this value to the metric will not influence the score. It is a signal to the equation to skip this metric.</p></body></html>"))
        self.crxPushButton.setText(_translate("MainWindow", "Not Defined (X)"))
        self.crlPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Loss of confidentiality is likely to have only a limited adverse effect on the organization or individuals associated with the organization (e.g., employees, customers).</p></body></html>"))
        self.crlPushButton.setText(_translate("MainWindow", "Low (L)"))
        self.crmPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Loss of confidentiality is likely to have a serious adverse effect on the organization or individuals associated with the organization (e.g., employees, customers).</p></body></html>"))
        self.crmPushButton.setText(_translate("MainWindow", "Medium (M)"))
        self.crhPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Loss of confidentiality is likely to have a catastrophic adverse effect on the organization or individuals associated with the organization (e.g., employees, customers).</p></body></html>"))
        self.crhPushButton.setText(_translate("MainWindow", "High (H)"))
        self.irGroupBox.setTitle(_translate("MainWindow", "Integrity Requirement (IR)"))
        self.irxPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Assigning this value to the metric will not influence the score. It is a signal to the equation to skip this metric.</p></body></html>"))
        self.irxPushButton.setText(_translate("MainWindow", "Not Defined (X)"))
        self.irlPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Loss of integrity is likely to have only a limited adverse effect on the organization or individuals associated with the organization (e.g., employees, customers).</p></body></html>"))
        self.irlPushButton.setText(_translate("MainWindow", "Low (L)"))
        self.irmPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Loss of integrity is likely to have a serious adverse effect on the organization or individuals associated with the organization (e.g., employees, customers).</p></body></html>"))
        self.irmPushButton.setText(_translate("MainWindow", "Medium (M)"))
        self.irhPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Loss of integrity is likely to have a catastrophic adverse effect on the organization or individuals associated with the organization (e.g., employees, customers).</p></body></html>"))
        self.irhPushButton.setText(_translate("MainWindow", "High (H)"))
        self.arGroupBox.setTitle(_translate("MainWindow", "Availability Requirement (AR)"))
        self.arxPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Assigning this value to the metric will not influence the score. It is a signal to the equation to skip this metric.</p></body></html>"))
        self.arxPushButton.setText(_translate("MainWindow", "Not Defined (X)"))
        self.arlPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Loss of availability is likely to have only a limited adverse effect on the organization or individuals associated with the organization (e.g., employees, customers).</p></body></html>"))
        self.arlPushButton.setText(_translate("MainWindow", "Low (L)"))
        self.armPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Loss of availability is likely to have a serious adverse effect on the organization or individuals associated with the organization (e.g., employees, customers).</p></body></html>"))
        self.armPushButton.setText(_translate("MainWindow", "Medium (M)"))
        self.arhPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Loss of availability is likely to have a catastrophic adverse effect on the organization or individuals associated with the organization (e.g., employees, customers).</p></body></html>"))
        self.arhPushButton.setText(_translate("MainWindow", "High (H)"))
        self.mavGroupBox.setTitle(_translate("MainWindow", "Modified Attack Vector (MAV)"))
        self.mavxPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Assigning this value to the metric will not influence the score. It is a signal to the equation to skip this metric.</p></body></html>"))
        self.mavxPushButton.setText(_translate("MainWindow", "Not Defined (X)"))
        self.mavnPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>A vulnerability exploitable with network access means the vulnerable component is bound to the network stack and the attacker\'s path is through OSI layer 3 (the network layer). Such a vulnerability is often termed &quot;remotely exploitable&quot; and can be thought of as an attack being exploitable one or more network hops away (e.g. across layer 3 boundaries from routers). An example of a network attack is an attacker causing a denial of service (DoS) by sending a specially crafted TCP packet from across the public Internet (e.g. CVE-2004-0230).</p></body></html>"))
        self.mavnPushButton.setText(_translate("MainWindow", "Network (N)"))
        self.mavaPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>A vulnerability exploitable with adjacent network access means the vulnerable component is bound to the network stack, however the attack is limited to the same shared physical (e.g. Bluetooth, IEEE 802.11), or logical (e.g. local IP subnet) network, and cannot be performed across an OSI layer 3 boundary (e.g. a router). An example of an Adjacent attack would be an ARP (IPv4) or neighbor discovery (IPv6) flood leading to a denial of service on the local LAN segment. See also CVE-2013-6014.</p></body></html>"))
        self.mavaPushButton.setText(_translate("MainWindow", "Adjacent (A)"))
        self.mavlPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>A vulnerability exploitable with Local access means that the vulnerable component is not bound to the network stack, and the attacker\'s path is via read/write/execute capabilities. In some cases, the attacker may be logged in locally in order to exploit the vulnerability, otherwise, she may rely on User Interaction to execute a malicious file.</p></body></html>"))
        self.mavlPushButton.setText(_translate("MainWindow", "Local (L)"))
        self.mavpPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>A vulnerability exploitable with Physical access requires the attacker to physically touch or manipulate the vulnerable component. Physical interaction may be brief (e.g. evil maid attack) or persistent. An example of such an attack is a cold boot attack which allows an attacker to access to disk encryption keys after gaining physical access to the system, or peripheral attacks such as Firewire/USB Direct Memory Access attacks.</p></body></html>"))
        self.mavpPushButton.setText(_translate("MainWindow", "Physical (P)"))
        self.macGroupBox.setTitle(_translate("MainWindow", "Modified Attack Complexity (MAC)"))
        self.macxPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Assigning this value to the metric will not influence the score. It is a signal to the equation to skip this metric.</p></body></html>"))
        self.macxPushButton.setText(_translate("MainWindow", "Not Defined (X)"))
        self.maclPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Specialized access conditions or extenuating circumstances do not exist. An attacker can expect repeatable success against the vulnerable component.</p></body></html>"))
        self.maclPushButton.setText(_translate("MainWindow", "Low (L)"))
        self.machPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>A successful attack depends on conditions beyond the attacker\'s control. That is, a successful attack cannot be accomplished at will, but requires the attacker to invest in some measurable amount of effort in preparation or execution against the vulnerable component before a successful attack can be expected. For example, a successful attack may depend on an attacker overcoming any of the following conditions:</p><p>* The attacker must conduct target-specific reconnaissance. For example, on target configuration settings, sequence numbers, shared secrets, etc.</p><p>* The attacker must prepare the target environment to improve exploit reliability. For example, repeated exploitation to win a race condition, or overcoming advanced exploit mitigation techniques.</p><p>* The attacker must inject herself into the logical network path between the target and the resource requested by the victim in order to read and/or modify network communications (e.g. man in the middle attack).</p></body></html>"))
        self.machPushButton.setText(_translate("MainWindow", "High (H)"))
        self.mprGroupBox.setTitle(_translate("MainWindow", "Modified Privileges Required (MPR)"))
        self.mprxPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Assigning this value to the metric will not influence the score. It is a signal to the equation to skip this metric.</p></body></html>"))
        self.mprxPushButton.setText(_translate("MainWindow", "Not Defined (X)"))
        self.mprnPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>The attacker is unauthorized prior to attack, and therefore does not require any access to settings or files to carry out an attack.</p></body></html>"))
        self.mprnPushButton.setText(_translate("MainWindow", "None (N)"))
        self.mprlPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>The attacker is authorized with (i.e. requires) privileges that provide basic user capabilities that could normally affect only settings and files owned by a user. Alternatively, an attacker with Low privileges may have the ability to cause an impact only to non-sensitive resources.</p></body></html>"))
        self.mprlPushButton.setText(_translate("MainWindow", "Low (L)"))
        self.mprhPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>The attacker is authorized with (i.e. requires) privileges that provide significant (e.g. administrative) control over the vulnerable component that could affect component-wide settings and files.</p></body></html>"))
        self.mprhPushButton.setText(_translate("MainWindow", "High (H)"))
        self.muiGroupBox.setTitle(_translate("MainWindow", "Modified User Interation (MUI)"))
        self.muixPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Assigning this value to the metric will not influence the score. It is a signal to the equation to skip this metric.</p></body></html>"))
        self.muixPushButton.setText(_translate("MainWindow", "Not Defined (X)"))
        self.muinPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>The vulnerable system can be exploited without interaction from any user.</p></body></html>"))
        self.muinPushButton.setText(_translate("MainWindow", "None (N)"))
        self.muirPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Successful exploitation of this vulnerability requires a user to take some action before the vulnerability can be exploited. For example, a successful exploit may only be possible during the installation of an application by a system administrator.</p></body></html>"))
        self.muirPushButton.setText(_translate("MainWindow", "Required (R)"))
        self.msGroupBox.setTitle(_translate("MainWindow", "Modified Scope (MS)"))
        self.msxPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Assigning this value to the metric will not influence the score. It is a signal to the equation to skip this metric.</p></body></html>"))
        self.msxPushButton.setText(_translate("MainWindow", "Not Defined (X)"))
        self.msuPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>An exploited vulnerability can only affect resources managed by the same authority. In this case the vulnerable component and the impacted component are the same.</p></body></html>"))
        self.msuPushButton.setText(_translate("MainWindow", "Unchanged (U)"))
        self.mscPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>An exploited vulnerability can affect resources beyond the authorization privileges intended by the vulnerable component. In this case the vulnerable component and the impacted component are different.</p></body></html>"))
        self.mscPushButton.setText(_translate("MainWindow", "Changed (C)"))
        self.mcGroupBox.setTitle(_translate("MainWindow", "Modified Confidentiality (MC)"))
        self.mcxPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Assigning this value to the metric will not influence the score. It is a signal to the equation to skip this metric.</p></body></html>"))
        self.mcxPushButton.setText(_translate("MainWindow", "Not Defined (X)"))
        self.mcnPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>There is no loss of confidentiality within the impacted component.</p></body></html>"))
        self.mcnPushButton.setText(_translate("MainWindow", "None (N)"))
        self.mclPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>There is some loss of confidentiality. Access to some restricted information is obtained, but the attacker does not have control over what information is obtained, or the amount or kind of loss is constrained. The information disclosure does not cause a direct, serious loss to the impacted component.</p></body></html>"))
        self.mclPushButton.setText(_translate("MainWindow", "Low (L)"))
        self.mchPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>There is total loss of confidentiality, resulting in all resources within the impacted component being divulged to the attacker. Alternatively, access to only some restricted information is obtained, but the disclosed information presents a direct, serious impact. For example, an attacker steals the administrator\'s password, or private encryption keys of a web server.</p></body></html>"))
        self.mchPushButton.setText(_translate("MainWindow", "High (H)"))
        self.miGroupBox.setTitle(_translate("MainWindow", "Modified Integrity (MI)"))
        self.mixPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Assigning this value to the metric will not influence the score. It is a signal to the equation to skip this metric.</p></body></html>"))
        self.mixPushButton.setText(_translate("MainWindow", "Not Defined (X)"))
        self.minPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>There is no loss of integrity within the impacted component.</p></body></html>"))
        self.minPushButton.setText(_translate("MainWindow", "None (N)"))
        self.milPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Modification of data is possible, but the attacker does not have control over the consequence of a modification, or the amount of modification is constrained. The data modification does not have a direct, serious impact on the impacted component.</p></body></html>"))
        self.milPushButton.setText(_translate("MainWindow", "Low (L)"))
        self.mihPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>There is a total loss of integrity, or a complete loss of protection. For example, the attacker is able to modify any/all files protected by the impacted component. Alternatively, only some files can be modified, but malicious modification would present a direct, serious consequence to the impacted component.</p></body></html>"))
        self.mihPushButton.setText(_translate("MainWindow", "High (H)"))
        self.maGroupBox.setTitle(_translate("MainWindow", "Modified Availability (MA)"))
        self.maxPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Assigning this value to the metric will not influence the score. It is a signal to the equation to skip this metric.</p></body></html>"))
        self.maxPushButton.setText(_translate("MainWindow", "Not Defined (X)"))
        self.manPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>There is no impact to availability within the impacted component.</p></body></html>"))
        self.manPushButton.setText(_translate("MainWindow", "None (N)"))
        self.malPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>There is reduced performance or interruptions in resource availability. Even if repeated exploitation of the vulnerability is possible, the attacker does not have the ability to completely deny service to legitimate users. The resources in the impacted component are either partially available all of the time, or fully available only some of the time, but overall there is no direct, serious consequence to the impacted component.</p></body></html>"))
        self.malPushButton.setText(_translate("MainWindow", "Low (L)"))
        self.mahPushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>There is total loss of availability, resulting in the attacker being able to fully deny access to resources in the impacted component; this loss is either sustained (while the attacker continues to deliver the attack) or persistent (the condition persists even after the attack has completed). Alternatively, the attacker has the ability to deny some availability, but the loss of availability presents a direct, serious consequence to the impacted component (e.g., the attacker cannot disrupt existing connections, but can prevent new connections; the attacker can repeatedly exploit a vulnerability that, in each instance of a successful attack, leaks a only small amount of memory, but after repeated exploitation causes a service to become completely unavailable).</p></body></html>"))
        self.mahPushButton.setText(_translate("MainWindow", "High (H)"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.environmentalScorePage), _translate("MainWindow", "Environmental Score"))

