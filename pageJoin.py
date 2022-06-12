import re
from sqlite3 import dbapi2
from tkinter import font
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
import sys
class JoinPage:
    def __init__ (self,UI,db):
        self.db=db
        self.ui=UI
        self.joinCheckBtn()
        self.btnJoinBackMover()
    
    def editClear(self):
        self.ui.joinNameEnter.setText("")
        self.ui.joinEmailEnter.setText("") 
        self.ui.joinPwEnter.setText("") 
        self.ui.joinBirthEnter.setText("")    

    def join(self,values):
        data=self.db.readData("user",["id"],[self.myEmail],self.db.cursor1)
        data2=self.db.readData("user",["name","birth"],[self.myName,self.myBirth],self.db.cursor1)

        if len(data)==0 and len(data2)==0:
            self.db.insertData("user", self.db.rows1, values,self.db.cursor1,self.db.connect1) 
            dialogError=QtWidgets.QDialog()
            self.ui.dialogError(dialogError,"회원가입에 성공했습니다.")
            dialogError.show()
            dialogError.exec()
            self.ui.stackedWidget.setCurrentWidget(self.ui.loginPage) #바꿔야됨 그 선택페이지로

        else:
            dialogError=QtWidgets.QDialog()
            self.ui.dialogError(dialogError,"이미 가입된 정보입니다 !!")
            dialogError.show()
            dialogError.exec()
            
# joinpage의 뒤로가기버튼
    def btnJoinBackMover(self):
        self.ui.joinBacktoLogin.clicked.connect(self.backtoLoginMove)
    def backtoLoginMove(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.loginPage)

# joinpage에서 가입 버튼을 누를시 -> 이메일,비번,생년월일,이름에 대한 예외처리 진행
    def joinCheckBtn(self):
        self.ui.joinBtn.clicked.connect(self.exceptRun)
    def exceptRun(self):
        check=True
        id=""
        add1=""
        add2=""
        self.myName=self.ui.joinNameEnter.text()  
        self.myEmail=self.ui.joinEmailEnter.text()
        self.myPw=self.ui.joinPwEnter.text()
        self.myBirth=self.ui.joinBirthEnter.text()
    # 이름 예외처리 
        if len(self.myName)<2:
            dialogError=QtWidgets.QDialog()
            self.ui.dialogError(dialogError,"이름은 2글자 이상 입력해주세요.")
            dialogError.show()
            dialogError.exec()
            check=False
        else:
            if self.myName.isalpha():     
                hangul = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')  
                result_name = hangul.findall(self.myName)
                if len(result_name)==0:
                    dialogError=QtWidgets.QDialog()
                    self.ui.dialogError(dialogError,"이름은 2글자 이상 입력해주세요.")
                    dialogError.show()
                    dialogError.exec()
                    check=False

            else:
                dialogError=QtWidgets.QDialog()
                self.ui.dialogError(dialogError,"이름은 한글로 입력해주세요.// 숫자 안됨.")
                dialogError.show()
                dialogError.exec()
                check=False

    # 이메일 예외처리
        if "@" and "." in self.myEmail:
            a="@"
            b="."
            if(self.myEmail.find(a)>self.myEmail.find(b)):
                dialogError=QtWidgets.QDialog()
                self.ui.dialogError(dialogError,"올바르지 않은 이메일 형식입니다.")
                dialogError.show()
                dialogError.exec()
                check=False
            else:
                id,address=self.myEmail.split("@")
                add1,add2=address.split(".")
                if id.encode().isalnum() and add1.encode().isalpha() and add2.encode().isalpha() :
                    pass
                else:
                    dialogError=QtWidgets.QDialog()
                    self.ui.dialogError(dialogError,"올바르지 않은 이메일 형식입니다.")
                    dialogError.show()
                    dialogError.exec()
                    check=False
        else:
            dialogError=QtWidgets.QDialog()
            self.ui.dialogError(dialogError,"올바르지 않은 이메일 형식입니다.")
            dialogError.show()
            dialogError.exec()
            check=False
        
    # 비밀번호 예외처리
        if len(self.myPw)<8:
            dialogError=QtWidgets.QDialog()
            self.ui.dialogError(dialogError,"비밀번호는 8자리 이상입니다.")
            dialogError.show()
            dialogError.exec()
            check=False
        
        if self.myPw.encode().isalnum():
            dialogError=QtWidgets.QDialog()
            self.ui.dialogError(dialogError,"비밀번호는 영어,숫자, 특수문자로 이루어져야 합니다.")
            dialogError.show()
            dialogError.exec()
            check=False
        else:
            new_myPw = re.sub(r"[^a-zA-Z0-9]","",self.myPw)
            if new_myPw.isdigit():
                dialogError=QtWidgets.QDialog()
                self.ui.dialogError(dialogError,"비밀번호는 영어,숫자, 특수문자로 이루어져야 합니다.")
                dialogError.show()
                dialogError.exec()
                check=False
            else:
                hangul = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')  
                result = hangul.findall(self.myPw)

                if len(result)>0:
                    dialogError=QtWidgets.QDialog()
                    self.ui.dialogError(dialogError,"비밀번호는 영어,숫자, 특수문자로 이루어져야 합니다.")
                    dialogError.show()
                    dialogError.exec()
                    check=False
                
    # 생년월일 예외처리
        if len(self.myBirth)==8:
            if self.myBirth.isdigit()==False:
                dialogError=QtWidgets.QDialog()
                self.ui.dialogError(dialogError,"생년월일은 숫자로 적어주세요")
                dialogError.show()
                dialogError.exec()
                check=False
            else:
                if len(self.myBirth)>0:
                    if int(self.myBirth)<19200000 or int(self.myBirth)>20210000:
                        dialogError=QtWidgets.QDialog()
                        self.ui.dialogError(dialogError,"년도는 1920~2020 사이만 가능합니다.")
                        dialogError.show()
                        dialogError.exec()
                        check=False
        else:
            dialogError=QtWidgets.QDialog()
            self.ui.dialogError(dialogError,"생년월일은 8자리로 적어주세요.")
            dialogError.show()
            dialogError.exec()
            check=False

    #회원가입 정보 db에 올리기
        if check==True:
            self.memberData=[self.myName,self.myEmail,self.myPw,self.myBirth]
            self.editClear()
            self.join(self.memberData)
            
        