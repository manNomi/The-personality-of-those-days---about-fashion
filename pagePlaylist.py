import time
import vlc
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
import time

class pagePlayList:

    def __init__(self,ui,db):
        self.ui=ui
        self.db=db
        self.initBtnEvnet()

    def initBtnEvnet(self):
        self.ui.playBackBtn.clicked.connect(lambda event : self.moveEvent(1))
        self.ui.insertVideoBtn.clicked.connect(lambda event : self.moveEvent())

    def moveEvent(self,changeNum):
        if changeNum==1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.pageMain)
    
    def insertMusic(self):
        dialog=QtWidgets.QDialog()
        self.ui.dialogPlayList(dialog)
        dialog.show()
        self.ui.dialogPlayListBtn.clicked.connect(lambda event:self.insertMusicCheck())

    def insertMusicCheck(self):
        pass
        
        


class PlayVideo:
    def __init__(self,ui):
        self.ui=ui
        self.instance = vlc.Instance()
    
    def btnEvent(self,num):
        self.play.PlayPause(num)
        if num==0:
            self.timer.timeRestart()
        elif num==1:
            self.ui.videoName.setText("")
            self.timer.timerSet()
        else :
            self.timer.timerStop()

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
        try:
            self.sec=listData[num][4]
            self.mp = self.instance.media_player_new()
            self.mp.set_hwnd(int(self.ui.videoPlay.winId()))
            print(self.ui.videoPlay.winId())
            mf="videos/"+str(listData[num][3])+".mp4"
            self.ui.videoName.setText(str(listData[num][3]))
            media = self.instance.media_new(mf)
            media.get_mrl()
            self.mp.set_media(media)
            self.play=Play(self.mp)
            self.play.start()
            
            self.progressbarSet(listData[num][4])
        except:
            self.ui.videoName.setText("LOADING....")


class Play(QThread):
    playvideo = pyqtSignal(int)  

    def __init__(self,play):
        super().__init__()
        self.playVideo=play
        self.timer=0
        
    def changeVolume(self, Volume):
        self.playVideo.audio_set_volume(100-Volume)

    def run(self):
        print("시작")
        self.playVideo.play()
        
    def playStop(self):
        self.playVideo.stop()
        
    def PlayPause(self,num):
        if num==0:
            if self.playVideo.is_playing()==False:
                self.playVideo.play()
        elif num==1:
            self.playVideo.stop()
        else:
            if self.playVideo.is_playing():
                self.playVideo.pause()
