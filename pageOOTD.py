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
        self.name=""
        self.btnEvent()
        self.setDefaultOOTD()
        
        
    def setDefaultOOTD(self):
        self.OOTDSet("Spring")
        self.OOTDSet("Summer")
        self.OOTDSet("Autum")
        self.OOTDSet("Winter")

        


    

    def getName(self,name):
        self.name=name
        self.setDefaultOOTD()
        self.setPicuter()

    def setPicuter(self):
        dataSpring=self.db.readData("OOTD",["id","season"],[self.name,'Spring'],self.db.cursor5)
        dataAutum=self.db.readData("OOTD",["id","season"],[self.name,'Autum'],self.db.cursor5)
        dataWinter=self.db.readData("OOTD",["id","season"],[self.name,'Winter'],self.db.cursor5)
        dataSummer=self.db.readData("OOTD",["id","season"],[self.name,'Summer'],self.db.cursor5)

        for index in range(0,len(dataSpring)):
            qPixmapSpring = QPixmap()
            imageSpring="spring/"+str(dataSpring[index][3])+".png"
            print(imageSpring)
            qPixmapSpring.load(imageSpring)
            qPixmapSpring=qPixmapSpring.scaled(250, 300)
            self.ui.springImageBtn[index].setPixmap(qPixmapSpring)
        for index in range(0,len(dataAutum)):
            qPixmapAutum = QPixmap()
            imageAutum="fall/"+str(dataAutum[index][3])+".png"
            print(imageAutum)
            qPixmapAutum.load(imageAutum)
            qPixmapAutum=qPixmapAutum.scaled(250, 300)
            self.ui.AutumnImageBtn[index].setPixmap(qPixmapAutum)
        for index in range(0,len(dataWinter)):
            qPixmapWinter = QPixmap()
            imageWinter="winter/"+str(dataWinter[index][3])+".png"
            print(imageWinter)
            qPixmapWinter.load(imageWinter)
            qPixmapWinter=qPixmapWinter.scaled(250, 300)
            self.ui.WinterImageBtn[index].setPixmap(qPixmapWinter)

        for index in range(0,len(dataSummer)):
            qPixmapSummer = QPixmap()
            imageSummer="summer/"+str(dataSummer[index][3])+".png"
            print(imageSummer)
            qPixmapSummer.load(imageSummer)
            qPixmapSummer=qPixmapSummer.scaled(250, 300)
            self.ui.SummerImageBtn[index].setPixmap(qPixmapSummer)



    def btnEvent(self):
        self.ui.scheduleBtn.clicked.connect(lambda event:self.btnOOTD())
        self.ui.OOTDBackBtn.clicked.connect(lambda event:self.backEvent())

    def btnOOTD(self):
        dialog=QtWidgets.QDialog()
        self.ui.dialogOOTDCheck(dialog)
        self.ui.dialogOOTDEditBtn.clicked.connect(lambda event:self.dialogOOTDEvent(dialog))
        dialog.show()

        


    def dialogOOTDEvent(self,dialog):
        input=self.ui.dialogOOTDEdit.text()
        
        springBtn=self.ui.springBtn.isChecked()
        summerBtn=self.ui.summerBtn.isChecked()
        autumBtn=self.ui.autumBtn.isChecked()
        winterBtn=self.ui.winterBtn.isChecked()



        btns=[springBtn,summerBtn,autumBtn,winterBtn]
        btn=[]
        for index in range(0,4):
            if btns[index]==True:
                btn.append(index)

        if len(btn)!=1:
            dialogError=QtWidgets.QDialog()
            self.ui.dialogError(dialogError,"체크박스를 확인하세요")
            dialogError.show()
            dialogError.exec()

        else:
            season='none'
        
            if btn[0]==0:
                season="Spring"
            elif btn[0]==1:
                season="Summer"
            elif btn[0]==2:
                season="Autum"
            elif btn[0]==3:
                season="Winter"
                
            data=self.db.readData("OOTD",["id","season","OOTD"],[self.name,season,input],self.db.cursor5)

            if len(data)!=0:
                dialogError=QtWidgets.QDialog()
                self.ui.dialogError(dialogError,"증복된 사진입니다")
                dialogError.show()
                dialogError.exec()
            else:
                datas=[self.name,season,input]
                self.db.insertData("OOTD",self.db.rows5,datas,self.db.cursor5,self.db.connect5)
                dialog.close()
                self.OOTDSet(season)
                self.setPicuter()


    def OOTDSet(self,season):
        data=self.db.readData("OOTD",["id","season"],[self.name,season],self.db.cursor5)
        self.ui.OOTDset(data,season)




    def backEvent(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.PageMain)

        
        
        