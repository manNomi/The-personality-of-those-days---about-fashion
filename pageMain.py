import mainUi
import pageCloset
import pageOOTD
import pagePlaylist
import pageGuide
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import db

class MainPage:

    def __init__(self,ui,db):
        self.db=db
        self.ui=ui

        self.closet=pageCloset.PageCloset(self.ui,self.db)
        self.ootd=pageOOTD.PageOOTD(self.ui,self.db)

        self.playList=pagePlaylist.pagePlayList(self.ui,self.db)
        
        self.pageGuide=pageGuide.PageGuide(self.ui,self.db)
        
        closetGif = QMovie("image/pageMainImage.gif", QByteArray())
        closetGif.setCacheMode(QMovie.CacheAll)
        closetGif.setScaledSize(QSize(330,335))
        self.ui.mainPic.setMovie(closetGif)

        closetGif.start()

        self.ui.stackedWidget.setCurrentWidget(self.ui.PageMain)
        self.ui.MainWindow.show()
        self.btnEvent()
        self.name=""


    def rename(self,id):
        self.name=id


    def btnEvent(self):
        for index in range(0,len(self.ui.mainBtns)):
            self.ui.mainBtns[index].clicked.connect(lambda event,value=index : self.moveEvent(value))

        self.ui.mainBackBtn.clicked.connect(lambda event,value=index : self.moveEvent(4))

        self.ui.scheduleBackBtn.clicked.connect(lambda event,value=index : self.moveEvent(6))

    def moveEvent(self,index):
        if index==0:
            self.ui.stackedWidget.setCurrentWidget(self.ui.PageCloset)
            self.closet.thread_pic(True)
            self.closet.getName(self.name)

        elif index==1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.PageOOTD)
            self.ootd.getName(self.name)
        elif index==2:
            self.ui.stackedWidget.setCurrentWidget(self.ui.PageSchedule)
        elif index==3:
            self.ui.stackedWidget.setCurrentWidget(self.ui.PageplayList)
            self.playList.getName(self.name)
        elif index==4:
            self.ui.stackedWidget.setCurrentWidget(self.ui.PageGuide)
        elif index==5:
            # self.ui.stackedWidget.setCurrentWidget(self.ui.PageLogin)   - pageLogin 
            pass
        elif index==6:
            self.ui.stackedWidget.setCurrentWidget(self.ui.PageMain)
            

if __name__=="__main__":
    main=MainPage()