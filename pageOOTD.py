from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class PageOOTD:
    def __init__(self,ui,db):
        self.ui=ui
        self.db=db
        self.btnEvent()

    
    def btnEvent(self):
        self.ui.scheduleBtn.clicked.connect(lambda event:self.btnOOTD())
        self.ui.ootdBackBtn.clicked.connect(lambda event:self.backEvent())

    def btnOOTD(self):
        dialog=QtWidgets.QDialog()
        self.ui.dialogOOTDCheck(dialog)
        dialog.show()
        
    def dialogOOTDCheck(self):
        print()


    def backEvent(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.PageMain)
        
        