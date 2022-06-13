from dataclasses import dataclass
import db
import mainUi
import pageJoin, pageFindId,pageFindPw
from tkinter import font
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
import pageMain
import sys
class LoginPage:
    def __init__(self):
        self.db=db.Database()
        self.ui=mainUi.Ui()
        self.join=pageJoin.JoinPage(self.ui,self.db)
        self.Id=pageFindId.FindId(self .ui,self.db)
        self.Pw=pageFindPw.FindPw(self.ui,self.db)
        self.mainPage=pageMain.MainPage(self.ui,self.db)
        self.ui.stackedWidget.setCurrentWidget(self.ui.loginPage)
        self.btnCheckMover()
        self.btnJoinMover()
        self.btnFindIdMover()
        self.btnFindPwMover()

#db랑 입력정보 비교하는 함수
    def memberLogin(self,idValue,pwValue):
        data=self.db.readData("user",["id","pw"],[idValue, pwValue],self.db.cursor1)
        if len(data)!=0:
            dialogError=QtWidgets.QDialog()
            self.ui.dialogError(dialogError,"로그인 성공")
            dialogError.show()
            dialogError.exec()
            self.ui.stackedWidget.setCurrentWidget(self.ui.PageMain) #창 선택페이지로 바꿔야뎀
            self.editClear()
            self.mainPage.rename(data[0][1])

        else:
            dialogError=QtWidgets.QDialog()
            self.ui.dialogError(dialogError,"로그인 실패")
            dialogError.show()
            dialogError.exec()

#확인 버튼 누르면 -> 이메일 비번 db에서 찾기
    def btnCheckMover(self):
        self.ui.loginBtn.clicked.connect(self.checkmove)
    def checkmove(self):
        myEmail=self.ui.loginIdEnter.text()
        myPw=self.ui.loginPwEnter.text()
        self.memberLogin(myEmail, myPw)

#회원가입 버튼 누르면 -> joinPage로 이동
    def btnJoinMover(self):
        self.ui.loginJoinBtn.clicked.connect(self.joinmove)
    def joinmove(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.joinPage)

#이메일 찾기 버튼 누르면 -> findIdPage로 이동
    def btnFindIdMover(self):
        self.ui.loginIdBtn.clicked.connect(self.FindIdmove)
    def FindIdmove(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.findId)

#비밀번호 찾기 버튼 누르면 -> findPwPage로 이동     
    def btnFindPwMover(self):
        self.ui.loginPwBtn.clicked.connect(self.FindPwMove)
    def FindPwMove(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.findPw)

    def editClear(self):
        self.ui.loginPwEnter.setText("")
        self.ui.loginIdEnter.setText("")


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    lg=LoginPage()
    sys.exit(app.exec_()) 
