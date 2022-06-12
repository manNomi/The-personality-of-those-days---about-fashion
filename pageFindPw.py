import re

from tkinter import font
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
import sys
class FindPw:
    def __init__ (self,UI,db):
        self.db=db
        self.ui=UI
        self.btnPwBackMover()
        self.findPwRun()

    def find(self,name,email,birth):
        findInfo=self.db.readData("user",["name","id","birth"],[name,email,birth],self.db.cursor1)
        if len(findInfo)==0:
            dialogError=QtWidgets.QDialog()
            self.ui.dialogError(dialogError,"정보를 찾을 수 없습니다.")
            dialogError.show()
            dialogError.exec()
        else:
            printstr="찾았습니다\npw는 "+ findInfo[0][3] +" 입니다."
            dialogError=QtWidgets.QDialog()
            self.ui.dialogError(dialogError,printstr)
            dialogError.show()
            dialogError.exec()
    
    def editClear(self):
        self.ui.findPwName.setText("")
        self.ui.findPwID.setText("")
        self.ui.findPwBirth.setText("")


    def btnPwBackMover(self):
        self.ui.findPwBacktoLogin.clicked.connect(self.backtoLoginMove)
    def backtoLoginMove(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.loginPage)

            
    def findPwRun(self):
        self.ui.findPwBtn.clicked.connect(self.findPwEnter)

    def findPwEnter(self):
        self.myName=self.ui.findPwName.text() 
        self.myEmail=self.ui.findPwID.text()
        self.myBirth=self.ui.findPwBirth.text()
        print(self.myName,self.myBirth)
        self.find(self.myName,self.myEmail,self.myBirth)
        self.editClear()
        self.ui.stackedWidget.setCurrentWidget(self.ui.loginPage)