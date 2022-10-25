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
        uic.loadUi("login.ui",self)

        self.show()
        self.login_btn.clicked.connect(self.Login)
        self.back_btn.clicked.connect(self.Back)
        self.next_btn.clicked.connect(self.Next)
        

    def Login(self):
        if self.username_txt.text()=="goks" and self.password_txt.text()=="pass":
            self.stackedWidget.setCurrentWidget(self.page_2)
            
        else:
            message = QMessageBox()
            message.setText("Invalid Login")
            message.exec_()

    def Back(self):
        self.stackedWidget.setCurrentWidget(self.page_1)

    def Next(self):
        self.stackedWidget.setCurrentWidget(self.page_3)


def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()
    
if __name__=='__main__':
    homebtn_pub=rospy.Publisher('/home_btn',Bool,queue_size=1)
    # homebtn_2_pub=rospy.Publisher('/home_btn_2',Bool,queue_size=1)
    # menubtn_pub=rospy.Publisher('/Menu_btn',Bool,queue_size=1)
    rospy.init_node('main',anonymous=True)
    main()