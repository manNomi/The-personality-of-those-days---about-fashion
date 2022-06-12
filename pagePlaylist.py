import time
import vlc
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
import time
from PyQt5 import *
from PyQt5.QtWidgets import*
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from json import load
from itsdangerous import exc
import pafy
import urllib.request
from PyQt5.QtGui import *
import sys

class pagePlayList:

    def __init__(self,ui,db):
        self.musicIndex=0

        self.ui=ui
        self.db=db
        self.name='만욱'
        self.initBtnEvnet()
        self.playVideo=PlayVideo(self.ui)

    def initBtnEvnet(self):
        self.ui.playBackBtn.clicked.connect(lambda event : self.moveEvent())
        self.ui.insertVideoBtn.clicked.connect(lambda event : self.insertMusic())
        self.ui.playMusicBtns[0].clicked.connect(lambda event : self.videoPlay(self.musicIndex))

        for index in range(0,len(self.ui.playMusicBtns)):
            self.ui.playMusicBtns[index].clicked.connect(lambda event : self.playVideo.btnEvent(index))
        


    def moveEvent(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.PageMain)
    
    def insertMusic(self):
        dialog=QtWidgets.QDialog()
        self.ui.dialogPlayList(dialog)
        dialog.show()
        self.ui.dialogPlayListBtn.clicked.connect(lambda event:self.insertMusicCheck(dialog))

        dialog.exec()

    def insertMusicCheck(self,dialogPrev):
        dialogPrev.close()
        insertData=self.ui.dialogPlayListEdit.text()
        data=self.db.readData("playList",["id","url"],[self.name,insertData],self.db.cursor4)
        if len(data)!=0:
            dialog=QtWidgets.QDialog()
            self.ui.dialogError(dialog,"이미 존재하는 값입니다")
            dialog.exec()
        else:
            self.insertVideo()

    def insertVideo(self):
        playList=self.ui.dialogPlayListEdit.text()
        videoData=self.storeVideo(self.ui.dialogPlayListEdit.text())
        try:
            listData=[self.name,playList,videoData[0],videoData[1]]
            print(listData)
            self.presentList=playList
            self.db.insertData("playList",self.db.rows4,listData,self.db.cursor4,self.db.connect4)
        except:
            dialog=QtWidgets.QDialog()
            self.ui.dialogError(dialog,"잘못된 URL입니다")
            dialog.exec()

    def storeVideo(self,url):
        try:
            video = pafy.new(url)
            sec=int(video.duration[0])*36000+int(video.duration[1])*3600+int(video.duration[3])*600+int(video.duration[4])*60+int(video.duration[6])*10+int(video.duration[7])
            videoName=video.title
            print(videoName,sec)
            return videoName,sec
        except:
            pass

    def musicBtns(self,num):
        if num==0:
            # 재생
            pass
        elif num==1:
            # 정지
            pass
            
        elif num==2:
            # 일시정지
            pass
        elif num==3:
            #다음곡
            pass
    
    def videoPlay(self,num):
        self.playVideo.playEvent()
        listData=self.db.readData("playList",["id"],[self.name],self.db.cursor4)
        self.playVideo.setVideoPlay(listData,num)

class PlayVideo:
    def __init__(self,ui):
        self.ui=ui
        self.instance = vlc.Instance()
    
    def btnEvent(self,num):
        self.play.PlayPause(num)
        if num==0:
            pass
        elif num==1:
            self.ui.videoName.setText("")
        elif num==2:
            print("멈추기")
        else :
            pass

    def playEvent(self):
        try:
            self.play.playStop()
            self.ui.videoName.setText("")
            self.timer.timerSet()
        except:
            pass

    def setVolume(self, Volume):
        self.play.changeVolume(Volume)

    def setVideoPlay(self,listData,num):

        qpixmap=QPixmap()
        qpixmap.load("")
        self.ui.playListPic.setPixmap(qpixmap)
        self.ui.playListPic.setStyleSheet("background-color:#00ffffff")
        
        self.ui.videoName.setText(listData[num][3])
        
        url=listData[num][2]
        
        self.play=Play(self.ui.videoPlay,url)

import threading
class Play(threading.Thread):
    def __init__(self,ui_video,url):
        threading.Thread.__init__(self)
        self.url=url
        self.ui=ui_video
        self.run()

        
    def changeVolume(self, Volume):
        self.playVideo.audio_set_volume(100-Volume)

    def run(self):
        # for index in range(0,2):
        try:
            video=pafy.new(self.url)
        except:pass

        best = video.getbest()
        playurl = best.url
        Instance = vlc.Instance()

        self.video = Instance.media_player_new()

        Media = Instance.media_new(playurl)

        Media.get_mrl()

        self.video.set_media(Media)

        self.video.set_hwnd(int(self.ui.winId())) 

        self.video.play()


        
    def playStop(self):
        self.video.stop()
        
    def PlayPause(self,num):
        if num==0:
            if self.video.is_playing()==False:
                self.video.play()
                print("재생")

        elif num==1:
            self.video.stop()
            print("멈춤")
        elif num==2:
            if self.video.is_playing():
                self.video.pause()
                print("일시정지")

        else:
            pass
