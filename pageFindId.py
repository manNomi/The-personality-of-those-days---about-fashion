from sympy import Id
import re
from tkinter import font
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
import sys
class FindId:
    def __init__ (self,UI,db):
        self.db=db
        self.ui=UI
        self.btnIdBackMover()
        self.findIdRun()

    def editClear(self):
        self.ui.findIdName.setText("")
        self.ui.findIdBirth.setText("")

    def find(self,name,birth):
        findInfo=self.db.readData("user",["name","birth"],[name,birth],self.db.cursor1)
        print(findInfo)
        if len(findInfo)==0:
            dialogError=QtWidgets.QDialog()
            self.ui.dialogError(dialogError,"정보를 찾을 수 없습니다.")
            dialogError.show()
            dialogError.exec()
        else:
            dialogError=QtWidgets.QDialog()
            printstring="찾았습니다\nEmail은 "+findInfo[0][2]+" 입니다."
            self.ui.dialogError(dialogError,printstring)
            dialogError.show()
            dialogError.exec()


    def btnIdBackMover(self):
        self.ui.findIdBacktoLogin.clicked.connect(self.backtoLoginMove)
    def backtoLoginMove(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.loginPage)
    
    def findIdRun(self):
        self.ui.findIdBtn.clicked.connect(self.findIdEnter)

    def findIdEnter(self):
        self.myName=self.ui.findIdName.text()  
        self.myBirth=self.ui.findIdBirth.text()
        print(self.myName,self.myBirth)
        self.find(self.myName,self.myBirth)
        self.editClear()
        self.ui.stackedWidget.setCurrentWidget(self.ui.loginPage)