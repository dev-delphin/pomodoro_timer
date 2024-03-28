import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Pomodoro TImer'
        self.left = 570
        self.top = 570
        self.setFixedSize(400,400)
        #self.width = 400
        #self.height = 400
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        #self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox + 40
        #self.textbox 
        self.label = QLabel("<font color=black size=4 face=Arial>Введите время концентрации в минутах.</font>", self)
        self.label.move(20,20)
        self.label.resize(360,20)
        self.concentration = QLineEdit(self,placeholderText="Введите время концентрации в минутах.")
        self.concentration.move(20, 40)
        self.concentration.resize(360,40)
        # Create textbox
        self.label = QLabel("<font color=black size=4 face=Arial>Введите время короткого перерыва в минутах.</font>", self)
        self.label.move(20,100)
        self.label.resize(360,20)
        self.short_pereriv = QLineEdit(self,placeholderText="Введите время короткого перерыва в минутах.")
        self.short_pereriv.move(20, 120)
        self.short_pereriv.resize(360,40)
        ## Create textbox
        self.label = QLabel("<font color=black size=4 face=Arial>Введите время длинного перерыва в минутах.</font>", self)
        self.label.move(20,180)
        self.label.resize(360,20)
        self.long_pereriv = QLineEdit(self,placeholderText="Введите время длинного перерыва в минутах.")
        self.long_pereriv.move(20, 200)
        self.long_pereriv.resize(360,40)
        ## Create textbox
        self.label = QLabel("<font color=black size=4 face=Arial>Введите количество циклов.</font>", self)
        self.label.move(20,260)
        self.label.resize(360,20)
        self.cycle = QLineEdit(self,placeholderText="Введите количество циклов.")
        self.cycle.move(20, 280)
        self.cycle.resize(360,40)
        #
        # Create a button in the window
        self.button = QPushButton('Start', self)
        self.button.move(150,340)
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
    
    @pyqtSlot()
    def on_click(self):
        conc = self.concentration.text()
        short_pereriv = self.short_pereriv.text()
        long_pereriv = self.long_pereriv.text()
        cycle = self.cycle.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + conc + short_pereriv + long_pereriv, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())