from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("YOUTUBE MP3 CONVERTER")
        MainWindow.resize(640, 421)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 641, 381))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout.addItem(spacerItem1, 2, 3, 1, 1)

        # Add a QHeaderView to the listView
        self.listView = QtWidgets.QListView(parent=self.gridLayoutWidget)
        self.listView.setObjectName("listView")
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listView.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.gridLayout.addWidget(self.listView, 5, 3, 1, 1)

        # Create the model and add it to the listView
        self.model = QtGui.QStandardItemModel(self.listView)
        self.model.setHorizontalHeaderLabels(["Checkbox", "URL"])
        self.listView.setModel(self.model)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 4, 1, 1)

        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 1, 1, 1)

        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem3, 9, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout.addItem(spacerItem4, 6, 3, 1, 1)

        self.pushButton_2 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 7, 3, 1, 1)

        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem5, 3, 7, 1, 1)

        self.pushButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 5, 1, 1)

        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem6, 3, 0, 1, 1)

        self.lineEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 3, 1, 1)

        self.pushButton_3 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 5, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        spacerItem7 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout.addItem(spacerItem7, 10, 3, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 9, 3, 1, 1)

        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YOUTUBE MP3 CONVERTER"))
        self.label.setText(_translate("MainWindow", "Youtube URL"))
        self.pushButton_2.setText(_translate("MainWindow", "Convert To MP3"))
        self.pushButton.setText(_translate("MainWindow", "ADD"))
        self.pushButton_3.setText(_translate("MainWindow", "DEL"))