import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from Ui_untitled import Ui_MainWindow
 
 
class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.button_click(self.pushButton))
        self.pushButton_2.clicked.connect(lambda: self.button_click(self.pushButton_2))
        self.pushButton_3.clicked.connect(lambda: self.button_click(self.pushButton_3))
        self.pushButton_4.clicked.connect(lambda: self.button_click(self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda: self.button_click(self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda: self.button_click(self.pushButton_6))
        self.pushButton_7.clicked.connect(lambda: self.button_click(self.pushButton_7))
        self.pushButton_8.clicked.connect(lambda: self.button_click(self.pushButton_8))
        self.pushButton_9.clicked.connect(lambda: self.button_click(self.pushButton_9))
        self.pushButton_0.clicked.connect(lambda: self.button_click(self.pushButton_0))
        self.pushButton_plus.clicked.connect(lambda: self.plus())
        self.pushButton_minus.clicked.connect(lambda: self.minus())
        self.pushButton_multiply.clicked.connect(lambda: self.multiply())
        self.pushButton_divide.clicked.connect(lambda: self.divide())
        self.pushButton_equal.clicked.connect(lambda: self.caculation())
        self.pushButton_back.clicked.connect(lambda: self.clear())
        
    def button_click(self, key):
        self.textBrowser_equation.insertPlainText(key.text())
    def clear(self):
        self.textBrowser_equation.clear()
    def caculation(self):
        if len(self.textBrowser_equation.toPlainText()) != 0:
            result='{:.6f}'.format(eval(self.textBrowser_equation.toPlainText()))
            self.textBrowser_result.insertPlainText(result)
    def plus(self):
        self.textBrowser_equation.insertPlainText('+')
    def minus(self):
        self.textBrowser_equation.insertPlainText('-')
    def multiply(self):
        self.textBrowser_equation.insertPlainText('*')
    def divide(self):
        self.textBrowser_equation.insertPlainText('/')
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())   
