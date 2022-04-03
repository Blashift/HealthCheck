from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QWidget

txt_title ='Здоровье'
win_x, win_y = 200, 100
win_width, win_height = 1000, 600
txt_hello = 'Добро пожаловать в программу по определению состояния здоровья!'
txt_instruction = 'Данное приложение позволит вам с помощью теста Руфье '
txt_next = 'НАЧАТЬ'

class MainWin(QWidget):
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLable(txt_instruction)
        self.button = QPushButton(txt_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text)
        self.layout.addWidget(self.instruction)
        self.Layout.addWidget(self.button)
    def connects (self):
        self.bnt_next.clicked.connect(self.next_click)
    def next_click(self):
        self.window.hide()
        self.tw =TestWin()
    app = QCoreApplication([])
    mw = MainWin(TestWin)
    app.exec_()

class MainWin(QWidget):
    def set_appear(self):
        pass
    def initUI(self):
        pass
    def connects (self):
        pass
    def next_click(self):
        self.window.hide()
        self.tw =TestWin()

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear(self)
        self.initUI(self)
        self.connects(self)
        self.show()

class TestWin(QWidget):
    def __init__(self):
        super().__init__(self)
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()