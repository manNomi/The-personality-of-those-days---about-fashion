from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui():
    
    def __init__(self):
        self.MainWindow=QtWidgets.QMainWindow()
        self.MainWindow.setGeometry(800,60,800,950)
        self.MainWindow.setMinimumSize(800,950)
        self.MainWindow.setMaximumSize(800,950)
        self.MainWindow.setStyleSheet("background-color : white;")
        

        self.centralwidget = QtWidgets.QWidget(self.MainWindow)

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(0,0,857,1176)

        self.stackedWidget.setObjectName("stackedWidget")
#########################################################################################
#font 

# color 

#color - #A0B4E6 연파
# #808080 회색
    
        font = QtGui.QFont()
        font.setFamily('함초롬돋움')
        font.setPointSize(16)
        font.setWeight(75)
#########################################################################################

        #PageMain
        self.PageMain=QtWidgets.QWidget()
        self.PageMain.setObjectName("PageMain")

        mainBorder=QtWidgets.QLabel(self.PageMain)
        mainBorder.setGeometry(20,10,771,933)
        mainBorder.setStyleSheet("background-color: white ;border-style: solid;border-color: #A0B4E6; border-width: 10px")

        self.mainPic=QtWidgets.QLabel(self.PageMain)
        self.mainPic.setGeometry(230,40,330,335)
        self.mainPic.setStyleSheet("background-color:white")
        
        
        mainBtnXY=[[310,530,170,50],[310,590,170,50],[310,650,170,50],[310,710,170,50],[310,770,170,50]]
        mainBtnText=['나만의 closet','OOTD 기록','일정등록','playlist','가이드 영상']
        self.mainBtns=[]
        for index in range(0,5):
            mainBtn=QtWidgets.QToolButton(self.PageMain)
            mainBtn.setGeometry(mainBtnXY[index][0],mainBtnXY[index][1],mainBtnXY[index][2],mainBtnXY[index][3])
            mainBtn.setStyleSheet("background-color:white;border-style: solid;border-color: #A0B4E6;border-width: 3px;color:#3057B9;border-radius: 10px")
            mainBtn.setText(mainBtnText[index])
            mainBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            font.setPointSize(10)
            mainBtn.setFont(font)

            self.mainBtns.append(mainBtn)

        self.mainBackBtn=QtWidgets.QPushButton(self.PageMain)
        self.mainBackBtn.setGeometry(40,40,40,40)
        self.mainBackBtn.setIcon(QtGui.QIcon("image/back.png"))
        self.mainBackBtn.setIconSize(QtCore.QSize(40,40))
        self.mainBackBtn.setStyleSheet("border-style: solid; border-color : white; border-width: 0px;color:white;")
        self.mainBackBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        

        self.stackedWidget.addWidget(self.PageMain)


            

#########################################################################################
#pageCloset
        self.PageCloset=QtWidgets.QWidget()
        self.PageCloset.setObjectName("PageCloset")

        closetBorder=QtWidgets.QLabel(self.PageCloset)
        closetBorder.setGeometry(20,10,771,933)
        closetBorder.setStyleSheet("background-color: white ;border-style: solid;border-color: #A0B4E6; border-width: 10px")

        closetPic=QtWidgets.QLabel(self.PageCloset)
        closetPic.setGeometry(51,22,82,235)
        closetPic.setStyleSheet("background-color:white")
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load("image/closetLeft.PNG")
        self.qPixmapVar=self.qPixmapVar.scaled(82,235)
        closetPic.setPixmap(self.qPixmapVar)

        closetPic2=QtWidgets.QLabel(self.PageCloset)
        closetPic2.setGeometry(657,22,97,235)
        closetPic2.setStyleSheet("background-color:white")
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load("image/closetRight.PNG")
        self.qPixmapVar=self.qPixmapVar.scaled(97,235)
        closetPic2.setPixmap(self.qPixmapVar)
            


        self.closetAd=QtWidgets.QLabel(self.PageCloset)
        self.closetAd.setGeometry(165,161,462,117)
        self.closetAd.setStyleSheet("background-color:black")

        font = QtGui.QFont()
        font.setFamily('함초롬돋움')
        font.setPointSize(16)
        font.setWeight(75)

        closetPicXY=[[190,30,170,50],[420,30,170,50],[190,100,170,50],[420,100,170,50]]
        closetBtnText=['상의 추가','하의 추가','선택','삭제']
        self.closetBtns=[]
        for index in range(0,4):
            closetBtn=QtWidgets.QToolButton(self.PageCloset)
            closetBtn.setGeometry(closetPicXY[index][0],closetPicXY[index][1],closetPicXY[index][2],closetPicXY[index][3])
            closetBtn.setText(closetBtnText[index])
            closetBtn.setStyleSheet("background-color:white;border-style: solid;border-color: #A0B4E6;border-width: 3px;color:#3057B9;border-radius: 10px")
            closetBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            closetBtn.setFont(font)

            self.closetBtns.append(closetBtn)

        self.chooseCloset = QtWidgets.QTabWidget(self.PageCloset)
        self.chooseCloset.setGeometry(40,279, 714, 625)
        font = QtGui.QFont()
        font.setFamily('함초롬돋움')
        font.setPointSize(16)
        font.setWeight(75)

        self.chooseCloset.setFont(font)
        self.chooseCloset.setObjectName("chooseCloset")

        self.chooseTop = QtWidgets.QWidget()
        self.chooseTop.setObjectName("chooseTop")
        
        self.chooseBottom = QtWidgets.QWidget()
        self.chooseBottom.setObjectName("chooseBottom")

        self.chooseCloset.addTab(self.chooseTop, "")
        self.chooseCloset.addTab(self.chooseBottom, "")


        self.chooseCloset.setTabText(self.chooseCloset.indexOf(self.chooseBottom),"하의")
        self.chooseCloset.setTabText(self.chooseCloset.indexOf(self.chooseTop),"상의")

        
        self.chooseCloset.setStyleSheet("QTabWidget::pane{border-style: solid; border-width: 3px;border-color:#808080}\nQTabBar::tab{ border-style: solid; border-width: 3px;border-color:#808080;color:#808080}")

        self.scrollTop = QtWidgets.QScrollArea(self.chooseTop)
        self.scrollTop.setGeometry(10,10,694,577)
        self.scrollTop.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollTop.setWidgetResizable(True)
        self.scrollTop.setObjectName("scrollTop")

        self.scrollTopCont = QtWidgets.QWidget()
        self.scrollTopCont.setGeometry(0, 0, 107, 87)
        self.scrollTopCont.setObjectName("scrollTopCont")

        self.groupBoxTop = QtWidgets.QGroupBox(self.scrollTopCont)
        self.groupBoxTop.setGeometry(0, 10, 103, 59)
        self.groupBoxTop.setObjectName("groupBoxTop")

        self.horizontal_Top = QtWidgets.QWidget(self.groupBoxTop)
        self.horizontal_Top.setGeometry(20, 20, 560,500)
        self.horizontal_Top.setObjectName("horizontal_Top")

        self.verticalLayout = QtWidgets.QFormLayout(self.horizontal_Top)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setSpacing(50)
        self.verticalLayout.setVerticalSpacing(100)

        self.groupBoxTop.setLayout(self.verticalLayout)
        self.scrollTop.setWidget(self.groupBoxTop)

        self.scrollBottom = QtWidgets.QScrollArea(self.chooseBottom)
        self.scrollBottom.setGeometry(10,10,694,577)
        self.scrollBottom.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollBottom.setWidgetResizable(True)
        self.scrollBottom.setObjectName("scrollBottom")

        self.scrollBottomWidgetContents = QtWidgets.QWidget()
        self.scrollBottomWidgetContents.setGeometry(0, 0, 107, 87)
        self.scrollBottomWidgetContents.setObjectName("scrollBottomWidgetContents")

        self.groupBoxBot = QtWidgets.QGroupBox(self.scrollBottomWidgetContents)
        self.groupBoxBot.setGeometry(0, 10, 103, 59)
        self.groupBoxBot.setObjectName("groupBoxBot")

        self.horizontal_Bot = QtWidgets.QWidget(self.groupBoxBot)
        self.horizontal_Bot.setGeometry(20, 20, 560,500)
        self.horizontal_Bot.setObjectName("horizontal_Bot")

        self.verticalLayoutBot = QtWidgets.QFormLayout(self.horizontal_Bot)
        self.verticalLayoutBot.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutBot.setObjectName("verticalLayoutBot")
        self.verticalLayoutBot.setSpacing(50)
        self.verticalLayoutBot.setVerticalSpacing(100)

        self.groupBoxBot.setLayout(self.verticalLayoutBot)
        self.scrollBottom.setWidget(self.groupBoxBot)

        self.closetBackBtn=QtWidgets.QPushButton(self.PageCloset)
        self.closetBackBtn.setGeometry(40,40,40,40)
        self.closetBackBtn.setIcon(QtGui.QIcon("image/back.png"))
        self.closetBackBtn.setIconSize(QtCore.QSize(40,40))
        self.closetBackBtn.setStyleSheet(" border-style: solid; border-color : white; border-width: 0px;color:white;")
        self.closetBackBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


        
        self.stackedWidget.addWidget(self.PageCloset)


##############################################################################################

        self.PageSchedule=QtWidgets.QWidget()
        self.PageSchedule.setObjectName("PageSchedule")

        scheduleBorder=QtWidgets.QLabel(self.PageSchedule)
        scheduleBorder.setGeometry(20,10,771,933)
        scheduleBorder.setStyleSheet("background-color: white ;border-style: solid;border-color: #A0B4E6; border-width: 10px")

        schedulePic=QtWidgets.QLabel(self.PageSchedule)
        schedulePic.setGeometry(308,22,182,235)
        schedulePic.setStyleSheet("background-color:black")
        
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load("image/calander.png")
        self.qPixmapVar=self.qPixmapVar.scaled(182,235)
        schedulePic.setPixmap(self.qPixmapVar)

        self.scheduleBtn=QtWidgets.QToolButton(self.PageSchedule)
        self.scheduleBtn.setGeometry(285,284,228,36)
        self.scheduleBtn.setStyleSheet("border-style: solid ; border-radius: 10px; border-color:#A0B4E6; border-width:3px; color: #3057B9;background-color: white")
        self.scheduleBtn.setFont(font)
        self.scheduleBtn.setText("확인")
        self.scheduleBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        QtCore.QMetaObject.connectSlotsByName(self.PageSchedule)


        self.calander = QtWidgets.QCalendarWidget(self.PageSchedule)
        self.calander.setGeometry(68, 367, 657, 514)
        self.calander.setStyleSheet("background-color :white;color :#808080;border-style:solid;border-color:#A0B4E6")
        self.calander.setSelectedDate(QtCore.QDate(2022, 5, 1))
        self.calander.setGridVisible(True)
        self.calander.setObjectName("calander")
        font.setPointSize(8)
        self.calander.setFont(font)
        self.stackedWidget.addWidget(self.PageSchedule)

        self.scheduleBackBtn=QtWidgets.QPushButton(self.PageSchedule)
        self.scheduleBackBtn.setGeometry(40,40,40,40)
        self.scheduleBackBtn.setIcon(QtGui.QIcon("image/back.png"))
        self.scheduleBackBtn.setIconSize(QtCore.QSize(40,40))
        self.scheduleBackBtn.setStyleSheet(" border-style: solid; border-color : white; border-width: 0px;color:white;")
        self.scheduleBackBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))



##########################################################################################
        self.PageScheduleCheck=QtWidgets.QWidget()
        self.PageScheduleCheck.setObjectName("PageScheduleCheck")

        scheduleBorder=QtWidgets.QLabel(self.PageScheduleCheck)
        scheduleBorder.setGeometry(20,10,771,933)
        scheduleBorder.setStyleSheet("background-color: white ;border-style: solid;border-color: #A0B4E6; border-width: 10px")

        schedulePic=QtWidgets.QLabel(self.PageScheduleCheck)
        schedulePic.setGeometry(320,45,182,235)
        schedulePic.setStyleSheet("background-color:black")
        
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load("image/calander.png")
        self.qPixmapVar=self.qPixmapVar.scaled(182,235)
        schedulePic.setPixmap(self.qPixmapVar)

        self.scheduleCheckBtn=QtWidgets.QToolButton(self.PageScheduleCheck)
        self.scheduleCheckBtn.setGeometry(142,845,228,36)
        self.scheduleCheckBtn.setStyleSheet("border-style: solid ; border-radius: 10px; border-color:#A0B4E6; border-width:3px; color: #3057B9;background-color: white")
        font.setPointSize(16)
        self.scheduleCheckBtn.setFont(font)
        self.scheduleCheckBtn.setText("일정추가")
        self.scheduleCheckBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        QtCore.QMetaObject.connectSlotsByName(self.PageScheduleCheck)

        self.scheduleCheckBtn=QtWidgets.QToolButton(self.PageScheduleCheck)
        self.scheduleCheckBtn.setGeometry(428,845,228,36)
        self.scheduleCheckBtn.setStyleSheet("border-style: solid ; border-radius: 10px; border-color:#A0B4E6; border-width:3px; color: #3057B9;background-color: white")
        self.scheduleCheckBtn.setFont(font)
        self.scheduleCheckBtn.setText("일정삭제")
        self.scheduleCheckBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        QtCore.QMetaObject.connectSlotsByName(self.PageScheduleCheck)

        scrollArea = QtWidgets.QScrollArea(self.PageScheduleCheck)
        scrollArea.setGeometry(57,272,685,551)
        scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        scrollArea.setWidgetResizable(True)
        scrollArea.setObjectName("scrollArea3")
        scrollArea.setStyleSheet("color:#3057B9;border-style: solid ; border-radius: 3px; border-color:#A0B4E6; border-width:3px;")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(0, 0, 188, 119)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setGeometry(0, 10, 181, 81)
        self.groupBox.setObjectName("groupBox")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(20, 20, 980,680)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QFormLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setSpacing(50)
        self.verticalLayout.setVerticalSpacing(100)

        self.scheduleCheckBackBtn=QtWidgets.QPushButton(self.PageScheduleCheck)
        self.scheduleCheckBackBtn.setGeometry(40,40,40,40)
        self.scheduleCheckBackBtn.setIcon(QtGui.QIcon("image/back.png"))
        self.scheduleCheckBackBtn.setIconSize(QtCore.QSize(40,40))
        self.scheduleCheckBackBtn.setStyleSheet(" border-style: solid; border-color : white; border-width: 0px;color:white;")
        self.scheduleCheckBackBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


        self.groupBox.setLayout(self.verticalLayout)
        scrollArea.setWidget(self.groupBox)

        self.stackedWidget.addWidget(self.PageScheduleCheck)
##########################################################################################
        self.PageOOTD=QtWidgets.QWidget()
        self.PageOOTD.setObjectName("PageOOTD")

        scheduleBorder=QtWidgets.QLabel(self.PageOOTD)
        scheduleBorder.setGeometry(20,10,771,933)
        scheduleBorder.setStyleSheet("background-color: white ;border-style: solid;border-color: #A0B4E6; border-width: 10px")

        OOTDPic=QtWidgets.QLabel(self.PageOOTD)
        OOTDPic.setGeometry(270,30,137,235)
        OOTDPic.setStyleSheet("background-color:white")

        OOTDPic2=QtWidgets.QLabel(self.PageOOTD)
        OOTDPic2.setGeometry(95,30,137,200)
        OOTDPic2.setStyleSheet("background-color:white")


        qPixmapVar = QPixmap()
        qPixmapVar.load("image/OOTDrigth.png")
        OOTDPic.setPixmap(qPixmapVar)
        
        qPixmapVar = QPixmap()
        qPixmapVar.load("image/OOTDleft.png")
        OOTDPic2.setPixmap(qPixmapVar)


        self.scheduleBtn=QtWidgets.QToolButton(self.PageOOTD)
        self.scheduleBtn.setGeometry(457,147,228,36)
        self.scheduleBtn.setStyleSheet("border-style: solid ; border-radius: 10px; border-color:#A0B4E6; border-width:3px; color: #3057B9;background-color: white")
        self.scheduleBtn.setFont(font)
        self.scheduleBtn.setText("OOTD 추가")
        self.scheduleBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        QtCore.QMetaObject.connectSlotsByName(self.PageOOTD)

        
        self.chooseOOTD = QtWidgets.QTabWidget(self.PageOOTD)
        self.chooseOOTD.setGeometry(40,279, 714, 625)
        font = QtGui.QFont()
        font.setFamily('함초롬돋움')
        font.setPointSize(16)
        font.setWeight(75)

        self.chooseOOTD.setFont(font)
        self.chooseOOTD.setObjectName("chooseOOTD")

        self.spring = QtWidgets.QWidget()
        self.spring.setObjectName("spring")

        self.summer = QtWidgets.QWidget()
        self.summer.setObjectName("summer")

        self.autumn = QtWidgets.QWidget()
        self.autumn.setObjectName("autumn")

        self.winter = QtWidgets.QWidget()
        self.winter.setObjectName("winter")


        self.chooseOOTD.addTab(self.spring, "")
        self.chooseOOTD.addTab(self.summer, "")
        self.chooseOOTD.addTab(self.autumn, "")
        self.chooseOOTD.addTab(self.winter, "")



        self.chooseOOTD.setTabText(self.chooseOOTD.indexOf(self.spring),"봄")
        self.chooseOOTD.setTabText(self.chooseOOTD.indexOf(self.summer),"여름")
        self.chooseOOTD.setTabText(self.chooseOOTD.indexOf(self.autumn),"가을")
        self.chooseOOTD.setTabText(self.chooseOOTD.indexOf(self.winter),"겨울")


        self.chooseOOTD.setStyleSheet("QTabWidget::pane{border-style: solid; border-width: 3px;border-color:#808080}\nQTabBar::tab{ border-style: solid; border-width: 3px;border-color:#808080;color:#808080}")

        self.scrollSpring = QtWidgets.QScrollArea(self.spring)
        self.scrollSpring.setGeometry(10,10,694,577)
        self.scrollSpring.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollSpring.setWidgetResizable(True)
        self.scrollSpring.setObjectName("scrollSpring")

        self.scrollSpringCont = QtWidgets.QWidget()
        self.scrollSpringCont.setGeometry(0, 0, 107, 87)
        self.scrollSpringCont.setObjectName("scrollSpringCont")

        self.groupBoxSpring = QtWidgets.QGroupBox(self.scrollSpringCont)
        self.groupBoxSpring.setGeometry(0, 10, 103, 59)
        self.groupBoxSpring.setObjectName("groupBoxSpring")

        self.horizontal_Spring = QtWidgets.QWidget(self.groupBoxSpring)
        self.horizontal_Spring.setGeometry(20, 20, 560,500)
        self.horizontal_Spring.setObjectName("horizontal_Spring")

        self.verticalLayoutSpring = QtWidgets.QFormLayout(self.horizontal_Spring)
        self.verticalLayoutSpring.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutSpring.setObjectName("verticalLayout")
        self.verticalLayoutSpring.setSpacing(50)
        self.verticalLayoutSpring.setVerticalSpacing(100)

        self.groupBoxSpring.setLayout(self.verticalLayoutSpring)
        self.scrollSpring.setWidget(self.groupBoxSpring)



        self.scrollSummer = QtWidgets.QScrollArea(self.summer)
        self.scrollSummer.setGeometry(10,10,694,577)
        self.scrollSummer.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollSummer.setWidgetResizable(True)
        self.scrollSummer.setObjectName("scrollSummer")

        self.scrollSummerCont = QtWidgets.QWidget()
        self.scrollSummerCont.setGeometry(0, 0, 107, 87)
        self.scrollSummerCont.setObjectName("scrollSummerCont")

        self.groupBoxSummer = QtWidgets.QGroupBox(self.scrollSummerCont)
        self.groupBoxSummer.setGeometry(0, 10, 103, 59)
        self.groupBoxSummer.setObjectName("groupBoxSummer")

        self.horizontal_Summer = QtWidgets.QWidget(self.groupBoxSummer)
        self.horizontal_Summer.setGeometry(20, 20, 560,500)
        self.horizontal_Summer.setObjectName("horizontal_Summer")

        self.verticalLayoutSummer = QtWidgets.QFormLayout(self.horizontal_Summer)
        self.verticalLayoutSummer.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutSummer.setObjectName("verticalLayout")
        self.verticalLayoutSummer.setSpacing(50)
        self.verticalLayoutSummer.setVerticalSpacing(100)

        self.groupBoxSummer.setLayout(self.verticalLayoutSummer)
        self.scrollSummer.setWidget(self.groupBoxSummer)

        self.scrollAutumn = QtWidgets.QScrollArea(self.autumn)
        self.scrollAutumn.setGeometry(10,10,694,577)
        self.scrollAutumn.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollAutumn.setWidgetResizable(True)
        self.scrollAutumn.setObjectName("scrollAutumn")

        self.scrollAutumnCont = QtWidgets.QWidget()
        self.scrollAutumnCont.setGeometry(0, 0, 107, 87)
        self.scrollAutumnCont.setObjectName("scrollAutumnCont")

        self.groupBoxAutumn = QtWidgets.QGroupBox(self.scrollAutumnCont)
        self.groupBoxAutumn.setGeometry(0, 10, 103, 59)
        self.groupBoxAutumn.setObjectName("groupBoxAutumn")

        self.horizontal_Autumn = QtWidgets.QWidget(self.groupBoxAutumn)
        self.horizontal_Autumn.setGeometry(20, 20, 560,500)
        self.horizontal_Autumn.setObjectName("horizontal_Autumn")

        self.verticalLayoutAutumn = QtWidgets.QFormLayout(self.horizontal_Autumn)
        self.verticalLayoutAutumn.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutAutumn.setObjectName("verticalLayout")
        self.verticalLayoutAutumn.setSpacing(50)
        self.verticalLayoutAutumn.setVerticalSpacing(100)

        self.groupBoxAutumn.setLayout(self.verticalLayoutAutumn)
        self.scrollAutumn.setWidget(self.groupBoxAutumn)

        self.scrollWinter = QtWidgets.QScrollArea(self.winter)
        self.scrollWinter.setGeometry(10,10,694,577)
        self.scrollWinter.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollWinter.setWidgetResizable(True)
        self.scrollWinter.setObjectName("scrollWinter")

        self.scrollWinterCont = QtWidgets.QWidget()
        self.scrollWinterCont.setGeometry(0, 0, 107, 87)
        self.scrollWinterCont.setObjectName("scrollWinterCont")

        self.groupBoxWinter = QtWidgets.QGroupBox(self.scrollWinterCont)
        self.groupBoxWinter.setGeometry(0, 10, 103, 59)
        self.groupBoxWinter.setObjectName("groupBoxWinter")

        self.horizontal_Winter = QtWidgets.QWidget(self.groupBoxWinter)
        self.horizontal_Winter.setGeometry(20, 20, 560,500)
        self.horizontal_Winter.setObjectName("horizontal_Winter")

        self.verticalLayoutWinter = QtWidgets.QFormLayout(self.horizontal_Winter)
        self.verticalLayoutWinter.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWinter.setObjectName("verticalLayout")
        self.verticalLayoutWinter.setSpacing(50)
        self.verticalLayoutWinter.setVerticalSpacing(100)

        self.groupBoxWinter.setLayout(self.verticalLayoutWinter)
        self.scrollWinter.setWidget(self.groupBoxWinter)

        self.OOTDBackBtn=QtWidgets.QPushButton(self.PageOOTD)
        self.OOTDBackBtn.setGeometry(40,40,40,40)
        self.OOTDBackBtn.setIcon(QtGui.QIcon("image/back.png"))
        self.OOTDBackBtn.setIconSize(QtCore.QSize(40,40))
        self.OOTDBackBtn.setStyleSheet(" border-style: solid; border-color : white; border-width: 0px;color:white;")
        self.OOTDBackBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


###############################################################################################################

        self.PageplayList=QtWidgets.QWidget()
        self.PageplayList.setObjectName("PageplayList")

        playListBorder=QtWidgets.QLabel(self.PageplayList)
        playListBorder.setGeometry(20,10,771,933)
        playListBorder.setStyleSheet("background-color: white ;border-style: solid;border-color: #A0B4E6; border-width: 10px")

        playListPic=QtWidgets.QLabel(self.PageplayList)
        playListPic.setGeometry(228,73,365,294)
        playListPic.setStyleSheet("background-color:black")
        
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load("image/playList.png")
        self.qPixmapVar=self.qPixmapVar.scaled(365,294)
        playListPic.setPixmap(self.qPixmapVar)

        self.insertVideoBtn=QtWidgets.QToolButton(self.PageplayList)
        self.insertVideoBtn.setGeometry(285,661,228,36)
        self.insertVideoBtn.setStyleSheet("border-style: solid ; border-radius: 10px; border-color:#3057B9 ; border-width:3px; color: #3057B9 ;background-color: white")
        self.insertVideoBtn.setFont(font)
        self.insertVideoBtn.setText("음악추가")
        self.insertVideoBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        QtCore.QMetaObject.connectSlotsByName(self.PageplayList)
        self.stackedWidget.addWidget(self.PageplayList)

        self.alertPlayBtn=QtWidgets.QToolButton(self.PageplayList)
        self.alertPlayBtn.setGeometry(371,36,85,110)
        self.alertPlayBtn.setStyleSheet("border-style: solid ; border-radius: 10px; border-color:#ffffff ; border-width:3px; color: #3057B9 ;background-color: white")
        self.alertPlayBtn.setIcon(QtGui.QIcon("image/say.png"))
        self.alertPlayBtn.setIconSize(QtCore.QSize(85,110))
        self.alertPlayBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        QtCore.QMetaObject.connectSlotsByName(self.PageplayList)
        self.stackedWidget.addWidget(self.PageplayList)

        self.musicName=QtWidgets.QLabel(self.PageplayList)
        self.musicName.setGeometry(114,441,550,73)
        self.musicName.setStyleSheet("background-color:black")
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load("image/playListBar.png")
        self.qPixmapVar=self.qPixmapVar.scaled(578,73)
        self.musicName.setPixmap(self.qPixmapVar)

        self.videoName=QtWidgets.QLabel(self.PageplayList)
        self.videoName.setGeometry(257,441,700,73)
        font = QtGui.QFont()
        self.videoName.setStyleSheet("background-color:#00ffffff ; color:#000000;")
        font.setPointSize(10)
        self.videoName.setFont(font)
        self.videoName.setText("슈프림팀 – 그땐 그땐 그땐")


        self.playMusicBtns=[]
        for index in range(0,4):
            dummyplayBtn=QtWidgets.QToolButton(self.PageplayList)
            dummyplayBtn.setGeometry(80+index*80,590,40,40)
            dummyplayBtn.setStyleSheet("border-style: solid ; border-radius: 10px; border-color:#ffffff ; border-width:3px; color: #ffffff ;background-color: white")
            dummyplayBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            QtCore.QMetaObject.connectSlotsByName(self.PageplayList)
            self.playMusicBtns.append(dummyplayBtn)


        self.playMusicBtns[0].setIcon(QtGui.QIcon("image/play.png"))
        self.playMusicBtns[0].setIconSize(QtCore.QSize(60,60))

        self.playMusicBtns[1].setIcon(QtGui.QIcon("image/stop.png"))
        self.playMusicBtns[1].setIconSize(QtCore.QSize(60,60))

        self.playMusicBtns[2].setIcon(QtGui.QIcon("image/presentStop.png"))
        self.playMusicBtns[2].setIconSize(QtCore.QSize(60,60))

        self.playMusicBtns[3].setIcon(QtGui.QIcon("image/nextMusic.png"))
        self.playMusicBtns[3].setIconSize(QtCore.QSize(60,60))

        self.horizontalSlider = QtWidgets.QSlider(self.PageplayList)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setGeometry(514, 591, 114, 36)
        self.horizontalSlider.setStyleSheet("background-color:white")
        self.horizontalSlider.setObjectName("horizontalSlider")

        musicVolume=QtWidgets.QLabel(self.PageplayList)
        musicVolume.setGeometry(457,588,34,44)
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load("image/volume.png")
        self.qPixmapVar=self.qPixmapVar.scaled(34,44)
        musicVolume.setPixmap(self.qPixmapVar)

        self.playBackBtn=QtWidgets.QPushButton(self.PageplayList)
        self.playBackBtn.setGeometry(40,40,40,40)
        self.playBackBtn.setIcon(QtGui.QIcon("image/back.png"))
        self.playBackBtn.setIconSize(QtCore.QSize(40,40))
        self.playBackBtn.setStyleSheet(" border-style: solid; border-color : white; border-width: 0px;color:white;")
        self.playBackBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


        self.stackedWidget.addWidget(self.PageplayList)

        
##########################################################################################



        self.PageGuide=QtWidgets.QWidget()
        self.PageGuide.setObjectName("PageGuide")

        playListBorder=QtWidgets.QLabel(self.PageGuide)
        playListBorder.setGeometry(20,10,771,933)
        playListBorder.setStyleSheet("background-color: white ;border-style: solid;border-color: #A0B4E6; border-width: 10px")

        self.videoPlay=QtWidgets.QFrame(self.PageGuide)
        self.videoPlay.setGeometry(114,132,571,661)
        self.videoPlay.setStyleSheet("background-color:black ; border-style: solid; border-color : white; border-width: 1px;color:white;")

        self.guideBackBtn=QtWidgets.QPushButton(self.PageGuide)
        self.guideBackBtn.setGeometry(40,40,40,40)
        self.guideBackBtn.setStyleSheet("border-style: solid; border-color : white; border-width: 0px;color:white;")

        self.guideBackBtn.setIcon(QtGui.QIcon("image/back.png"))
        self.guideBackBtn.setIconSize(QtCore.QSize(40,40))

        self.guideBackBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


        self.stackedWidget.addWidget(self.PageGuide)



##########################################################################################



        self.stackedWidget.addWidget(self.PageOOTD)


##########################################################################################

        self.MainWindow.setCentralWidget(self.centralwidget)



    def dialogCloset(self,Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800,1040)
        Dialog.setStyleSheet("background-color : white;")
        self.dialogLabel = QtWidgets.QLabel(Dialog)
        self.dialogLabel.setGeometry(0, 0, 600, 300)
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(18)
        self.dialogLabel.setFont(font)
        self.dialogLabel.setStyleSheet("color : red;")
        self.dialogLabel.setObjectName("label")
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        closetBorder=QtWidgets.QLabel(Dialog)
        closetBorder.setGeometry(20,10,780,1020)
        closetBorder.setStyleSheet("background-color: white ;border-style: solid;border-color: #A0B4E6; border-width: 10px")

        closetDigXY=[[150,80,500,400],[150,475,500,490]]
        self.logoPics=[]
        for index in range(0,2):
            closetDig=QtWidgets.QLabel(Dialog)
            closetDig.setGeometry(closetDigXY[index][0],closetDigXY[index][1],closetDigXY[index][2],closetDigXY[index][3])
            closetDig.setStyleSheet("border-style: solid ; border-color:#808080; border-width:3px")
            self.logoPics.append(closetDig)

        closetNameXY=[[320,250,150,40],[320,700,150,40]]
        closetText=['상의 사진','하의 사진']
        self.logoNames=[]
        for index in range(0,2):
            closetName=QtWidgets.QLabel(Dialog)
            closetName.setText(closetText[index])
            font.setPointSize(14)
            closetName.setFont(font)
            closetName.setAlignment(Qt.AlignCenter)
            closetName.setGeometry(closetNameXY[index][0],closetNameXY[index][1],closetNameXY[index][2],closetNameXY[index][3])
            closetName.setStyleSheet("border-style: solid ; border-radius: 10px; border-color:#A0B4E6; border-width:3px; color : #3057B9;")
            self.logoNames.append(closetName)

    #  dialogClosetBtn 버튼  dialogClosetText - edit
    def dialogClosetCheck(self,Dialog,type):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800,700)
        Dialog.setStyleSheet("background-color : white;")
        self.dialogLabel = QtWidgets.QLabel(Dialog)
        self.dialogLabel.setGeometry(0, 0, 600, 300)
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(18)
        self.dialogLabel.setFont(font)
        self.dialogLabel.setStyleSheet("color : red;")
        self.dialogLabel.setObjectName("label")
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        closetBorder=QtWidgets.QLabel(Dialog)
        closetBorder.setGeometry(20,10,760,680)
        closetBorder.setStyleSheet("background-color: white ;border-style: solid;border-color: #A0B4E6; border-width: 10px")


        self.dialogClosetText = QtWidgets.QLineEdit(Dialog)
        self.dialogClosetText.setGeometry(100 ,300, 600, 150)
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(12)
        self.dialogClosetText.setFont(font)
        self.dialogClosetText.setStyleSheet("background-color:white ; border-style: solid; border-color : #a0b4e6; border-width: 2px;color:#a0b4e6")
        self.dialogClosetText.setObjectName("label")


        
        labelName = QtWidgets.QLabel(Dialog)
        labelName.setGeometry(185,170, 450, 100)
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(12)
        labelName.setFont(font)
        labelName.setStyleSheet("background-color:white;color:#3057B9")
        labelName.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily('함초롬돋움')
        font.setPointSize(16)
        font.setWeight(75)
        labelName.setFont(font)
        if type=="상의":
            labelName.setText("상의 사진 이름을 입력하세요")
        else:
            labelName.setText("하의 사진 이름을 입력하세요")

        self.dialogClosetBtn=QtWidgets.QToolButton(Dialog)
        self.dialogClosetBtn.setGeometry(200,500,400,50)
        self.dialogClosetBtn.setStyleSheet("border-style: solid ; border-radius: 10px; border-color:#A0B4E6; border-width:3px; color: #3057B9;background-color: white")

        self.dialogClosetBtn.setFont(font)
        self.dialogClosetBtn.setText("확인")
        self.dialogClosetBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        QtCore.QMetaObject.connectSlotsByName(Dialog)


# dialogCheckEditBtn  버튼   dialogText edit

    def dialogSchedualCheck(self,Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800,700)
        Dialog.setStyleSheet("background-color : white;")
        self.dialogLabel = QtWidgets.QLabel(Dialog)
        self.dialogLabel.setGeometry(0, 0, 600, 300)
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(18)
        self.dialogLabel.setFont(font)
        self.dialogLabel.setStyleSheet("color : red;")
        self.dialogLabel.setObjectName("label")
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        closetBorder=QtWidgets.QLabel(Dialog)
        closetBorder.setGeometry(20,10,760,680)
        closetBorder.setStyleSheet("background-color: white ;border-style: solid;border-color: #A0B4E6; border-width: 10px")


        self.dialogText = QtWidgets.QLineEdit(Dialog)
        self.dialogText.setGeometry(100 ,300, 600, 150)
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(12)
        self.dialogText.setFont(font)
        self.dialogText.setStyleSheet("background-color:white ; border-style: solid; border-color : #a0b4e6; border-width: 2px;color:#a0b4e6")
        self.dialogText.setObjectName("label")


        
        labelName = QtWidgets.QLabel(Dialog)
        labelName.setGeometry(185,170, 450, 100)
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(12)
        labelName.setFont(font)
        labelName.setStyleSheet("background-color:white;color:#3057B9")
        labelName.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily('함초롬돋움')
        font.setPointSize(16)
        font.setWeight(75)
        labelName.setFont(font)
        labelName.setText("시작시간/끝나는 시간/이름")

        self.dialogCheckEditBtn=QtWidgets.QToolButton(Dialog)
        self.dialogCheckEditBtn.setGeometry(200,500,400,50)
        self.dialogCheckEditBtn.setStyleSheet("border-style: solid ; border-radius: 10px; border-color:#A0B4E6; border-width:3px; color: #3057B9;background-color: white")

        self.dialogCheckEditBtn.setFont(font)
        self.dialogCheckEditBtn.setText("확인")
        self.dialogCheckEditBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        


# dialogOOTDEditBtn 버튼  dialogOOTDEdit  text 에딧
    def dialogOOTDCheck(self,Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800,700)
        Dialog.setStyleSheet("background-color : white;")
        self.dialogLabel = QtWidgets.QLabel(Dialog)
        self.dialogLabel.setGeometry(0, 0, 600, 300)
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(18)
        self.dialogLabel.setFont(font)
        self.dialogLabel.setStyleSheet("color : red;")
        self.dialogLabel.setObjectName("label")
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        closetBorder=QtWidgets.QLabel(Dialog)
        closetBorder.setGeometry(20,10,760,680)
        closetBorder.setStyleSheet("background-color: white ;border-style: solid;border-color: #A0B4E6; border-width: 10px")

        self.dialogOOTDEdit = QtWidgets.QLineEdit(Dialog)
        self.dialogOOTDEdit.setGeometry(100 ,300, 600, 150)
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(12)
        self.dialogOOTDEdit.setFont(font)
        self.dialogOOTDEdit.setStyleSheet("background-color:white ; border-style: solid; border-color : #a0b4e6; border-width: 2px;color:#a0b4e6")
        self.dialogOOTDEdit.setObjectName("label")
        
        labelName = QtWidgets.QLabel(Dialog)
        labelName.setGeometry(185,120, 450, 100)
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(12)
        labelName.setFont(font)
        labelName.setStyleSheet("background-color:white;color:#3057B9")
        labelName.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily('함초롬돋움')
        font.setPointSize(16)
        font.setWeight(75)
        labelName.setFont(font)
        labelName.setText("사진의 이름을 입력하세요")

        self.dialogOOTDEditBtn=QtWidgets.QToolButton(Dialog)
        self.dialogOOTDEditBtn.setGeometry(200,500,400,50)
        self.dialogOOTDEditBtn.setStyleSheet("border-style: solid ; border-radius: 10px; border-color:#A0B4E6; border-width:3px; color: #3057B9;background-color: white")
        self.dialogOOTDEditBtn.setFont(font)
        self.dialogOOTDEditBtn.setText("확인")
        self.dialogOOTDEditBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        font.setPointSize(10)

        self.springBtn=QtWidgets.QCheckBox(Dialog)
        self.springBtn.setGeometry(150,230,100,50)
        self.springBtn.setText("봄")
        self.springBtn.setFont(font)


        self.summerBtn=QtWidgets.QCheckBox(Dialog)
        self.summerBtn.setGeometry(270,230,100,50)
        self.summerBtn.setText("여름")
        self.summerBtn.setFont(font)


        self.autumBtn=QtWidgets.QCheckBox(Dialog)
        self.autumBtn.setGeometry(390,230,100,50)
        self.autumBtn.setText("가을")
        self.autumBtn.setFont(font)


        self.winterBtn=QtWidgets.QCheckBox(Dialog)
        self.winterBtn.setGeometry(510,230,100,50)

        self.winterBtn.setText("겨울")
        self.winterBtn.setFont(font)



    def dialogError(self,Dialog,text):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800,700)
        dialogBorder=QtWidgets.QLabel(Dialog)
        dialogBorder.setGeometry(20,10,760,660)
        dialogBorder.setStyleSheet("background-color: white ;border-style: solid;border-color: #A0B4E6; border-width: 10px")
        Dialog.setStyleSheet("background-color : white;")
        self.dialogLabel = QtWidgets.QLabel(Dialog)
        self.dialogLabel.setGeometry(200, 180, 400, 300)
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(18)
        self.dialogLabel.setFont(font)
        self.dialogLabel.setText(text)
        self.dialogLabel.setStyleSheet("color : red;")
        self.dialogLabel.setObjectName("label")

    
    def dialogSmallMusic(self,Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800,300)
        Dialog.setStyleSheet("background-color : white;")
        self.dialogLabel = QtWidgets.QLabel(Dialog)
        self.dialogLabel.setGeometry(0, 0, 600, 300)
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(18)
        self.dialogLabel.setFont(font)
        self.dialogLabel.setStyleSheet("color : red;")
        self.dialogLabel.setObjectName("label")
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        picture=QtWidgets.QLabel(Dialog)
        picture.setGeometry(0,0,800,700)

        dialogBorder=QtWidgets.QLabel(Dialog)
        dialogBorder.setGeometry(20,10,760,280)
        dialogBorder.setStyleSheet("background-color: white ;border-style: solid;border-color: #A0B4E6; border-width: 10px")

        self.musicName=QtWidgets.QLabel(Dialog)
        self.musicName.setGeometry(80,50,650,100)
        self.musicName.setStyleSheet("background-color:black")
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load("image/playListBar.png")
        self.qPixmapVar=self.qPixmapVar.scaled(683,100)
        self.musicName.setPixmap(self.qPixmapVar)

        self.videoName=QtWidgets.QLabel(Dialog)
        self.videoName.setGeometry(270,50,300,100)
        font = QtGui.QFont()
        self.videoName.setStyleSheet("background-color:#00ffffff ; color:#000000;")
        font.setPointSize(10)
        self.videoName.setFont(font)
        self.videoName.setText("슈프림팀 – 그땐 그땐 그땐")


        self.playMusicBtns=[]
        for index in range(0,4):
            dummyplayBtn=QtWidgets.QToolButton(Dialog)
            dummyplayBtn.setGeometry(80+index*50,200,30,30)
            dummyplayBtn.setStyleSheet("border-style: solid ; border-radius: 10px; border-color:#ffffff ; border-width:3px; color: #ffffff ;background-color: white")
            dummyplayBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            QtCore.QMetaObject.connectSlotsByName(Dialog)
            self.playMusicBtns.append(dummyplayBtn)

        self.playMusicBtns[0].setIcon(QtGui.QIcon("image/play.png"))
        self.playMusicBtns[0].setIconSize(QtCore.QSize(60,60))

        self.playMusicBtns[1].setIcon(QtGui.QIcon("image/stop.png"))
        self.playMusicBtns[1].setIconSize(QtCore.QSize(60,60))

        self.playMusicBtns[2].setIcon(QtGui.QIcon("image/presentStop.png"))
        self.playMusicBtns[2].setIconSize(QtCore.QSize(60,60))

        self.playMusicBtns[3].setIcon(QtGui.QIcon("image/nextMusic.png"))
        self.playMusicBtns[3].setIconSize(QtCore.QSize(60,60))

        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setGeometry(500, 200, 200, 30)
        self.horizontalSlider.setStyleSheet("background-color:white")
        self.horizontalSlider.setObjectName("horizontalSlider")

        musicVolume=QtWidgets.QLabel(Dialog)
        musicVolume.setGeometry(400,200,30,30)
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load("image/volume.png")
        self.qPixmapVar=self.qPixmapVar.scaled(30,30)
        musicVolume.setPixmap(self.qPixmapVar)


    def setCloset(self,value,list):

        if value==1:
            self.scrollTopCont = QtWidgets.QWidget()
            self.scrollTopCont.setGeometry(0, 0, 188, 119)
            self.scrollTopCont.setObjectName("scrollTop")
            
            self.groupBoxTop = QtWidgets.QGroupBox(self.scrollTopCont)
            self.groupBoxTop.setGeometry(0, 10, 181, 81)
            self.groupBoxTop.setObjectName("groupBoxTop")

            self.horizontal_Top = QtWidgets.QWidget(self.groupBoxTop)
            self.horizontal_Top.setGeometry(20, 20, 980,680)
            self.horizontal_Top.setObjectName("horizontal_Top")

            self.verticalLayout = QtWidgets.QGridLayout(self.horizontal_Top)
            self.verticalLayout.setContentsMargins(0, 0, 0, 0)
            self.verticalLayout.setObjectName("verticalLayout")

            self.groupBoxTop.setLayout(self.verticalLayout)
            self.scrollTop.setWidget(self.groupBoxTop)

            self.closetImageBtn=[]

            self.closetImageBtn.clear()
            print(len(list))
            number=0
            for index in range(0,len(list)):
                font = QtGui.QFont()
                font.setFamily("Bebas Neue")
                font.setPointSize(9)
                closetImagesTop=QtWidgets.QToolButton(self.horizontal_Top)
                qPixmapVar = QPixmap()
                image="closet_top/"+str(list[index][2])+".PNG"
                print(image)
                qPixmapVar.load(image)
                qPixmapVar=qPixmapVar.scaled(150, 200)
                icon = QIcon() # QIcon 생성
                icon.addPixmap(qPixmapVar)
                closetImagesTop.setIcon(icon)
                closetImagesTop.setIconSize(QtCore.QSize(150, 200))
                closetImagesTop.setStyleSheet("background-color:black ; border-style: solid; border-color : white; border-width: 1px;color:white")
                closetImagesTop.setFont(font)
                closetImagesTop.setText(list[index][2])
                closetImagesTop.setFixedWidth(150)
                closetImagesTop.setFixedHeight(200)
                closetImagesTop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                if (index+2)%2==0:
                    self.verticalLayout.addWidget(closetImagesTop,0,number)
                else:
                    self.verticalLayout.addWidget(closetImagesTop,1,number)
                    number+=1

                self.closetImageBtn.append(closetImagesTop)

        else:
            self.scrollBottomWidgetContents = QtWidgets.QWidget()
            self.scrollBottomWidgetContents.setGeometry(0, 0, 188, 119)
            self.scrollBottomWidgetContents.setObjectName("scrollBottomWidgetContents")
            
            self.groupBoxBot = QtWidgets.QGroupBox(self.scrollBottomWidgetContents)
            self.groupBoxBot.setGeometry(0, 10, 181, 81)
            self.groupBoxBot.setObjectName("groupBoxBot")

            self.horizontal_Bot = QtWidgets.QWidget(self.groupBoxBot)
            self.horizontal_Bot.setGeometry(20, 20, 980,680)
            self.horizontal_Bot.setObjectName("horizontal_Bot")

            self.verticalLayoutBot = QtWidgets.QGridLayout(self.horizontal_Bot)
            self.verticalLayoutBot.setContentsMargins(0, 0, 0, 0)
            self.verticalLayoutBot.setObjectName("verticalLayoutBot")

            self.groupBoxBot.setLayout(self.verticalLayoutBot)
            self.scrollBottom.setWidget(self.groupBoxBot)

            self.closetImageBtnBot=[]

            self.closetImageBtnBot.clear()
            print(len(list))
            number=0
            for index in range(0,len(list)):
                font = QtGui.QFont()
                font.setFamily("Bebas Neue")
                font.setPointSize(9)
                closetImagesBot=QtWidgets.QToolButton(self.horizontal_Bot)
                qPixmapVar = QPixmap()
                image="closet_bot/"+str(list[index][2])+".PNG"
                print(image)
                qPixmapVar.load(image)
                qPixmapVar=qPixmapVar.scaled(150, 200)
                icon = QIcon() # QIcon 생성
                icon.addPixmap(qPixmapVar)
                closetImagesBot.setIcon(icon)
                closetImagesBot.setIconSize(QtCore.QSize(150, 200))
                closetImagesBot.setStyleSheet("background-color:black ; border-style: solid; border-color : white; border-width: 1px;color:white")
                closetImagesBot.setFont(font)
                closetImagesBot.setText(list[index][2])
                closetImagesBot.setFixedWidth(150)
                closetImagesBot.setFixedHeight(200)
                closetImagesBot.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                if (index+2)%2==0:
                    self.verticalLayoutBot.addWidget(closetImagesBot,0,number)
                else:
                    self.verticalLayoutBot.addWidget(closetImagesBot,1,number)
                    number+=1

                self.closetImageBtnBot.append(closetImagesBot)

        
    def dialogClosetDelete(self,Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800,700)
        Dialog.setStyleSheet("background-color : white;")
        self.dialogLabel = QtWidgets.QLabel(Dialog)
        self.dialogLabel.setGeometry(0, 0, 600, 300)
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(18)
        self.dialogLabel.setFont(font)
        self.dialogLabel.setStyleSheet("color : red;")
        self.dialogLabel.setObjectName("label")
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        closetBorder=QtWidgets.QLabel(Dialog)
        closetBorder.setGeometry(20,10,760,680)
        closetBorder.setStyleSheet("background-color: white ;border-style: solid;border-color: #A0B4E6; border-width: 10px")


        self.dialogClosetText = QtWidgets.QLineEdit(Dialog)
        self.dialogClosetText.setGeometry(100 ,400, 600, 100)
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(12)
        self.dialogClosetText.setFont(font)
        self.dialogClosetText.setStyleSheet("background-color:white ; border-style: solid; border-color : #a0b4e6; border-width: 2px;color:#a0b4e6")
        self.dialogClosetText.setObjectName("label")


        
        labelName = QtWidgets.QLabel(Dialog)
        labelName.setGeometry(200,170, 500, 100)
        font = QtGui.QFont()
        
        labelName.setFont(font)
        labelName.setStyleSheet("background-color:white;color:#3057B9")
        labelName.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(20)
        font.setWeight(75)
        labelName.setFont(font)
        labelName.setText("삭제하실 상의(하의)\n이름을 입력해주세요")

        self.checkBoxTop=QtWidgets.QCheckBox(Dialog)
        self.checkBoxTop.setText("상의")
        self.checkBoxTop.setGeometry(200,300,80,50)
        self.checkBoxTop.setStyleSheet("background-color:white;color:#3057B9")
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(13)
        font.setWeight(75)
        self.checkBoxTop.setFont(font)


        self.checkBoxBot=QtWidgets.QCheckBox(Dialog)
        self.checkBoxBot.setText("하의")
        self.checkBoxBot.setGeometry(300,300,80,50)
        self.checkBoxBot.setStyleSheet("background-color:white;color:#3057B9")
        self.checkBoxBot.setFont(font)



        self.dialogClosetDeleteBtn=QtWidgets.QToolButton(Dialog)
        self.dialogClosetDeleteBtn.setGeometry(200,550,400,50)
        self.dialogClosetDeleteBtn.setStyleSheet("border-style: solid ; border-radius: 10px; border-color:#A0B4E6; border-width:3px; color: #3057B9;background-color: white")

        self.dialogClosetDeleteBtn.setFont(font)
        self.dialogClosetDeleteBtn.setText("확인")
        self.dialogClosetDeleteBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def closetDialogSet(self,type,value):
        try:
            if type==1:
                qPixmapVar = QPixmap()
                qPixmapVar.load(value)
                qPixmapVar=qPixmapVar.scaledToHeight(400)
                print(value)
                self.logoPics[0].setPixmap(qPixmapVar)
                self.logoPics[0].setAlignment(Qt.AlignCenter)
                self.logoNames[0].setText("")
                self.logoNames[0].setStyleSheet("background-color:#00ffffff")


            else:
                qPixmapVar = QPixmap()
                qPixmapVar.load(value)
                qPixmapVar=qPixmapVar.scaledToHeight(490)
                self.logoPics[1].setAlignment(Qt.AlignCenter)
                self.logoPics[1].setPixmap(qPixmapVar)
                self.logoNames[1].setText("")
                self.logoNames[1].setStyleSheet("background-color:#00ffffff")
        except:
            pass

    
    def OOTDset(self,data,seasonCheck):
        if seasonCheck=='Spring':
            season=1
        elif seasonCheck=='Summer':
            season=2

        elif seasonCheck=='Autum':
            season=3
        
        elif seasonCheck=='Winter':
            season=4

        if season==1:
            self.scrollSpringCont = QtWidgets.QWidget()
            self.scrollSpringCont.setGeometry(0, 0, 188, 119)
            self.scrollSpringCont.setObjectName("scrollTop")
            
            self.groupBoxSpring = QtWidgets.QGroupBox(self.scrollSpringCont)
            self.groupBoxSpring.setGeometry(0, 10, 181, 81)
            self.groupBoxSpring.setObjectName("groupBoxSpring")

            self.horizontal_Spring = QtWidgets.QWidget(self.groupBoxSpring)
            self.horizontal_Spring.setGeometry(20, 20, 980,680)
            self.horizontal_Spring.setObjectName("horizontal_Spring")

            self.verticalLayoutSpring = QtWidgets.QGridLayout(self.horizontal_Spring)
            self.verticalLayoutSpring.setContentsMargins(0, 0, 0, 0)
            self.verticalLayoutSpring.setObjectName("verticalLayoutSpring")

            self.groupBoxSpring.setLayout(self.verticalLayoutSpring)
            self.scrollSpring.setWidget(self.groupBoxSpring)

            self.springImageBtn=[]

            self.springImageBtn.clear()
            print(len(data))
            number=0
            for index in range(0,len(data)):
                font = QtGui.QFont()
                font.setFamily("Bebas Neue")
                font.setPointSize(9)
                springImages=QtWidgets.QToolButton(self.horizontal_Top)
                qPixmapVar = QPixmap()
                image="OOTD/Spring/"+str(data[index][2])+".PNG"
                print(image)
                qPixmapVar.load(image)
                qPixmapVar=qPixmapVar.scaled(150, 200)
                icon = QIcon() # QIcon 생성
                icon.addPixmap(qPixmapVar)
                springImages.setIcon(icon)
                springImages.setIconSize(QtCore.QSize(150, 200))
                springImages.setStyleSheet("background-color:black ; border-style: solid; border-color : white; border-width: 1px;color:white")
                springImages.setFont(font)
                springImages.setText(data[index][3])
                springImages.setFixedWidth(150)
                springImages.setFixedHeight(200)
                springImages.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                if (index+2)%2==0:
                    self.verticalLayoutSpring.addWidget(springImages,0,number)
                else:
                    self.verticalLayoutSpring.addWidget(springImages,1,number)
                    number+=1

                self.springImageBtn.append(springImages)
        elif season==2:
            self.scrollSummerCont = QtWidgets.QWidget()
            self.scrollSummerCont.setGeometry(0, 0, 188, 119)
            self.scrollSummerCont.setObjectName("scrollTop")
            
            self.groupBoxSummer = QtWidgets.QGroupBox(self.scrollSummerCont)
            self.groupBoxSummer.setGeometry(0, 10, 181, 81)
            self.groupBoxSummer.setObjectName("groupBoxSummer")

            self.horizontal_Summer = QtWidgets.QWidget(self.groupBoxSummer)
            self.horizontal_Summer.setGeometry(20, 20, 980,680)
            self.horizontal_Summer.setObjectName("horizontal_Summer")

            self.verticalLayoutSummer = QtWidgets.QGridLayout(self.horizontal_Summer)
            self.verticalLayoutSummer.setContentsMargins(0, 0, 0, 0)
            self.verticalLayoutSummer.setObjectName("verticalLayoutSummer")

            self.groupBoxSummer.setLayout(self.verticalLayoutSummer)
            self.scrollSummer.setWidget(self.groupBoxSummer)

            self.SummerImageBtn=[]

            self.SummerImageBtn.clear()
            print(len(data))
            number=0
            for index in range(0,len(data)):
                font = QtGui.QFont()
                font.setFamily("Bebas Neue")
                font.setPointSize(9)
                SummerImages=QtWidgets.QToolButton(self.horizontal_Top)
                qPixmapVar = QPixmap()
                image="OOTD/Summer/"+str(data[index][2])+".PNG"
                print(image)
                qPixmapVar.load(image)
                qPixmapVar=qPixmapVar.scaled(150, 200)
                icon = QIcon() # QIcon 생성
                icon.addPixmap(qPixmapVar)
                SummerImages.setIcon(icon)
                SummerImages.setIconSize(QtCore.QSize(150, 200))
                SummerImages.setStyleSheet("background-color:black ; border-style: solid; border-color : white; border-width: 1px;color:white")
                SummerImages.setFont(font)
                SummerImages.setText(data[index][3])
                SummerImages.setFixedWidth(150)
                SummerImages.setFixedHeight(200)
                SummerImages.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                if (index+2)%2==0:
                    self.verticalLayoutSummer.addWidget(SummerImages,0,number)
                else:
                    self.verticalLayoutSummer.addWidget(SummerImages,1,number)
                    number+=1

                self.SummerImageBtn.append(SummerImages)

        elif season==3:
            self.scrollAutumnCont = QtWidgets.QWidget()
            self.scrollAutumnCont.setGeometry(0, 0, 188, 119)
            self.scrollAutumnCont.setObjectName("scrollTop")
            
            self.groupBoxAutumn = QtWidgets.QGroupBox(self.scrollAutumnCont)
            self.groupBoxAutumn.setGeometry(0, 10, 181, 81)
            self.groupBoxAutumn.setObjectName("groupBoxAutumn")

            self.horizontal_Autumn = QtWidgets.QWidget(self.groupBoxAutumn)
            self.horizontal_Autumn.setGeometry(20, 20, 980,680)
            self.horizontal_Autumn.setObjectName("horizontal_Autumn")

            self.verticalLayoutAutumn = QtWidgets.QGridLayout(self.horizontal_Autumn)
            self.verticalLayoutAutumn.setContentsMargins(0, 0, 0, 0)
            self.verticalLayoutAutumn.setObjectName("verticalLayoutAutumn")

            self.groupBoxAutumn.setLayout(self.verticalLayoutAutumn)
            self.scrollAutumn.setWidget(self.groupBoxAutumn)

            self.AutumnImageBtn=[]

            self.AutumnImageBtn.clear()
            print(len(data))
            number=0
            for index in range(0,len(data)):
                font = QtGui.QFont()
                font.setFamily("Bebas Neue")
                font.setPointSize(9)
                AutumnImages=QtWidgets.QToolButton(self.horizontal_Top)
                qPixmapVar = QPixmap()
                image="OOTD/Autumn/"+str(data[index][2])+".PNG"
                print(image)
                qPixmapVar.load(image)
                qPixmapVar=qPixmapVar.scaled(150, 200)
                icon = QIcon() # QIcon 생성
                icon.addPixmap(qPixmapVar)
                AutumnImages.setIcon(icon)
                AutumnImages.setIconSize(QtCore.QSize(150, 200))
                AutumnImages.setStyleSheet("background-color:black ; border-style: solid; border-color : white; border-width: 1px;color:white")
                AutumnImages.setFont(font)
                AutumnImages.setText(data[index][3])
                AutumnImages.setFixedWidth(150)
                AutumnImages.setFixedHeight(200)
                AutumnImages.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                if (index+2)%2==0:
                    self.verticalLayoutAutumn.addWidget(AutumnImages,0,number)
                else:
                    self.verticalLayoutAutumn.addWidget(AutumnImages,1,number)
                    number+=1

                self.AutumnImageBtn.append(AutumnImages)

        elif season==4:
            self.scrollWinterCont = QtWidgets.QWidget()
            self.scrollWinterCont.setGeometry(0, 0, 188, 119)
            self.scrollWinterCont.setObjectName("scrollTop")
            
            self.groupBoxWinter = QtWidgets.QGroupBox(self.scrollWinterCont)
            self.groupBoxWinter.setGeometry(0, 10, 181, 81)
            self.groupBoxWinter.setObjectName("groupBoxWinter")

            self.horizontal_Winter = QtWidgets.QWidget(self.groupBoxWinter)
            self.horizontal_Winter.setGeometry(20, 20, 980,680)
            self.horizontal_Winter.setObjectName("horizontal_Winter")

            self.verticalLayoutWinter = QtWidgets.QGridLayout(self.horizontal_Winter)
            self.verticalLayoutWinter.setContentsMargins(0, 0, 0, 0)
            self.verticalLayoutWinter.setObjectName("verticalLayoutWinter")

            self.groupBoxWinter.setLayout(self.verticalLayoutWinter)
            self.scrollWinter.setWidget(self.groupBoxWinter)

            self.WinterImageBtn=[]

            self.WinterImageBtn.clear()
            print(len(data))
            number=0
            number2=0
            for index in range(0,len(data)):
                font = QtGui.QFont()
                font.setFamily("Bebas Neue")
                font.setPointSize(9)
                WinterImages=QtWidgets.QToolButton(self.horizontal_Top)
                qPixmapVar = QPixmap()
                image="OOTD/Winter/"+str(data[index][3])+".PNG"
                print(image)
                qPixmapVar.load(image)
                qPixmapVar=qPixmapVar.scaled(150, 200)
                icon = QIcon() # QIcon 생성
                icon.addPixmap(qPixmapVar)
                WinterImages.setIcon(icon)
                WinterImages.setIconSize(QtCore.QSize(150, 200))
                WinterImages.setStyleSheet("background-color:black ; border-style: solid; border-color : white; border-width: 1px;color:white")
                WinterImages.setFont(font)
                WinterImages.setText(data[index][3])
                WinterImages.setFixedWidth(150)
                WinterImages.setFixedHeight(200)
                WinterImages.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                if (index+1)%5==0:
                    number2=0
                    self.verticalLayoutWinter.addWidget(WinterImages,number,number2)
                    number+=1
                else:
                    self.verticalLayoutWinter.addWidget(WinterImages,number,number2)
                    number2+=1


                self.WinterImageBtn.append(WinterImages)


    def dialogPlayList(self,Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800,700)
        Dialog.setStyleSheet("background-color : white;")
        self.dialogLabel = QtWidgets.QLabel(Dialog)
        self.dialogLabel.setGeometry(0, 0, 600, 300)
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(18)
        self.dialogLabel.setFont(font)
        self.dialogLabel.setStyleSheet("color : red;")
        self.dialogLabel.setObjectName("label")
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        closetBorder=QtWidgets.QLabel(Dialog)
        closetBorder.setGeometry(20,10,760,680)
        closetBorder.setStyleSheet("background-color: white ;border-style: solid;border-color: #A0B4E6; border-width: 10px")

        self.dialogPlayListEdit = QtWidgets.QLineEdit(Dialog)
        self.dialogPlayListEdit.setGeometry(100 ,300, 600, 150)
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(12)
        self.dialogPlayListEdit.setFont(font)
        self.dialogPlayListEdit.setStyleSheet("background-color:white ; border-style: solid; border-color : #a0b4e6; border-width: 2px;color:#a0b4e6")
        self.dialogPlayListEdit.setObjectName("label")
        
        labelName = QtWidgets.QLabel(Dialog)
        labelName.setGeometry(185,120, 450, 100)
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(12)
        labelName.setFont(font)
        labelName.setStyleSheet("background-color:white;color:#3057B9")
        labelName.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily('함초롬돋움')
        font.setPointSize(16)
        font.setWeight(75)
        labelName.setFont(font)
        labelName.setText("사진의 이름을 입력하세요")

        self.dialogPlayListBtn=QtWidgets.QToolButton(Dialog)
        self.dialogPlayListBtn.setGeometry(200,500,400,50)
        self.dialogPlayListBtn.setStyleSheet("border-style: solid ; border-radius: 10px; border-color:#A0B4E6; border-width:3px; color: #3057B9;background-color: white")
        self.dialogPlayListBtn.setFont(font)
        self.dialogPlayListBtn.setText("확인")
        self.dialogPlayListBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        font.setPointSize(10)


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main=Ui()
    Main.stackedWidget.setCurrentWidget(Main.PageOOTD)

    dialog=QtWidgets.QDialog()
    Main.dialogOOTDCheck(dialog)
    dialog.show()

    Main.MainWindow.show()
    sys.exit(app.exec_())
    