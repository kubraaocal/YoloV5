from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *

class AraYuz(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()#bu classa işaret ediyor.
        self.resize(900, 800)#windows ekran boyutu
        self.setStyleSheet(open("still.qss", "r").read())#araştır
        ##########
        self.lbl_Arayuz = QtWidgets.QLabel(self)#Görüntü İşleme başlığını ekliyor label olarak
        self.lbl_Arayuz.setGeometry(0,0,900,800)#windowsu kaplayan arka planımızı setliyor.
        ##########
        self.btn_goruntu = QtWidgets.QPushButton(self)
        self.btn_goruntu.setGeometry(QtCore.QRect(10, 10, 100, 50))
        self.btn_goruntu.setIconSize(QSize(30,30))
        ##########
        self.btn_tespiteBasla = QtWidgets.QPushButton(self)
        self.btn_tespiteBasla.setGeometry(QtCore.QRect(150, 10, 100, 50))
        ##########
        self.lbl_arayuz = QtWidgets.QLabel(self)
        self.lbl_arayuz.setGeometry(QtCore.QRect(270, 10, 561, 500))
        self.lbl_arayuz.setStyleSheet("background:white;")#görüntünün seçildikten sonra geldiği alan
        self.show()
        self.araYuzOlustur()#projeye ekleme fonksiyounu çağırdık.
        QtCore.QMetaObject.connectSlotsByName(self)

    def araYuzOlustur(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Görüntü İşleme"))
        self.btn_goruntu.setText(_translate("self", " Görüntü Seç "))
        self.btn_tespiteBasla.setText(_translate("self", "Tanımaya Başla!"))


