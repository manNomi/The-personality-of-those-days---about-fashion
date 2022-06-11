import time
import vlc
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
import time

class pagePlayList:

    def __init__(self,ui,db):
        self.ui=ui
        self.db=db
        self.name='만욱'
        self.initBtnEvnet()
        self.playVideo=PlayVideo(self.ui)

    def initBtnEvnet(self):
        self.ui.playBackBtn.clicked.connect(lambda event : self.moveEvent(1))
        self.ui.insertVideoBtn.clicked.connect(lambda event : self.insertMusic())
        for index in range(0,len(self.ui.playMusicBtns)):
            self.ui.playMusicBtns[index].clicked.connect(lambda event : self.playVideo.videoPlay(index))


    def moveEvent(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageMain)
    
    def insertMusic(self):
        dialog=QtWidgets.QDialog()
        self.ui.dialogPlayList(dialog)
        dialog.show()
        self.ui.dialogPlayListBtn.clicked.connect(lambda event:self.insertMusicCheck())

    def insertMusicCheck(self):
        insertData=self.ui.dialogPlayListEdit.text()
        data=self.db.readData("playList",["id","playList"],[self.name,insertData],self.db.cursor4)
        if len(data)!=0:
            dialog=QtWidgets.QDialog()
            self.ui.dialogError(dialog,"이미 존재하는 값입니다")
            dialog.show()
        else:
            datas=[self.name,insertData]
            self.db.insertData("playList",self.db.rows4,datas,self.db.cursor4,self.db.connect4)
            dialog.close()
            


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
        self.play.playEvent()
        listData=self.db.readData("playVideo",["id","playList"],[self.name,self.playList],self.db.cursor4)
        print("listData="+str(listData))
        self.play.setVideoPlay(listData,num)
        


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
