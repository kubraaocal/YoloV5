from PyQt5 import QtWidgets
import sys

from DosyaYoluClass import dosyaYoluClass
from GoruntuBulma import goruntuBulma
from AraYuz import AraYuz
from GoruntuTespit import goruntuTespitiniBaslat

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    degiskenler = dosyaYoluClass()
    arayuz = AraYuz()

    arayuz.btn_goruntu.clicked.connect(lambda: goruntuBulma(degiskenler, arayuz))
    arayuz.btn_tespiteBasla.clicked.connect(lambda: goruntuTespitiniBaslat(arayuz))

    sys.exit(app.exec_())

