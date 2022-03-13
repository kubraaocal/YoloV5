from tkinter import filedialog
import cv2
from PyQt5 import QtGui
from tkinter import *

root = Tk()#root,diğer tüm widget'ların girdiği kök penceredir.
# Bu, Tk sınıfının bir örneğidir ve her tkinter uygulamasının
# bu sınıfın tam olarak bir örneğine sahip olması gerekir. app,
# Frame'in bir alt sınıfı olan App sınıfının bir örneğidir
root.withdraw()

def goruntuBulma(dosyaYolu,arayuz):
    dosyaYolu.goruntuKonum = filedialog.askopenfilename()
    if (dosyaYolu.goruntuKonum != ""):
        print(dosyaYolu.goruntuKonum)
        goruntu = cv2.imread(dosyaYolu.goruntuKonum)
        goruntu = cv2.resize(goruntu, (561, 500))
        cv2.imwrite('GoruntuTespit/fotograf.jpg', goruntu)

        pix = pixDonustur(goruntu)
        arayuz.lbl_arayuz.setPixmap(pix)

def pixDonustur(goruntu):#label basma işleminde dönüştürme yapıyor.
    fotograf = QtGui.QImage(goruntu, goruntu.shape[1],goruntu.shape[0], goruntu.shape[1] * 3, QtGui.QImage.Format_RGB888)
    pix = QtGui.QPixmap(fotograf)
    return pix






