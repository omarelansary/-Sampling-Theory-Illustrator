# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Final.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1259, 895)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Reconstructed_Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Reconstructed_Label.setFont(font)
        self.Reconstructed_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Reconstructed_Label.setObjectName("Reconstructed_Label")
        self.verticalLayout_5.addWidget(self.Reconstructed_Label)
        # self.Reconstructed_View = QtWidgets.QGraphicsView(self.centralwidget)
        self.Reconstructed_View = PlotWidget(self.centralwidget)

        self.Reconstructed_View.setObjectName("Reconstructed_View")
        self.verticalLayout_5.addWidget(self.Reconstructed_View)
        self.gridLayout.addLayout(self.verticalLayout_5, 2, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.SignalPreview_Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SignalPreview_Label.setFont(font)
        self.SignalPreview_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.SignalPreview_Label.setObjectName("SignalPreview_Label")
        self.verticalLayout_3.addWidget(self.SignalPreview_Label)
        self.Composed_View = QtWidgets.QGraphicsView(self.centralwidget)
        self.Composed_View.setObjectName("Composed_View")
        self.verticalLayout_3.addWidget(self.Composed_View)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 3, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.AllSignals_Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AllSignals_Label.setFont(font)
        self.AllSignals_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.AllSignals_Label.setObjectName("AllSignals_Label")
        self.verticalLayout_7.addWidget(self.AllSignals_Label)
        self.Signal_List = QtWidgets.QListWidget(self.centralwidget)
        self.Signal_List.setObjectName("Signal_List")
        self.verticalLayout_7.addWidget(self.Signal_List)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Delete_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Delete_pushButton.setObjectName("Delete_pushButton")
        self.horizontalLayout_3.addWidget(self.Delete_pushButton)
        self.ViewInPrimary_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ViewInPrimary_pushButton.setObjectName("ViewInPrimary_pushButton")
        self.horizontalLayout_3.addWidget(self.ViewInPrimary_pushButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_7, 2, 5, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.PrimarySignal_Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PrimarySignal_Label.setFont(font)
        self.PrimarySignal_Label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PrimarySignal_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.PrimarySignal_Label.setObjectName("PrimarySignal_Label")
        self.verticalLayout.addWidget(self.PrimarySignal_Label)
        # self.Illustrator_View = QtWidgets.QGraphicsView(self.centralwidget)
        self.Illustrator_View =  PlotWidget(self.centralwidget)

        self.Illustrator_View.setObjectName("Illustrator_View")
        self.verticalLayout.addWidget(self.Illustrator_View)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_12.addWidget(self.label)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Example_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Example_label.setFont(font)
        self.Example_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Example_label.setObjectName("Example_label")
        self.verticalLayout_4.addWidget(self.Example_label)
        self.verticalLayout_12.addLayout(self.verticalLayout_4)
        self.verticalLayout_11.addLayout(self.verticalLayout_12)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.A_Label = QtWidgets.QLabel(self.centralwidget)
        self.A_Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.A_Label.setFont(font)
        self.A_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.A_Label.setObjectName("A_Label")
        self.verticalLayout_8.addWidget(self.A_Label)
        self.A_Text = QtWidgets.QLineEdit(self.centralwidget)
        self.A_Text.setText("1")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.A_Text.sizePolicy().hasHeightForWidth())
        self.A_Text.setSizePolicy(sizePolicy)
        self.A_Text.setMinimumSize(QtCore.QSize(0, 0))
        self.A_Text.setMaximumSize(QtCore.QSize(16777215, 30))
        self.A_Text.setObjectName("A_Text")
        self.verticalLayout_8.addWidget(self.A_Text)
        self.verticalLayout_11.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.F_Label = QtWidgets.QLabel(self.centralwidget)
        self.F_Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.F_Label.setFont(font)
        self.F_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.F_Label.setObjectName("F_Label")
        self.verticalLayout_9.addWidget(self.F_Label)
        self.F_Text = QtWidgets.QLineEdit(self.centralwidget)
        self.F_Text.setText("1")      
        self.F_Text.setMaximumSize(QtCore.QSize(16777215, 30))
        self.F_Text.setObjectName("F_Text")
        self.verticalLayout_9.addWidget(self.F_Text)
        self.verticalLayout_11.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.Theta_Label = QtWidgets.QLabel(self.centralwidget)
        self.Theta_Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Theta_Label.setFont(font)
        self.Theta_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Theta_Label.setObjectName("Theta_Label")
        self.verticalLayout_10.addWidget(self.Theta_Label)
        self.Theta_Text = QtWidgets.QLineEdit(self.centralwidget)
        self.Theta_Text.setText("45")
        self.Theta_Text.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Theta_Text.setObjectName("Theta_Text")
        self.verticalLayout_10.addWidget(self.Theta_Text)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Preview_pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Preview_pushButton.setFont(font)
        self.Preview_pushButton.setObjectName("Preview_pushButton")
        self.horizontalLayout_2.addWidget(self.Preview_pushButton)
        self.Add_pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Add_pushButton.setFont(font)
        self.Add_pushButton.setObjectName("Add_pushButton")
        self.horizontalLayout_2.addWidget(self.Add_pushButton)
        self.verticalLayout_11.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_11, 0, 5, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.SignalPreview_Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SignalPreview_Label.setFont(font)
        self.SignalPreview_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.SignalPreview_Label.setObjectName("SignalPreview_Label")
        self.verticalLayout_3.addWidget(self.SignalPreview_Label)
        self.Composed_View =  PlotWidget(self.centralwidget)
        self.Composed_View.setObjectName("Composed_View")
        self.verticalLayout_3.addWidget(self.Composed_View)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 3, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Fmax0_Label = QtWidgets.QLabel(self.centralwidget)
        self.Fmax0_Label.setMaximumSize(QtCore.QSize(30, 16777215))
        self.Fmax0_Label.setObjectName("Fmax0_Label")
        self.horizontalLayout.addWidget(self.Fmax0_Label)
        spacerItem1 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.Fmax1_Label = QtWidgets.QLabel(self.centralwidget)
        self.Fmax1_Label.setMaximumSize(QtCore.QSize(30, 16777215))
        self.Fmax1_Label.setObjectName("Fmax1_Label")
        self.horizontalLayout.addWidget(self.Fmax1_Label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.Fmax2_Label = QtWidgets.QLabel(self.centralwidget)
        self.Fmax2_Label.setMaximumSize(QtCore.QSize(30, 16777215))
        self.Fmax2_Label.setObjectName("Fmax2_Label")
        self.horizontalLayout.addWidget(self.Fmax2_Label)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.Fmax3_Label = QtWidgets.QLabel(self.centralwidget)
        self.Fmax3_Label.setMaximumSize(QtCore.QSize(30, 16777215))
        self.Fmax3_Label.setObjectName("Fmax3_Label")
        self.horizontalLayout.addWidget(self.Fmax3_Label)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.Fmax4_Label = QtWidgets.QLabel(self.centralwidget)
        self.Fmax4_Label.setMaximumSize(QtCore.QSize(30, 16777215))
        self.Fmax4_Label.setObjectName("Fmax4_Label")
        self.horizontalLayout.addWidget(self.Fmax4_Label)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.Illustrator_Frequency_Slider = QtWidgets.QSlider(self.centralwidget)
        self.Illustrator_Frequency_Slider.setMaximumSize(QtCore.QSize(16777215, 10))
        self.Illustrator_Frequency_Slider.setSingleStep(1)
        self.Illustrator_Frequency_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Illustrator_Frequency_Slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.Illustrator_Frequency_Slider.setTickInterval(33)
        self.Illustrator_Frequency_Slider.setObjectName("Illustrator_Frequency_Slider")
        self.verticalLayout_2.addWidget(self.Illustrator_Frequency_Slider)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 4, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.AllSignals_Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AllSignals_Label.setFont(font)
        self.AllSignals_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.AllSignals_Label.setObjectName("AllSignals_Label")
        self.verticalLayout_7.addWidget(self.AllSignals_Label)
        self.Signal_List = QtWidgets.QListWidget(self.centralwidget)
        self.Signal_List.setObjectName("Signal_List")
        self.verticalLayout_7.addWidget(self.Signal_List)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Delete_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Delete_pushButton.setObjectName("Delete_pushButton")
        self.horizontalLayout_3.addWidget(self.Delete_pushButton)
        self.ViewInPrimary_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ViewInPrimary_pushButton.setObjectName("ViewInPrimary_pushButton")
        self.horizontalLayout_3.addWidget(self.ViewInPrimary_pushButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_7, 2, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 5, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.AddedSignal_Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AddedSignal_Label.setFont(font)
        self.AddedSignal_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.AddedSignal_Label.setObjectName("AddedSignal_Label")
        self.verticalLayout_6.addWidget(self.AddedSignal_Label)
        self.AddedSignal_View =  PlotWidget(self.centralwidget)
        self.AddedSignal_View.setObjectName("AddedSignal_View")
        self.verticalLayout_6.addWidget(self.AddedSignal_View)
        self.gridLayout.addLayout(self.verticalLayout_6, 2, 3, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 1, 5, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1259, 26))
        self.menubar.setObjectName("menubar")
        self.menuBrowse = QtWidgets.QMenu(self.menubar)
        self.menuBrowse.setObjectName("menuBrowse")
        self.menuSave = QtWidgets.QMenu(self.menubar)
        self.menuSave.setObjectName("menuSave")
        self.menuVeiw = QtWidgets.QMenu(self.menubar)
        self.menuVeiw.setObjectName("menuVeiw")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_File = QtWidgets.QAction(MainWindow)
        self.actionSave_File.setObjectName("actionSave_File")
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionHide_Reconstructed_Signal = QtWidgets.QAction(MainWindow)
        self.actionHide_Reconstructed_Signal.setObjectName("actionHide_Reconstructed_Signal")
        self.actionShow_Reconstructed_Signal = QtWidgets.QAction(MainWindow)
        self.actionShow_Reconstructed_Signal.setObjectName("actionShow_Reconstructed_Signal")
        self.menuBrowse.addAction(self.actionOpen_File)

        self.menuSave.addAction(self.actionSave_File)
        self.menuVeiw.addAction(self.actionHide_Reconstructed_Signal)
        self.menuVeiw.addAction(self.actionShow_Reconstructed_Signal)
        self.menubar.addAction(self.menuBrowse.menuAction())
        self.menubar.addAction(self.menuSave.menuAction())
        self.menubar.addAction(self.menuVeiw.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Reconstructed_Label.setText(_translate("MainWindow", "Reconstructed Signal"))
        self.SignalPreview_Label.setText(_translate("MainWindow", "Signal Preview"))
        self.AllSignals_Label.setText(_translate("MainWindow", "All Signals list"))
        self.Delete_pushButton.setText(_translate("MainWindow", "Delete Selected Signal"))
        self.ViewInPrimary_pushButton.setText(_translate("MainWindow", "View in Primary"))
        self.PrimarySignal_Label.setText(_translate("MainWindow", "Primary Signal"))
        self.label.setText(_translate("MainWindow", "Construct Your Signal"))
        self.Example_label.setText(_translate("MainWindow", "Ex: ASin(wt+Shift)"))
        self.A_Label.setText(_translate("MainWindow", "Amplitude"))
     
        self.F_Label.setText(_translate("MainWindow", "Freq (Hz)"))
        self.Theta_Label.setText(_translate("MainWindow", "Shift (deg)"))
        self.Preview_pushButton.setText(_translate("MainWindow", "Preview"))
        self.Add_pushButton.setText(_translate("MainWindow", "Add"))
        self.Fmax0_Label.setText(_translate("MainWindow", "0 FM"))
        self.Fmax1_Label.setText(_translate("MainWindow", "1 FM"))
        self.Fmax2_Label.setText(_translate("MainWindow", "2 FM"))
        self.Fmax3_Label.setText(_translate("MainWindow", "3 Fm"))
        self.Fmax4_Label.setText(_translate("MainWindow", "4 FM"))
        self.SignalPreview_Label.setText(_translate("MainWindow", "Signal Preview"))
        self.Fmax0_Label.setText(_translate("MainWindow", "0 "))
        self.Fmax1_Label.setText(_translate("MainWindow", "1FM"))
        self.Fmax2_Label.setText(_translate("MainWindow", "2FM"))
        self.Fmax3_Label.setText(_translate("MainWindow", "3FM "))
        self.Fmax4_Label.setText(_translate("MainWindow", "4FM "))
        self.AllSignals_Label.setText(_translate("MainWindow", "All Signals list"))
        self.Delete_pushButton.setText(_translate("MainWindow", "Delete Selected Signal"))
        self.ViewInPrimary_pushButton.setText(_translate("MainWindow", "View in Primary"))
        self.AddedSignal_Label.setText(_translate("MainWindow", "Added Signals"))
        self.menuBrowse.setTitle(_translate("MainWindow", "Browse..."))
        self.menuSave.setTitle(_translate("MainWindow", "Save"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))

        self.menuVeiw.setTitle(_translate("MainWindow", "View"))
        self.actionSave_File.setText(_translate("MainWindow", "Save File "))
        self.actionHide_Reconstructed_Signal.setText(_translate("MainWindow", "Hide Reconstructed Signal"))
        self.actionShow_Reconstructed_Signal.setText(_translate("MainWindow", "Show Reconstructed Signal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
