"""
In this example, we demonstrate how to create simple camera viewer using Opencv3 and PyQt5

Author: Berrouba.A
Last edited: 21 Feb 2018
"""

# import system module
import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.Qt import Qt
import time

# import Opencv module
import cv2

from ui_main_window import *
class MainWindow(QWidget):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function
        self.ui.control_bt.clicked.connect(self.controlTimer)
        self.ui.calib_bt.clicked.connect(self.kalibrasi)


    # view camera
    def viewCam(self):
        # read image in BGR format
        ret, image = self.cap.read()
        #save img
        self.frame=image
        self.ui.capture_bt.clicked.connect(self.save_img)
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        #qImg_scaled=qImg.scaled(width*0.5, height*0.5, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        qImg_scaled=qImg.scaledToHeight(height*0.5, Qt.SmoothTransformation)
        pixmap = QPixmap.fromImage(qImg_scaled)
        self.ui.image_label.setPixmap(pixmap)

    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            self.make_720p()
            # start timer
            self.timer.start(20)
            # update control_bt text
            self.ui.control_bt.setText("Stop")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
            self.ui.control_bt.setText("Start")
            self.ui.image_label.setText("Process the image...")
                     
    def save_img(self):
        cv2.imwrite(filename='saved_img.jpg', img=self.frame)
        #self.cap.release()
        time.sleep(10/ 1000.0)
        # get image infos
        height, width, channel = self.frame.shape
        step = channel * width
        # create QImage from image
        frame=cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        qImg = QImage(frame.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        qImg_scaled=qImg.scaledToHeight(height*0.5, Qt.SmoothTransformation)
        pixmap = QPixmap.fromImage(qImg_scaled)
        self.ui.image_label.setPixmap(pixmap)
       
       
       #self.ui.image_label.setPixmap(QtGui.QPixmap("saved_img.jpg"))
       #self.ui.image_label.setScaledContents(True)
       
             
    def make_1080p(self):
        self.cap.set(3, 1920)
        self.cap.set(4, 1080)

    def make_720p(self):
        self.cap.set(3, 1280)
        self.cap.set(4, 960)

    def make_480p(self):
        self.cap.set(3, 640)
        self.cap.set(4, 480)

    def change_res(self, width, height):
        self.cap.set(3, width)
        self.cap.set(4, height)
    def kalibrasi(self):
        tinggi=self.ui.text_Timg.toPlainText()
        jarak=self.ui.text_Treal.toPlainText()
        if self.num_there(jarak) and self.num_there(tinggi):
            tangen=int(jarak)/int(tinggi)
        else:
            tangen=0
        print (tangen)
        return tangen
    
    def num_there(self,s):
        return all(i.isdigit() for i in s)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())