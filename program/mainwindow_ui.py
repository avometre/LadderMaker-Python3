# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(996, 609)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 50, 651, 521))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMouseTracking(True)
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(580, 10, 50, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(630, 10, 50, 13))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(580, 30, 50, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(630, 30, 50, 13))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.undoBbutton = QtWidgets.QToolButton(self.centralwidget)
        self.undoBbutton.setGeometry(QtCore.QRect(30, 10, 61, 21))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/CurvedArrowRightDown.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undoBbutton.setIcon(icon)
        self.undoBbutton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.undoBbutton.setObjectName("undoBbutton")
        self.redoButton = QtWidgets.QToolButton(self.centralwidget)
        self.redoButton.setGeometry(QtCore.QRect(100, 10, 61, 21))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/CurvedArrowLeftDown.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redoButton.setIcon(icon1)
        self.redoButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.redoButton.setObjectName("redoButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(680, 50, 231, 321))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableWidget.setFont(font)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(55)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(14)
        self.infoButton = QtWidgets.QPushButton(self.centralwidget)
        self.infoButton.setGeometry(QtCore.QRect(200, 10, 75, 23))
        self.infoButton.setObjectName("infoButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(680, 380, 231, 101))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.toolBar.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 996, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuDiagnostics = QtWidgets.QMenu(self.menuBar)
        self.menuDiagnostics.setObjectName("menuDiagnostics")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar_2)
        self.actionContNO = QtWidgets.QAction(MainWindow)
        self.actionContNO.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/contact_NO_button.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionContNO.setIcon(icon2)
        self.actionContNO.setObjectName("actionContNO")
        self.actionContNC = QtWidgets.QAction(MainWindow)
        self.actionContNC.setCheckable(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/contact_NC_button.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionContNC.setIcon(icon3)
        self.actionContNC.setObjectName("actionContNC")
        self.actionCoil = QtWidgets.QAction(MainWindow)
        self.actionCoil.setCheckable(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/Coil_button.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCoil.setIcon(icon4)
        self.actionCoil.setObjectName("actionCoil")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionaddRung = QtWidgets.QAction(MainWindow)
        self.actionaddRung.setCheckable(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/rung.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionaddRung.setIcon(icon5)
        self.actionaddRung.setObjectName("actionaddRung")
        self.actionWiden = QtWidgets.QAction(MainWindow)
        self.actionWiden.setCheckable(True)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/widen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionWiden.setIcon(icon6)
        self.actionWiden.setObjectName("actionWiden")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionDEL = QtWidgets.QAction(MainWindow)
        self.actionDEL.setCheckable(True)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/del.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDEL.setIcon(icon7)
        self.actionDEL.setObjectName("actionDEL")
        self.actionORwire = QtWidgets.QAction(MainWindow)
        self.actionORwire.setCheckable(True)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/ORwire.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionORwire.setIcon(icon8)
        self.actionORwire.setObjectName("actionORwire")
        self.actionNarrow = QtWidgets.QAction(MainWindow)
        self.actionNarrow.setCheckable(True)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/icons/narrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNarrow.setIcon(icon9)
        self.actionNarrow.setObjectName("actionNarrow")
        self.actionFalling = QtWidgets.QAction(MainWindow)
        self.actionFalling.setCheckable(True)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/icons/falling_button.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFalling.setIcon(icon10)
        self.actionFalling.setObjectName("actionFalling")
        self.actionTimer = QtWidgets.QAction(MainWindow)
        self.actionTimer.setCheckable(True)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/icons/timer_button.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTimer.setIcon(icon11)
        self.actionTimer.setObjectName("actionTimer")
        self.actionCounter = QtWidgets.QAction(MainWindow)
        self.actionCounter.setCheckable(True)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/icons/counter_button.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCounter.setIcon(icon12)
        self.actionCounter.setObjectName("actionCounter")
        self.actionEdit_nTools = QtWidgets.QAction(MainWindow)
        self.actionEdit_nTools.setObjectName("actionEdit_nTools")
        self.actionElemnents = QtWidgets.QAction(MainWindow)
        self.actionElemnents.setObjectName("actionElemnents")
        self.actionWhatsThis = QtWidgets.QAction(MainWindow)
        self.actionWhatsThis.setObjectName("actionWhatsThis")
        self.actionCheck_HW = QtWidgets.QAction(MainWindow)
        self.actionCheck_HW.setObjectName("actionCheck_HW")
        self.actionUSBHelp = QtWidgets.QAction(MainWindow)
        self.actionUSBHelp.setObjectName("actionUSBHelp")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setCheckable(True)
        self.actionSettings.setObjectName("actionSettings")
        self.actionWaltech = QtWidgets.QAction(MainWindow)
        self.actionWaltech.setCheckable(True)
        self.actionWaltech.setChecked(True)
        self.actionWaltech.setAutoRepeat(False)
        self.actionWaltech.setMenuRole(QtWidgets.QAction.ApplicationSpecificRole)
        self.actionWaltech.setObjectName("actionWaltech")
        self.actionArduinoUno = QtWidgets.QAction(MainWindow)
        self.actionArduinoUno.setCheckable(True)
        self.actionArduinoUno.setMenuRole(QtWidgets.QAction.ApplicationSpecificRole)
        self.actionArduinoUno.setObjectName("actionArduinoUno")
        self.actionCheck_HW_2 = QtWidgets.QAction(MainWindow)
        self.actionCheck_HW_2.setObjectName("actionCheck_HW_2")
        self.actionArduinoUno_IO = QtWidgets.QAction(MainWindow)
        self.actionArduinoUno_IO.setObjectName("actionArduinoUno_IO")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionPlus = QtWidgets.QAction(MainWindow)
        self.actionPlus.setCheckable(True)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/icons/plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlus.setIcon(icon13)
        self.actionPlus.setObjectName("actionPlus")
        self.actionMinus = QtWidgets.QAction(MainWindow)
        self.actionMinus.setCheckable(True)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/icons/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMinus.setIcon(icon14)
        self.actionMinus.setObjectName("actionMinus")
        self.actionEquals = QtWidgets.QAction(MainWindow)
        self.actionEquals.setCheckable(True)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/icons/equ.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEquals.setIcon(icon15)
        self.actionEquals.setObjectName("actionEquals")
        self.actionMove = QtWidgets.QAction(MainWindow)
        self.actionMove.setCheckable(True)
        self.actionMove.setEnabled(False)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/icons/move.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMove.setIcon(icon16)
        self.actionMove.setVisible(False)
        self.actionMove.setObjectName("actionMove")
        self.actionDivide = QtWidgets.QAction(MainWindow)
        self.actionDivide.setCheckable(True)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icons/icons/divide.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDivide.setIcon(icon17)
        self.actionDivide.setObjectName("actionDivide")
        self.actionMult = QtWidgets.QAction(MainWindow)
        self.actionMult.setCheckable(True)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/icons/icons/times.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMult.setIcon(icon18)
        self.actionMult.setObjectName("actionMult")
        self.actionGreater = QtWidgets.QAction(MainWindow)
        self.actionGreater.setCheckable(True)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/icons/icons/greater_than.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGreater.setIcon(icon19)
        self.actionGreater.setObjectName("actionGreater")
        self.actionLessthan = QtWidgets.QAction(MainWindow)
        self.actionLessthan.setCheckable(True)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/icons/icons/less_than.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLessthan.setIcon(icon20)
        self.actionLessthan.setObjectName("actionLessthan")
        self.actionGreaterOrEq = QtWidgets.QAction(MainWindow)
        self.actionGreaterOrEq.setCheckable(True)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/icons/icons/greater_than_or_eq.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGreaterOrEq.setIcon(icon21)
        self.actionGreaterOrEq.setObjectName("actionGreaterOrEq")
        self.actionLessOrEq = QtWidgets.QAction(MainWindow)
        self.actionLessOrEq.setCheckable(True)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/icons/icons/less_than_or_eq.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLessOrEq.setIcon(icon22)
        self.actionLessOrEq.setObjectName("actionLessOrEq")
        self.actionPWM = QtWidgets.QAction(MainWindow)
        self.actionPWM.setCheckable(True)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/icons/icons/PWM.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPWM.setIcon(icon23)
        self.actionPWM.setObjectName("actionPWM")
        self.actionADC = QtWidgets.QAction(MainWindow)
        self.actionADC.setCheckable(True)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/icons/icons/ADC.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionADC.setIcon(icon24)
        self.actionADC.setObjectName("actionADC")
        self.actionArduinoMega_IO = QtWidgets.QAction(MainWindow)
        self.actionArduinoMega_IO.setObjectName("actionArduinoMega_IO")
        self.actionArduinoMega = QtWidgets.QAction(MainWindow)
        self.actionArduinoMega.setCheckable(True)
        self.actionArduinoMega.setObjectName("actionArduinoMega")
        self.actionATmega328P_Custom = QtWidgets.QAction(MainWindow)
        self.actionATmega328P_Custom.setCheckable(True)
        self.actionATmega328P_Custom.setObjectName("actionATmega328P_Custom")
        self.actionArduinoNano = QtWidgets.QAction(MainWindow)
        self.actionArduinoNano.setCheckable(True)
        self.actionArduinoNano.setMenuRole(QtWidgets.QAction.ApplicationSpecificRole)
        self.actionArduinoNano.setObjectName("actionArduinoNano")
        self.actionArduinoNano_IO = QtWidgets.QAction(MainWindow)
        self.actionArduinoNano_IO.setObjectName("actionArduinoNano_IO")
        self.actionEnableSerialDebugging = QtWidgets.QAction(MainWindow)
        self.actionEnableSerialDebugging.setCheckable(True)
        self.actionEnableSerialDebugging.setObjectName("actionEnableSerialDebugging")
        self.actionATmega328P_Custom_IO = QtWidgets.QAction(MainWindow)
        self.actionATmega328P_Custom_IO.setObjectName("actionATmega328P_Custom_IO")
        self.toolBar.addAction(self.actionElemnents)
        self.toolBar.addAction(self.actionContNO)
        self.toolBar.addAction(self.actionContNC)
        self.toolBar.addAction(self.actionCoil)
        self.toolBar.addAction(self.actionFalling)
        self.toolBar.addAction(self.actionTimer)
        self.toolBar.addAction(self.actionCounter)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPlus)
        self.toolBar.addAction(self.actionMinus)
        self.toolBar.addAction(self.actionMult)
        self.toolBar.addAction(self.actionDivide)
        self.toolBar.addAction(self.actionMove)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionGreater)
        self.toolBar.addAction(self.actionLessthan)
        self.toolBar.addAction(self.actionGreaterOrEq)
        self.toolBar.addAction(self.actionLessOrEq)
        self.toolBar.addAction(self.actionEquals)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPWM)
        self.toolBar.addAction(self.actionADC)
        self.toolBar.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuHelp.addAction(self.actionWhatsThis)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionUSBHelp)
        self.menuHelp.addAction(self.actionArduinoUno_IO)
        self.menuHelp.addAction(self.actionArduinoNano_IO)
        self.menuHelp.addAction(self.actionArduinoMega_IO)
        self.menuHelp.addAction(self.actionATmega328P_Custom_IO)
        self.menuHelp.addAction(self.actionAbout)
        self.menuDiagnostics.addAction(self.actionWaltech)
        self.menuDiagnostics.addAction(self.actionArduinoUno)
        self.menuDiagnostics.addAction(self.actionArduinoNano)
        self.menuDiagnostics.addAction(self.actionArduinoMega)
        self.menuDiagnostics.addAction(self.actionATmega328P_Custom)
        self.menuDiagnostics.addSeparator()
        self.menuDiagnostics.addAction(self.actionCheck_HW_2)
        self.menuDiagnostics.addSeparator() # Add a separator before this new option
        self.menuDiagnostics.addAction(self.actionEnableSerialDebugging)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuDiagnostics.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.toolBar_2.addAction(self.actionEdit_nTools)
        self.toolBar_2.addAction(self.actionaddRung)
        self.toolBar_2.addAction(self.actionORwire)
        self.toolBar_2.addAction(self.actionWiden)
        self.toolBar_2.addAction(self.actionNarrow)
        self.toolBar_2.addAction(self.actionDEL)

        self.retranslateUi(MainWindow)
        self.actionClose.triggered.connect(MainWindow.close) # type: ignore
        self.undoBbutton.clicked.connect(self.actionUndo.trigger) # type: ignore
        self.redoButton.clicked.connect(self.actionRedo.trigger) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Waltech Ladder Maker"))
        self.label.setText(_translate("MainWindow", "Mouse X:"))
        self.label_3.setText(_translate("MainWindow", "Mouse Y:"))
        self.undoBbutton.setText(_translate("MainWindow", "Undo"))
        self.redoButton.setText(_translate("MainWindow", "Redo"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "I/O"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Elmnt."))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "loc."))
        self.infoButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Create hex file and upload it to the Hardware</p></body></html>"))
        self.infoButton.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>This buton starts the following: </p><p>- creation of C code.  </p><p>- compiling of that cod with GCC</p><p>- uploading of the resulting hex file to the hardware via USB</p></body></html>"))
        self.infoButton.setText(_translate("MainWindow", "compile"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "Elements"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuDiagnostics.setTitle(_translate("MainWindow", "Hardware"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.actionContNO.setText(_translate("MainWindow", "contNO"))
        self.actionContNO.setToolTip(_translate("MainWindow", "Normally Open Contact"))
        self.actionContNO.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#000000;\">Inserts a Normally Open Contact in the ladder. </span><span style=\" font-size:10pt; color:#000000;\"><br/><br/>--A dialog window will appear.<br/>--Choose an input from the dropdown menu.<br/>--If &quot;internal&quot; selected and name is shared, the state will come from a Coil</span><span style=\" color:#000000;\"/></p></body></html>"))
        self.actionContNC.setText(_translate("MainWindow", "contNC"))
        self.actionContNC.setToolTip(_translate("MainWindow", "Normally Closed Contact"))
        self.actionContNC.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Sans Serif\'; font-size:11pt; color:#000000;\">Inserts a Normally Closed Contact in the ladder. <br/><br/>--A dialog window will appear.<br/>--Choose an input from the dropdown menu.<br/>--If &quot;internal&quot; selected and name is shared, the state will come from a Coil </span></p></body></html>"))
        self.actionCoil.setText(_translate("MainWindow", "Coil"))
        self.actionCoil.setToolTip(_translate("MainWindow", "Coil"))
        self.actionCoil.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#000000;\">Inserts a Coil in the ladder. <br/><br/>--A dialog window will appear.<br/>--Choose an Output from the dropdown menu.<br/>--If &quot;internal&quot; selected and name is shared with another element, the state of this coil will pass to that element.</span></p></body></html>"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionUndo.setText(_translate("MainWindow", "undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionaddRung.setText(_translate("MainWindow", "addRung"))
        self.actionaddRung.setToolTip(_translate("MainWindow", "Add a Rung"))
        self.actionaddRung.setWhatsThis(_translate("MainWindow", "<html><head/><body><span style=\" font-size:11pt; color:#000000;\"><p>Add a rung</p><p>Note: rungs can be converted to OR branches with the vertical wire tool.</p></body></html>"))
        self.actionWiden.setText(_translate("MainWindow", "Widen"))
        self.actionWiden.setToolTip(_translate("MainWindow", "Widen rung"))
        self.actionWiden.setWhatsThis(_translate("MainWindow", "<html><head/><body><span style=\" font-size:11pt; color:#000000;\"><p>Makes the entire ladder one element width wider.</p></body></html>"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionDEL.setText(_translate("MainWindow", "DEL"))
        self.actionDEL.setToolTip(_translate("MainWindow", "<html><head/><body><p>Delete an element or empty rung </p></body></html>"))
        self.actionDEL.setWhatsThis(_translate("MainWindow", "<html><head/><body><span style=\" font-size:11pt; color:#000000;\"><p>Delete an element</p><p>Delete an empty rung</p><p>Note: Use the vertical wire (OR) to delete branches. </p></body></html>"))
        self.actionORwire.setText(_translate("MainWindow", "OR wire"))
        self.actionORwire.setToolTip(_translate("MainWindow", "<html><head/><body><p>Toggles vertical wire to to OR branch.</p><p>Connects Rung to Rung below, Becomes OR branch</p></body></html>"))
        self.actionORwire.setWhatsThis(_translate("MainWindow", "<html><head/><body><span style=\" font-size:11pt; color:#000000;\"><p>--Click to add or remove a vertical wire</p><p>--This tool can link rungs together to make an OR branch.</p><p>--Use this tool to widen or shrink the OR branch</p></body></html>"))
        self.actionNarrow.setText(_translate("MainWindow", "Narrow"))
        self.actionNarrow.setToolTip(_translate("MainWindow", "Remove extra empty locations"))
        self.actionNarrow.setWhatsThis(_translate("MainWindow", "<html><head/><body><span style=\" font-size:11pt; color:#000000;\"><p>Narrows the ladder by one element width</p></body></html>"))
        self.actionFalling.setText(_translate("MainWindow", "falling"))
        self.actionFalling.setToolTip(_translate("MainWindow", "Falling edge"))
        self.actionFalling.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#000000;\">Inserts a falling Edge in the ladder. <br/><br/>--Creates a 10ns pulse on the rung-out when a falling edge is dected at the rung-in</span><br/></p></body></html>"))
        self.actionTimer.setText(_translate("MainWindow", "Timer"))
        self.actionTimer.setToolTip(_translate("MainWindow", "Timer"))
        self.actionTimer.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#000000;\">Inserts a Timer in the ladder. <br/><br/>--A dialog window will appear.<br/>--Set the time delay.  10 min max (655 sec)<br/>--If rung-in state goes True and stays that way for the delay duration, the rung-out will go True.  <br/>--Timer is reset when the rung-in state goes False</p></body></html>"))
        self.actionCounter.setText(_translate("MainWindow", "Counter"))
        self.actionCounter.setToolTip(_translate("MainWindow", "Counter"))
        self.actionCounter.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#000000;\">Inserts a Counter in the ladder. <br/><br/>--A dialog window will appear.<br/>--Set the number of counts (setpoint).  65535 max.<br/>--If rung-in state goes True setpoint number of times, the rung-out will go True. <br/>--Choose a name.  If shared with a Coil, this will provide a Reset.</p></body></html>"))
        self.actionEdit_nTools.setText(_translate("MainWindow", "Edit"))
        self.actionElemnents.setText(_translate("MainWindow", "Elemnents"))
        self.actionWhatsThis.setText(_translate("MainWindow", "WhatsThis"))
        self.actionWhatsThis.setToolTip(_translate("MainWindow", "<html><head/><body><p>Click this to get help with a tool</p></body></html>"))
        self.actionCheck_HW.setText(_translate("MainWindow", "Test Hardware"))
        self.actionCheck_HW.setToolTip(_translate("MainWindow", "<html><head/><body><p>Checks USB</p></body></html>"))
        self.actionCheck_HW.setWhatsThis(_translate("MainWindow", "Checks USB connection, programmer, and controller."))
        self.actionUSBHelp.setText(_translate("MainWindow", "USB"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionWaltech.setText(_translate("MainWindow", "Waltech"))
        self.actionArduinoUno.setText(_translate("MainWindow", "Arduino Uno"))
        self.actionCheck_HW_2.setText(_translate("MainWindow", "Test USB"))
        self.actionCheck_HW_2.setToolTip(_translate("MainWindow", "Test USB connection, drver, programmer, hardware"))
        self.actionArduinoUno_IO.setText(_translate("MainWindow", "Arduino Uno IO"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionPlus.setText(_translate("MainWindow", "Plus"))
        self.actionPlus.setWhatsThis(_translate("MainWindow", "<html><head/><body><span style=\" font-size:11pt; color:#000000;\"><p>Add. </p><p>Must be paced on far right.</p><p>Sources can be a constant or a name of another element. </p><p>sources and result are 16 bit signed.  (-32767 to 32767)</p></body></html>"))
        self.actionMinus.setText(_translate("MainWindow", "minus"))
        self.actionMinus.setWhatsThis(_translate("MainWindow", "<html><head/><body><span style=\" font-size:11pt; color:#000000;\"><p>Subtract. </p><p>Must be paced on far right.</p><p>Sources can be a constant or a name of another element. </p><p>sources and result are 16 bit signed.  (-32767 to 32767)</p><p><br/></p></body></html>"))
        self.actionEquals.setText(_translate("MainWindow", "equals"))
        self.actionEquals.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Comparison: Equals.</p><p>Conductive if true.</p><p>Sources can be a constant or a name of another element. </p><p><br/></p></body></html>"))
        self.actionMove.setText(_translate("MainWindow", "move"))
        self.actionDivide.setText(_translate("MainWindow", "divide"))
        self.actionDivide.setWhatsThis(_translate("MainWindow", "<html><head/><body><span style=\" font-size:11pt; color:#000000;\"><p>Divide. </p><p>Must be paced on far right.</p><p>Sources can be a constant or a name of another element. </p><p>sources and result are 16 bit signed.  (-32767 to 32767)</p><p>Divide by zero OK.</p></body></html>"))
        self.actionMult.setText(_translate("MainWindow", "mult"))
        self.actionMult.setWhatsThis(_translate("MainWindow", "<html><head/><body><span style=\" font-size:11pt; color:#000000;\"><p>Multiply.</p><p>Must be paced on far right.</p><p>Sources can be a constant or a name of another element. </p><p>sources and result are 16 bit signed.  (-32767 to 32767)</p></body></html>"))
        self.actionGreater.setText(_translate("MainWindow", "greater"))
        self.actionGreater.setWhatsThis(_translate("MainWindow", "<html><head/><body><span style=\" font-size:11pt; color:#000000;\"><p>Comparison: Greater Than.</p><p>Conductive if true.</p><p>Sources can be a constant or a name of another element.</p></body></html>"))
        self.actionLessthan.setText(_translate("MainWindow", "lessthan"))
        self.actionLessthan.setWhatsThis(_translate("MainWindow", "<html><head/><body><span style=\" font-size:11pt; color:#000000;\"><p>Comparison: Less Than.</p><p>Conductive if true.</p><p>Sources can be a constant or a name of another element.</p></body></html>"))
        self.actionGreaterOrEq.setText(_translate("MainWindow", "greaterOrEq"))
        self.actionGreaterOrEq.setWhatsThis(_translate("MainWindow", "<html><head/><body><span style=\" font-size:11pt; color:#000000;\"><p>Comparison: Greater Than or Equal.</p><p>Conductive if true.</p><p>Sources can be a constant or a name of another element.</p></body></html>"))
        self.actionLessOrEq.setText(_translate("MainWindow", "lessOrEq"))
        self.actionLessOrEq.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Comparison: Less Than or Equal.</p><p>Conductive if true.</p><p>Sources can be a constant or a name of another element.</p></body></html>"))
        self.actionPWM.setText(_translate("MainWindow", "PWM"))
        self.actionPWM.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Pulse width modulated output. </span></p><p><span style=\" color:#000000;\">Must be placed on far right.</span></p><p><span style=\" color:#000000;\">Active if rung in state True.</span></p><p><span style=\" color:#000000;\">Menu item will be greyed if PWM not available on this hardware.</span></p><p><span style=\" color:#000000;\">If output set to &quot;Internal&quot; PWM will be de-activated</span></p><p><span style=\" color:#000000;\">NOTES:</span></p><p><span style=\" color:#000000;\">If two PWM elements exist in the ladder with the same hardware output, the first active one will apply. This allows to set a single output to different levels.</span></p><p><span style=\" color:#000000;\">The PWM frequency is fixed at 16khz. </span></p></body></html>"))
        self.actionADC.setText(_translate("MainWindow", "ADC"))
        self.actionADC.setWhatsThis(_translate("MainWindow", "<html><head/><body><span style=\" font-size:11pt; color:#000000;\"><p>ADC. Measure Voltage.</p><p>Ten bit output (0 to 1024)</p><p>5v (AVcc) refrence.  value = (Vin x 1024)÷5</p><p>Must be placed on far right.</p><p>Active if rung in state True.</p><p>Menu item will be greyed if ADC not available on this hardware.</p><p>if input set to &quot;Internal&quot; ADC will be de-activated.</p><p><br/></p></body></html>"))
        self.actionArduinoMega_IO.setText(_translate("MainWindow", "Arduino Mega IO"))
        self.actionArduinoMega.setText(_translate("MainWindow", "Arduino Mega"))
        self.actionATmega328P_Custom.setText(_translate("MainWindow", "ATmega328P Custom"))
        self.actionArduinoNano.setText(_translate("MainWindow", "Arduino Nano"))
        self.actionArduinoNano_IO.setText(_translate("MainWindow", "Arduino Nano IO"))
        self.actionATmega328P_Custom_IO.setText(_translate("MainWindow", "ATmega328P Custom IO"))
        self.actionEnableSerialDebugging.setText(_translate("MainWindow", "Enable Basic Serial Prints"))
import toolbaricons_rc
