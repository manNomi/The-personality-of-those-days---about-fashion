from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import threadChange

from PyQt5 import *
import vlc


class PageGuide:
    def __init__(self,ui,db):
        self.ui=ui
        self.db=db

        self.initBtn()
        self.guideSet()
    
    def guideSet(self):
        self.instance=vlc.Instance()
        self.playGuide = self.instance.media_player_new()
        self.playGuide.set_hwnd(int(self.ui.guidePlay.winId()))
        mf="guide/guideMovie.mp4"
        media = self.instance.media_new(mf)
        media.get_mrl()
        self.playGuide.set_media(media)

    
    def initBtn(self):
        for index in range(0,len(self.ui.guideBtns)):
            self.ui.guideBtns[index].clicked.connect(lambda event,value=index:self.moveEvent(value))
        self.ui.guideBackBtn.clicked.connect(lambda event:self.moveEvent(3))

    def moveEvent(self,type):
        if type==0:
            if self.playGuide.is_playing()==False:
                self.playGuide.play()
        elif type==1:
            self.playGuide.stop()
        elif type==2:
            self.playGuide.pause()
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.PageMain)
