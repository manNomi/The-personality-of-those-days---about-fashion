import mainUi
import pageCloset
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import db

class MainPage:

    def __init__(self):
        self.db=db.Database()



        app = QtWidgets.QApplication(sys.argv)
        self.ui=mainUi.Ui()
        self.closet=pageCloset.PageCloset(self.ui,self.db)

        closetGif = QMovie("image/pageMainImage.gif", QByteArray())
        closetGif.setCacheMode(QMovie.CacheAll)
        closetGif.setScaledSize(QSize(330,335))
        self.ui.mainPic.setMovie(closetGif)

        closetGif.start()


        self.ui.stackedWidget.setCurrentWidget(self.ui.PageMain)
        self.ui.MainWindow.show()


        self.btnEvent()


        sys.exit(app.exec_())




    
    def btnEvent(self):
        for index in range(0,len(self.ui.mainBtns)):
            self.ui.mainBtns[index].clicked.connect(lambda event,value=index : self.moveEvent(value))

        self.ui.mainBackBtn.clicked.connect(lambda event,value=index : self.moveEvent(4))
        

    def moveEvent(self,index):
        if index==0:
            self.ui.stackedWidget.setCurrentWidget(self.ui.PageCloset)
        elif index==1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.PageOOTD)
        elif index==2:
            self.ui.stackedWidget.setCurrentWidget(self.ui.PagePlayList)
        elif index==3:
            self.ui.stackedWidget.setCurrentWidget(self.ui.PageGuide)
        elif index==3:
            # self.ui.stackedWidget.setCurrentWidget(self.ui.PageLogin)   - pageLogin 
            pass
        
            




if __name__=="__main__":
    main=MainPage()
    
    