import sys
from uiface import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('My Title')

        self.ui.pushButton.clicked.connect(self.countSimbol)

    def countSimbol(self):
        self.ui.label.setText("Длина Вашего текста %d" % len(self.ui.lineEdit.text()))   
                
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
