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
        self.name="만욱"
        self.btnEvent()
        self.closetSetting()
        self.closetBtnEvent()
    


    def closetSetting(self):
        
        dataTop=self.db.readData("top",["id"],[self.name],self.db.cursor2)
        dataBot=self.db.readData("bot",["id"],[self.name],self.db.cursor3)

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

            dialog=QtWidgets.QDialog()
            self.ui.dialogCloset(dialog)
            dialog.show()
            dialog.exec()
        
        elif value==3:
            # 삭제
            self.deleteThing()
            

        elif value==4:
            # 이동
            self.ui.stackedWidget.setCurrentWidget(self.ui.PageMain)

            
    def chooseEvent(self):
        dialog=QtWidgets.QDialog()
        self.ui.dialogClosetCheck(dialog,"상의")
        dialog.show()


    def closetBtnEvent(self):
        for index in range(0,len(self.ui.closetImageBtn)):
            self.ui.closetImageBtn[index].clicked.connect(lambda event , value=index : self.closetDialog(1,value))
        for index in range(0,len(self.ui.closetImageBtnBot)):     
            self.ui.closetImageBtnBot[index].clicked.connect(lambda event , value=index : self.closetDialog(2,value))

    def closetDialog(self,type,value):
            if type==1:
                dataTop=self.db.readData("top",["id"],[self.name],self.db.cursor3)
                imageNum=dataTop[value]
                image="closet_top/"+str(imageNum[2])+".png"
                self.ui.closetDialogSet(1,image)
            else:
                dataBot=self.db.readData("bot",["id"],[self.name],self.db.cursor3)
                imageNum=dataBot[value]
                image="closet_bot/"+str(imageNum[2])+".png"
                self.ui.closetDialogSet(2,image)
                




    
    def insertTop(self):
        dialog=QtWidgets.QDialog()
        self.ui.dialogClosetCheck(dialog,"상의")
        dialog.show()
        print(self.ui.dialogClosetText)
        self.ui.dialogClosetBtn.clicked.connect(lambda event : self.checkTop(dialog))
        dialog.exec()
    
    def checkTop(self,dialog):
        top=self.ui.dialogClosetText.text()
        data=self.db.readData("top",["id","top"],[self.name,top],self.db.cursor2)

        if len(data)!=0:
            dialogError=QtWidgets.QDialog()
            self.ui.dialogError(dialogError,"증복된 입력입니다")
            dialogError.exec()
        else:
            datas=[self.name,top]
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
        data=self.db.readData("bot",["id","bot"],[self.name,bot],self.db.cursor3)
        if len(data)!=0:
            dialogError=QtWidgets.QDialog()
            self.ui.dialogError(dialogError,"증복된 입력입니다")
            dialogError.exec()
        else:
            datas=[self.name,bot]
            self.db.insertData("bot",self.db.rows3,datas,self.db.cursor3,self.db.connect3)
            dialog.close()
        self.closetSetting()
        dialog.close()

    def deleteThing(self):
        dialog=QtWidgets.QDialog()
        self.ui.dialogClosetDelete(dialog)
        dialog.show()
        self.ui.dialogClosetDeleteBtn.clicked.connect(lambda event : self.deleteCloset(dialog))

    def deleteCloset(self,dialog):
        
        top=self.ui.checkBoxTop.isChecked()
        bot=self.ui.checkBoxBot.isChecked()
        if top==True and bot==True:
            dialogError=QtWidgets.QDialog()
            self.ui.dialogError(dialogError,"상의와 하의중 \n하나만 눌러주세요")
            dialogError.exec()

        elif top==False and bot==False:
            dialogError=QtWidgets.QDialog()
            self.ui.dialogError(dialogError,"상의와 하의중 \n하나를 눌러주세요")
            dialogError.exec()
        
        else:
            if top==True:
                topCloth=self.ui.dialogClosetText.text()
                data=self.db.readData("top",["id","top"],[self.name,topCloth],self.db.cursor2)
                if len(data)!=0:
                    deleteData=["sequance",data[0][0]]
                    self.db.deleteData("top",deleteData,self.db.cursor2,self.db.connect2)
                    dialog.close()
                    self.closetSetting()

                else:
                    dialogError=QtWidgets.QDialog()
                    self.ui.dialogError(dialogError,"존재하지 않는 옷입니다")
                    dialogError.exec()
            
            else:
                botCloth=self.ui.dialogClosetText.text()
                data=self.db.readData("bot",["id","bot"],[self.name,botCloth],self.db.cursor3)
                if len(data)!=0:
                    deleteData=["sequance",data[0][0]]
                    self.db.deleteData("bot",deleteData,self.db.cursor3,self.db.connect3)
                    dialog.close()
                    self.closetSetting()

                else:
                    dialogError=QtWidgets.QDialog()
                    self.ui.dialogError(dialogError,"존재하지 않는 옷입니다")
                    dialogError.exec()
                    
                
