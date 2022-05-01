from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
import sys
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class Ui():
    
    def __init__(self):
        self.MainWindow=QtWidgets.QMainWindow()
        self.MainWindow.setGeometry(800,60,1400,1350)
        self.MainWindow.setMinimumSize(1400,1350)
        self.MainWindow.setMaximumSize(1400,1350)
        self.MainWindow.setStyleSheet("background-color : white;")

        self.centralwidget = QtWidgets.QWidget(self.MainWindow)

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(0,0,1500,1600)

        self.stackedWidget.setObjectName("stackedWidget")
#########################################################################################
#font 

        fontMart = QtGui.QFont()
        fontMart.setFamily("Nanum Gothic Coding")

# color 

#color - #A0B4E6 연파
# #808080 회색
        

        fontDB = QFontDatabase()
        fontDB.addApplicationFont('./Od크림라떼.ttf')

        font = QtGui.QFont()
        font.setFamily('HY엽서L')
        font.setPointSize(16)
        font.setWeight(75)


#########################################################################################
#pageCloset
        self.PageCloset=QtWidgets.QWidget()
        self.PageCloset.setObjectName("PageCloset")

        closetBorder=QtWidgets.QLabel(self.PageCloset)
        closetBorder.setGeometry(20,10,1350,1270)
        closetBorder.setStyleSheet("background-color: white ;border-style: solid;border-color: #A0B4E6; border-width: 10px")

        closetPicXY=[[100,30,144,320],[1150,30,144,320]]
        logoPics=[]
        for index in range(0,2):
            closetPic=QtWidgets.QLabel(self.PageCloset)
            closetPic.setGeometry(closetPicXY[index][0],closetPicXY[index][1],closetPicXY[index][2],closetPicXY[index][3])
            closetPic.setStyleSheet("background-color:black")
            logoPics.append(closetPic)


        closetAd=QtWidgets.QLabel(self.PageCloset)
        closetAd.setGeometry(290,220,810,160)
        closetAd.setStyleSheet("background-color:black")
        logoPics.append(closetPic)

        font = QtGui.QFont()
        font.setFamily('HY엽서L')
        font.setPointSize(16)
        font.setWeight(75)

        closetPicXY=[[280,30,384,80],[730,30,384,80],[280,120,384,80],[730,120,384,80]]
        closetBtnText=['상의 추가','하의 추가','선택','삭제']
        self.closetBtns=[]
        for index in range(0,4):
            closetBtn=QtWidgets.QToolButton(self.PageCloset)
            closetBtn.setGeometry(closetPicXY[index][0],closetPicXY[index][1],closetPicXY[index][2],closetPicXY[index][3])
            closetBtn.setStyleSheet("background-color:white;border-style: solid;border-color: #A0B4E6;border-width: 5px;color:#3057B9")
            closetBtn.setText(closetBtnText[index])
            closetBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            closetBtn.setFont(font)

            self.closetBtns.append(closetBtn)

        self.chooseCloset = QtWidgets.QTabWidget(self.PageCloset)
        self.chooseCloset.setGeometry(70,380, 1250, 850)
        font = QtGui.QFont()
        font.setFamily('HY엽서L')
        font.setPointSize(16)
        font.setWeight(75)
        self.chooseCloset.setFont(font)
        self.chooseCloset.setObjectName("chooseCloset")
        
        self.chooseBottom = QtWidgets.QWidget()
        self.chooseBottom.setObjectName("chooseBottom")
        self.chooseTop = QtWidgets.QWidget()
        self.chooseTop.setObjectName("chooseTop")

        self.chooseCloset.addTab(self.chooseBottom, "")
        self.chooseCloset.addTab(self.chooseTop, "")


        self.chooseCloset.setTabText(self.chooseCloset.indexOf(self.chooseBottom),"하의")
        self.chooseCloset.setTabText(self.chooseCloset.indexOf(self.chooseTop),"상의")

        
        self.chooseCloset.setStyleSheet("QTabWidget::pane{border-style: solid; border-width: 3px;border-color:#808080}\nQTabBar::tab{ border-style: solid; border-width: 3px;border-color:#808080;color:#808080}")

        self.scrollTop = QtWidgets.QScrollArea(self.chooseTop)
        self.scrollTop.setGeometry(10,10,1215,785)
        self.scrollTop.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollTop.setWidgetResizable(True)
        self.scrollTop.setObjectName("scrollTop")

        self.scrollTopWidgetContents = QtWidgets.QWidget()
        self.scrollTopWidgetContents.setGeometry(0, 0, 188, 119)
        self.scrollTopWidgetContents.setObjectName("scrollTopWidgetContents")

        self.groupBox = QtWidgets.QGroupBox(self.scrollTopWidgetContents)
        self.groupBox.setGeometry(0, 10, 181, 81)
        self.groupBox.setObjectName("groupBox")

        self.horizontal_Top = QtWidgets.QWidget(self.groupBox)
        self.horizontal_Top.setGeometry(20, 20, 980,680)
        self.horizontal_Top.setObjectName("horizontal_Top")

        self.verticalLayout = QtWidgets.QFormLayout(self.horizontal_Top)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setSpacing(50)
        self.verticalLayout.setVerticalSpacing(100)

        self.groupBox.setLayout(self.verticalLayout)
        self.scrollTop.setWidget(self.groupBox)

        self.scrollBottom = QtWidgets.QScrollArea(self.chooseBottom)
        self.scrollBottom.setGeometry(10,10,1215,785)
        self.scrollBottom.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollBottom.setWidgetResizable(True)
        self.scrollBottom.setObjectName("scrollBottom")

        self.scrollBottomWidgetContents = QtWidgets.QWidget()
        self.scrollBottomWidgetContents.setGeometry(0, 0, 188, 119)
        self.scrollBottomWidgetContents.setObjectName("scrollBottomWidgetContents")

        self.groupBox = QtWidgets.QGroupBox(self.scrollBottomWidgetContents)
        self.groupBox.setGeometry(0, 10, 181, 81)
        self.groupBox.setObjectName("groupBox")

        self.horizontal_Top = QtWidgets.QWidget(self.groupBox)
        self.horizontal_Top.setGeometry(20, 20, 980,680)
        self.horizontal_Top.setObjectName("horizontal_Top")

        self.verticalLayout = QtWidgets.QFormLayout(self.horizontal_Top)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setSpacing(50)
        self.verticalLayout.setVerticalSpacing(100)

        self.groupBox.setLayout(self.verticalLayout)
        self.scrollBottom.setWidget(self.groupBox)



        
        self.stackedWidget.addWidget(self.PageCloset)


##############################################################################################

        self.PageSchedule=QtWidgets.QWidget()
        self.PageSchedule.setObjectName("PageSchedule")

        scheduleBorder=QtWidgets.QLabel(self.PageSchedule)
        scheduleBorder.setGeometry(20,10,1350,1270)
        scheduleBorder.setStyleSheet("background-color: white ;border-style: solid;border-color: #A0B4E6; border-width: 10px")

        schedulePic=QtWidgets.QLabel(self.PageSchedule)
        schedulePic.setGeometry(625,30,144,320)
        schedulePic.setStyleSheet("background-color:black")

        self.scheduleBtn=QtWidgets.QToolButton(self.PageSchedule)
        self.scheduleBtn.setGeometry(500,400,400,50)
        self.scheduleBtn.setStyleSheet("border-style: solid ; border-radius: 10px; border-color:#A0B4E6; border-width:3px; color: #3057B9;background-color: white")
        self.scheduleBtn.setFont(font)
        self.scheduleBtn.setText("확인")
        self.scheduleBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        QtCore.QMetaObject.connectSlotsByName(self.PageSchedule)


        self.calander = QtWidgets.QCalendarWidget(self.PageSchedule)
        self.calander.setGeometry(120, 500, 1150, 700)
        self.calander.setStyleSheet("background-color :white;color :#808080;border-style:solid;border-color:#A0B4E6")
        self.calander.setSelectedDate(QtCore.QDate(2022, 5, 1))
        self.calander.setGridVisible(True)
        self.calander.setObjectName("calander")
        font.setPointSize(8)
        self.calander.setFont(font)


        self.stackedWidget.addWidget(self.PageSchedule)

       


##########################################################################################


        self.PageScheduleCheck=QtWidgets.QWidget()
        self.PageScheduleCheck.setObjectName("PageScheduleCheck")

        scheduleBorder=QtWidgets.QLabel(self.PageScheduleCheck)
        scheduleBorder.setGeometry(20,10,1350,1270)
        scheduleBorder.setStyleSheet("background-color: white ;border-style: solid;border-color: #A0B4E6; border-width: 10px")

        schedulePic=QtWidgets.QLabel(self.PageScheduleCheck)
        schedulePic.setGeometry(625,30,144,320)
        schedulePic.setStyleSheet("background-color:black")

        self.scheduleCheckBtn=QtWidgets.QToolButton(self.PageScheduleCheck)
        self.scheduleCheckBtn.setGeometry(250,1150,400,50)
        self.scheduleCheckBtn.setStyleSheet("border-style: solid ; border-radius: 10px; border-color:#A0B4E6; border-width:3px; color: #3057B9;background-color: white")
        font.setPointSize(16)
        self.scheduleCheckBtn.setFont(font)
        self.scheduleCheckBtn.setText("일정추가")
        self.scheduleCheckBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        QtCore.QMetaObject.connectSlotsByName(self.PageScheduleCheck)

        self.scheduleCheckBtn=QtWidgets.QToolButton(self.PageScheduleCheck)
        self.scheduleCheckBtn.setGeometry(750,1150,400,50)
        self.scheduleCheckBtn.setStyleSheet("border-style: solid ; border-radius: 10px; border-color:#A0B4E6; border-width:3px; color: #3057B9;background-color: white")
        self.scheduleCheckBtn.setFont(font)
        self.scheduleCheckBtn.setText("일정삭제")
        self.scheduleCheckBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        QtCore.QMetaObject.connectSlotsByName(self.PageScheduleCheck)



        scrollArea = QtWidgets.QScrollArea(self.PageScheduleCheck)
        scrollArea.setGeometry(100,370,1200,750)
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

        self.groupBox.setLayout(self.verticalLayout)
        scrollArea.setWidget(self.groupBox)



        self.stackedWidget.addWidget(self.PageScheduleCheck)
##########################################################################################





        self.PageOOTD=QtWidgets.QWidget()
        self.PageOOTD.setObjectName("PageOOTD")

        scheduleBorder=QtWidgets.QLabel(self.PageOOTD)
        scheduleBorder.setGeometry(20,10,1350,1270)
        scheduleBorder.setStyleSheet("background-color: white ;border-style: solid;border-color: #A0B4E6; border-width: 10px")

        OOTDPic=QtWidgets.QLabel(self.PageOOTD)
        OOTDPic.setGeometry(450,30,240,320)
        OOTDPic.setStyleSheet("background-color:black")

        OOTDPic=QtWidgets.QLabel(self.PageOOTD)
        OOTDPic.setGeometry(100,30,240,320)
        OOTDPic.setStyleSheet("background-color:black")

        self.scheduleBtn=QtWidgets.QToolButton(self.PageOOTD)
        self.scheduleBtn.setGeometry(800,200,400,50)
        self.scheduleBtn.setStyleSheet("border-style: solid ; border-radius: 10px; border-color:#A0B4E6; border-width:3px; color: #3057B9;background-color: white")
        self.scheduleBtn.setFont(font)
        self.scheduleBtn.setText("OOTD 추가")
        self.scheduleBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        QtCore.QMetaObject.connectSlotsByName(self.PageOOTD)

        
        
        self.scrollAreaOOTD = QtWidgets.QScrollArea(self.PageOOTD)
        self.scrollAreaOOTD.setGeometry(100,400,1230,800)
        self.scrollAreaOOTD.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollAreaOOTD.setWidgetResizable(True)
        self.scrollAreaOOTD.setObjectName("scrollAreaOOTD")

        self.scrollAreaOOTDWidgetContents = QtWidgets.QWidget()
        self.scrollAreaOOTDWidgetContents.setGeometry(0, 0, 188, 119)
        self.scrollAreaOOTDWidgetContents.setObjectName("scrollAreaOOTDWidgetContents")

        self.groupBoxOOTD = QtWidgets.QGroupBox(self.scrollAreaOOTDWidgetContents)
        self.groupBoxOOTD.setGeometry(0, 10, 181, 81)
        self.groupBoxOOTD.setObjectName("groupBoxOOTD")

        self.verticalLayoutWidgetOOTD = QtWidgets.QWidget(self.groupBoxOOTD)
        self.verticalLayoutWidgetOOTD.setGeometry(20, 20, 980,680)
        self.verticalLayoutWidgetOOTD.setObjectName("verticalLayoutWidgetOOTD")

        self.verticalLayoutOOTD = QtWidgets.QFormLayout(self.verticalLayoutWidgetOOTD)
        self.verticalLayoutOOTD.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutOOTD.setObjectName("verticalLayoutOOTD")
        self.verticalLayoutOOTD.setSpacing(50)
        self.verticalLayoutOOTD.setVerticalSpacing(100)

        self.groupBoxOOTD.setLayout(self.verticalLayoutOOTD)
        self.scrollAreaOOTD.setWidget(self.groupBoxOOTD)





        self.stackedWidget.addWidget(self.PageOOTD)





##########################################################################################
        self.stackedWidget.setCurrentWidget(self.PageOOTD)

        self.MainWindow.setCentralWidget(self.centralwidget)




    def dialogCloset(self,Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800,1040)
        Dialog.setStyleSheet("background-color : white;")
        self.dialogLabel = QtWidgets.QLabel(Dialog)
        self.dialogLabel.setGeometry(0, 0, 600, 300)
        font = QtGui.QFont()
        font.setFamily("HY엽서L")
        font.setPointSize(18)
        self.dialogLabel.setFont(font)
        self.dialogLabel.setStyleSheet("color : red;")
        self.dialogLabel.setObjectName("label")
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        closetBorder=QtWidgets.QLabel(Dialog)
        closetBorder.setGeometry(20,10,780,1020)
        closetBorder.setStyleSheet("background-color: white ;border-style: solid;border-color: #A0B4E6; border-width: 10px")

        closetDigXY=[[150,80,500,430],[150,505,500,430]]
        logoPics=[]
        for index in range(0,2):
            closetDig=QtWidgets.QLabel(Dialog)
            closetDig.setGeometry(closetDigXY[index][0],closetDigXY[index][1],closetDigXY[index][2],closetDigXY[index][3])
            closetDig.setStyleSheet("border-style: solid ; border-color:#808080; border-width:3px")
            logoPics.append(closetDig)

        closetNameXY=[[320,250,150,40],[320,700,150,40]]
        closetText=['상의 사진','하의 사진']
        
        logoNames=[]
        for index in range(0,2):
            closetName=QtWidgets.QLabel(Dialog)
            closetName.setText(closetText[index])
            font.setPointSize(14)
            closetName.setFont(font)
            closetName.setAlignment(Qt.AlignCenter)
            closetName.setGeometry(closetNameXY[index][0],closetNameXY[index][1],closetNameXY[index][2],closetNameXY[index][3])
            closetName.setStyleSheet("border-style: solid ; border-radius: 10px; border-color:#A0B4E6; border-width:3px; color : #3057B9;")
            logoNames.append(closetName)

    #  dialogClosetBtn 버튼  dialogClosetText - edit
    def dialogClosetCheck(self,Dialog,type):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800,700)
        Dialog.setStyleSheet("background-color : white;")
        self.dialogLabel = QtWidgets.QLabel(Dialog)
        self.dialogLabel.setGeometry(0, 0, 600, 300)
        font = QtGui.QFont()
        font.setFamily("HY엽서L")
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
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.dialogClosetText.setFont(font)
        self.dialogClosetText.setStyleSheet("background-color:white ; border-style: solid; border-color : #a0b4e6; border-width: 2px;color:#a0b4e6")
        self.dialogClosetText.setObjectName("label")


        
        labelName = QtWidgets.QLabel(Dialog)
        labelName.setGeometry(185,170, 450, 100)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        labelName.setFont(font)
        labelName.setStyleSheet("background-color:white;color:#3057B9")
        labelName.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily('HY엽서L')
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
        font.setFamily("HY엽서L")
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
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.dialogText.setFont(font)
        self.dialogText.setStyleSheet("background-color:white ; border-style: solid; border-color : #a0b4e6; border-width: 2px;color:#a0b4e6")
        self.dialogText.setObjectName("label")


        
        labelName = QtWidgets.QLabel(Dialog)
        labelName.setGeometry(185,170, 450, 100)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        labelName.setFont(font)
        labelName.setStyleSheet("background-color:white;color:#3057B9")
        labelName.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily('HY엽서L')
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
        font.setFamily("HY엽서L")
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
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.dialogOOTDEdit.setFont(font)
        self.dialogOOTDEdit.setStyleSheet("background-color:white ; border-style: solid; border-color : #a0b4e6; border-width: 2px;color:#a0b4e6")
        self.dialogOOTDEdit.setObjectName("label")
        
        labelName = QtWidgets.QLabel(Dialog)
        labelName.setGeometry(185,170, 450, 100)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        labelName.setFont(font)
        labelName.setStyleSheet("background-color:white;color:#3057B9")
        labelName.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily('HY엽서L')
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




    

        


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main=Ui()
    
    dialog=QtWidgets.QDialog()
    Main.dialogOOTDCheck(dialog)
    dialog.show()

    Main.MainWindow.show()
    sys.exit(app.exec_())
    