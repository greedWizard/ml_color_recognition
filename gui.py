# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from algs.color_pick import kns_class, train_set, colors_dict, k


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(483, 390)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.colorLabel = QtWidgets.QLabel(self.centralwidget)
        self.colorLabel.setText("")
        self.colorLabel.setObjectName("colorLabel")
        self.verticalLayout.addWidget(self.colorLabel)
        self.resultLabel = QtWidgets.QLabel(self.centralwidget)
        self.resultLabel.setEnabled(True)
        self.resultLabel.setObjectName("resultLabel")
        self.verticalLayout.addWidget(self.resultLabel)
        self.colorChangeButton = QtWidgets.QPushButton(self.centralwidget)
        self.colorChangeButton.setObjectName("colorChangeButton")
        self.verticalLayout.addWidget(self.colorChangeButton)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 483, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.colorChangeButton.clicked.connect(self.color_picker)

        self.color = (255, 255, 255)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.predict_color)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ColorDetector v1.0"))
        self.resultLabel.setText(_translate("MainWindow", "None"))
        self.colorChangeButton.setText(_translate("MainWindow", "Pick Color"))
        self.pushButton.setText(_translate("MainWindow", "Detect"))

    def color_picker(self):
        self.color = QtWidgets.QColorDialog.getColor()
        self.color = [self.color.red(), self.color.green(), self.color.blue()]

        qcolor = QtGui.QColor(self.color[0], self.color[1], self.color[2])

        self.colorLabel.setStyleSheet('QWidget {background-color: %s}' % qcolor.name())

    def predict_color(self):
        vote = kns_class(train_set, self.color, k=k)
        result = colors_dict[vote]

        self.resultLabel.setText(result)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())