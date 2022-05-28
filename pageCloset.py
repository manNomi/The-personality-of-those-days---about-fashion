import mainUi
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class PageCloset:
    def __init__(self,ui,db):
        self.ui=ui
        self.db=db
        self.btnEvent()
        self.closetSetting()


    def closetSetting(self):
        id="만욱"
        dataTop=self.db.readData("top",["id"],[id],self.db.cursor2)
        dataBot=self.db.readData("bot",["id"],[id],self.db.cursor3)

        self.ui.setCloset(1,dataTop)
        self.ui.setCloset(2,dataBot)
        

    def btnEvent(self):
        for index in range(0,len(self.ui.closetBtns)):
            self.ui.closetBtns[index].clicked.connect(lambda event,value=index:self.eventFlow(value))
        self.ui.closetBackBtn.clicked.connect(lambda event,value=index:self.eventFlow(4))


    def eventFlow(self,value):
        if value==0:
            # 상의추가
            self.insertTop()

        elif value==1:
            #하의추가
            self.insertBot()

        elif value==2:
            #선택
            pass
            

        elif value==3:
            # 삭제
            pass
            

        elif value==4:
            # 이동
            self.ui.stackedWidget.setCurrentWidget(self.ui.PageMain)

            

    
    def insertTop(self):
        dialog=QtWidgets.QDialog()
        self.ui.dialogClosetCheck(dialog,"상의")
        dialog.show()
        print(self.ui.dialogClosetText)
        self.ui.dialogClosetBtn.clicked.connect(lambda event : self.checkTop(dialog))
        dialog.exec()
    
    def checkTop(self,dialog):
        top=self.ui.dialogClosetText.text()
        id="만욱"
        data=self.db.readData("top",["id","top"],[id,top],self.db.cursor2)

        if len(data)!=0:
            dialogError=QtWidgets.QDialog()
            self.ui.dialogError(dialogError,"증복된 입력입니다")
            dialogError.exec()
        else:
            datas=[id,top]
            self.db.insertData("top",self.db.rows2,datas,self.db.cursor2,self.db.connect2)
            dialog.close()
        self.closetSetting()
        dialog.close()


    def insertBot(self):
        dialog=QtWidgets.QDialog()
        self.ui.dialogClosetCheck(dialog,"하의")
        dialog.show()
        print(self.ui.dialogClosetText)
        self.ui.dialogClosetBtn.clicked.connect(lambda event : self.checkBot(dialog))
        dialog.exec()
    
    def checkBot(self,dialog):
        bot=self.ui.dialogClosetText.text()
        id="만욱"
        data=self.db.readData("bot",["id","bot"],[id,bot],self.db.cursor3)
        if len(data)!=0:
            dialogError=QtWidgets.QDialog()
            self.ui.dialogError(dialogError,"증복된 입력입니다")
            dialogError.exec()
        else:
            datas=[id,bot]
            self.db.insertData("bot",self.db.rows3,datas,self.db.cursor3,self.db.connect3)
            dialog.close()
        self.closetSetting()
        dialog.close()