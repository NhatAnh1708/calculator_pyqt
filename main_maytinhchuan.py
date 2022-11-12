import sys 
from PyQt5 import QtWidgets
from MayTinhChuan import Ui_MainWindow
import numpy as np



class MainWindow:
    def __init__(self) :
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.ui.AC_button.clicked.connect(lambda: self.pressed_it("AC"))
        self.ui.plus_minus_button.clicked.connect(lambda: self.pressed_plus_minus())
        self.ui.phantram_button.clicked.connect(lambda: self.pressed_phantram())
        self.ui.minus_button.clicked.connect(lambda: self.pressed_it("/"))
        self.ui.seven_button.clicked.connect(lambda: self.pressed_it("7"))
        self.ui.eight_button.clicked.connect(lambda: self.pressed_it("8"))
        self.ui.nine_button.clicked.connect(lambda: self.pressed_it("9"))
        self.ui.nhan_button.clicked.connect(lambda: self.pressed_it("*"))
        self.ui.four_button.clicked.connect(lambda: self.pressed_it("4"))
        self.ui.five_button.clicked.connect(lambda: self.pressed_it("5"))
        self.ui.six_button.clicked.connect(lambda: self.pressed_it("6"))
        self.ui.chia_button.clicked.connect(lambda: self.pressed_it("-"))
        self.ui.one_button.clicked.connect(lambda: self.pressed_it("1"))
        self.ui.two_button.clicked.connect(lambda: self.pressed_it("2"))
        self.ui.three_button.clicked.connect(lambda: self.pressed_it("3"))
        self.ui.cong_button.clicked.connect(lambda: self.pressed_it("+"))
        self.ui.zero_button.clicked.connect(lambda: self.pressed_it("0"))
        self.ui.phay_button.clicked.connect(lambda: self.pressed_it("."))
        self.ui.bang_button.clicked.connect(lambda: self.pressed_equal())
    def show(self): # ham de show man hinh
        self.MainWindow.show()  
    def pressed_plus_minus(self): # ham de doi dau 
        screen1 = self.ui.screen_button.text()
        if "-"  in screen1:
            self.ui.screen_button.setText(screen1.replace("-"," "))
        else:
            self.ui.screen_button.setText(f'-{screen1}')
    # def pressed_Arrow(self):
    #     screen1 = self.ui.screen_button.text()
    #     screen1 = screen1[:-1]
    #     self.ui.screen_button.setText(screen1)
    def pressed_phantram(self):
        screen1 = self.ui.screen_button.text()
        self.ui.screen_button.setText(f'{screen1}*0.01')
    def pressed_it(self,pressed): #ham de hien thi
        
        
        if pressed == "AC":
            self.ui.screen_button.setText("0")
        elif pressed == "x":
            self.ui.screen_button.setText("*")
        # elif pressed == "÷":  # bi loi hien thi chi hien thi ra /
        #     self.ui.screen_button.setText("/")
        else:
            if self.ui.screen_button.text() == "0":
                self.ui.screen_button.setText("")
            self.ui.screen_button.setText(f'{self.ui.screen_button.text()}{pressed}')    
    def phantram(x):
        return x*0.01
    
    def pressed_equal(self):    # ham tinh toan
        screen1 = self.ui.screen_button.text()
        try:
            result = np.round(eval(screen1),5)
            self.ui.screen_button.setText(str(result))
            
        except:
            self.ui.screen_button("Error")
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())


    
