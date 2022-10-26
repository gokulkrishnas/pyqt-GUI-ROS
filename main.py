from curses import window
from email import message
from re import T
import sys
import rospy
import platform

from std_msgs.msg import Bool,Int8,String
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets

class MyGUI(QDialog):

    def __init__(self):
        super(MyGUI,self).__init__()
        uic.loadUi("GUI_Robo.ui",self)

        self.show()
        self.login_btn.clicked.connect(self.Login)
        self.back_btn.clicked.connect(self.Page_4)
        self.home_btn.clicked.connect(self.Back_to_login)
        self.rviz_btn.clicked.connect(self.RVIZ)
        

    def Login(self):
        if self.username_txt.text()=="g" and self.password_txt.text()=="p":
            self.stackedWidget.setCurrentWidget(self.page_2)
            msg = "Logged in successfully!!!!"
            pub.publish(msg)

        else:
            message = QMessageBox()
            message.setText("Invalid Login")
            message.exec_()

    def Back_to_login(self):
        self.stackedWidget.setCurrentWidget(self.page_1)

    def RVIZ(self):
        self.stackedWidget.setCurrentWidget(self.page_3)

    def Page_4(self):
        self.stackedWidget.setCurrentWidget(self.page_4)


def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()
    
if __name__=='__main__':
    pub=rospy.Publisher('/login_btn',String,queue_size=1)
    # homebtn_2_pub=rospy.Publisher('/home_btn_2',Bool,queue_size=1)
    # menubtn_pub=rospy.Publisher('/Menu_btn',Bool,queue_size=1)
    rospy.init_node('main',anonymous=True)
    main()
