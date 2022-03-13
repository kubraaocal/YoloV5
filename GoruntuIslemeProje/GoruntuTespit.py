import cv2
import os
from PyQt5 import QtGui

def pixDonustur(goruntu):#label basma işleminde dönüştürme yapıyor.
    fotograf = QtGui.QImage(goruntu, goruntu.shape[1],goruntu.shape[0], goruntu.shape[1] * 3, QtGui.QImage.Format_RGB888)
    pix = QtGui.QPixmap(fotograf)
    return pix

def goruntuTespit(arayuz):
    goruntu = cv2.imread("runs/detect/" + os.listdir("runs/detect")[-1] + "/fotograf.jpg")
    goruntu = cv2.resize(goruntu, (561, 500))

    pix = pixDonustur(goruntu)
    arayuz.lbl_arayuz.setPixmap(pix)

def goruntuTespitiniBaslat(arayuz):
            os.system('cmd /c "python yolov5/detect.py --weights EnIyiAgirlik/best.pt --img 640 --conf 0.25 --source GoruntuTespit/fotograf.jpg" ')
            goruntuTespit(arayuz)


