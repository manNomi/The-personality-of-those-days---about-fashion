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
        self.name="만욱"
        self.btnEvent()

    
    def btnEvent(self):
        self.ui.scheduleBtn.clicked.connect(lambda event:self.btnOOTD())
        self.ui.ootdBackBtn.clicked.connect(lambda event:self.backEvent())

    def btnOOTD(self):
        dialog=QtWidgets.QDialog()
        self.ui.dialogOOTDCheck(dialog)
        self.ui.dialogOOTDEditBtn.clicked.connect(lambda event:self.dialogOOTDEvent(dialog))
        dialog.show()
        
    def dialogOOTDEvent(self,dialog):
        input=self.ui.dialogOOTDEdit.text()
        data=self.db.readData("OOTD",["id","OOTD"],[self.name,input],self.db.cursor5)
        if len(data)!=0:
            dialogError=QtWidgets.QDialog()
            self.ui.dialogError(dialogError,"증복된 사진입니다")
        else:
            datas=[self.name,input]
            self.db.insertData("OOTD",self.db.rows5,datas,self.db.cursor5,self.db.connect5)
            dialog.close()

    def OOTDSet(self):
        pass



    def backEvent(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.PageMain)
        
        