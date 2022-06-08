from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time

class Main_pic(QThread):
    time = pyqtSignal(int)    # 사용자 정의 시그널

    def __init__(self):
        super().__init__()
        self.num = 0           # 초깃값 설정
        self.num2=0
    def run(self):
        while True:
            self.time.emit(self.num)     # 방출
            self.num += 1
            time.sleep(1)
            if self.num>=6:
                self.num=0

