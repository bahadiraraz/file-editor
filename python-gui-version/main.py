import sys
### MADE BY BAHADIR54
from PyQt5.QtWidgets import QApplication,QMainWindow

from interface import Ui_MainWindow
import functions


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.liste = list()
        self.ui.dosya_islem_buton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dosya_menu))
        self.ui.silme_islem_buton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.silme_menu))
        self.ui.silme_islem_donus_dosya.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.silme_menu))
        self.ui.pushButton.clicked.connect(lambda :self.ui.stackedWidget.setCurrentWidget(self.ui.ana_menu_sayfa))
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dosya_menu))
        self.ui.dizin_degisme_buton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dizin_degisme_menu))
        self.ui.ana_menu_buton_dosya.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ana_menu_sayfa))
        self.ui.dizin_ana_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ana_menu_sayfa))
        self.ui.dosya_menu_buton1.clicked.connect(lambda :self.ui.stackedWidget.setCurrentWidget(self.ui.dosya_acma_menu))
        self.ui.ana_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ana_menu_sayfa))
        self.ui.geri_dosya_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dosya_menu))
        self.ui.dosya_menu_buton3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.sirali_ac_menu))
        self.ui.sirali_ac_menu__geri.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dosya_menu))
        self.ui.sirali_ac_menu_ana_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ana_menu_sayfa))
        self.ui.dosya_menu_buton5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.tum_dosya_menu))
        self.ui.tum_dosyalar_ana_menu_buton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ana_menu_sayfa))
        self.ui.tum_dosyalar_geri_buton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dosya_menu))
        self.ui.dosya_menu_buton6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.sirali_ac_menu))
        self.ui.sirali_ac_menu_ana_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ana_menu_sayfa))
        self.ui.sirali_ac_menu__geri.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dosya_menu))
        self.ui.dosya_menu_buton7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.sadece_dosyala_menu))
        self.ui.dosya_menu_buton8.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.sadece_dosyala_menu))
        self.ui.sadece_dosya_ana_menu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ana_menu_sayfa))
        self.ui.sadece_dosya_geri.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dosya_menu))
        self.ui.dosya_sil_buton.clicked.connect(self.sadece)
        self.ui.full_temizle_buton.clicked.connect(self.temizle)
        self.ui.sirali_acma_buton.clicked.connect(self.sirali)
        self.ui.git_acma_buton.clicked.connect(self.git)
        self.ui.uzanti_ara_buton.clicked.connect(self.uzanti)
        self.ui.pushButton_3.clicked.connect(self.dosya_ekle)
        self.ui.dizin_degis_tamam.clicked.connect(self.degis)
        self.ui.txt_olustur_buton.clicked.connect(self.txt)
        self.genel()
        self.ekle()
        self.show()
        self.tum()
    def txt(self):

        functions.komut.txt_olstur(self.ui.txt_olustur_yazma.text())
        self.ekle()
        self.ui.txt_olustur_yazma.clear()
    def uzanti(self):
        self.ui.uzantili_dosya_liste.clear()
        a=functions.komut.dosya_bul_uzanti(self.ui.uzanti_yazma.text())
        for i in a :
            self.ui.uzantili_dosya_liste.addItem(i)
        self.ui.uzanti_yazma.clear()
    def sadece(self):
        functions.komut.silme(self.ui.dosya_silme_yazi.text())
        self.ui.dosya_silme_yazi.clear()
        self.genel()
        self.ekle()
        self.show()
        self.tum()

    def temizle(self):
        functions.komut.full_temizle()
        self.ekle()
        self.genel()
        self.tum()
    def tum(self):
        self.ui.tumdosyalar.clear()
        for i in functions.komut.tumicerik():
            self.ui.tumdosyalar.addItem(i)

    def ekle(self):
        self.liste.clear()
        self.ui.tum_dosya_liste.clear()
        self.ui.listWidget.clear()
        self.ui.silme_menu_liste.clear()
        self.ui.sirali_ac_dosya_liste.clear()
        for i in functions.komut.icerikgoster():
            self.ui.listWidget.addItem(i)
            self.ui.sirali_ac_dosya_liste.addItem(i)
            self.ui.silme_menu_liste.addItem(i)
            self.liste.append(i)
        for j in functions.komut.dosyalar():
            self.ui.tum_dosya_liste.addItem(j)



    def degis(self):
        functions.komut.dizin_degis(self.ui.dizin_gir.text())
        self.ekle()
        self.genel()
        self.tum()
        print(functions.konum.path)
        print(functions.konum.dosyaicerigi)
    def git(self):
        a=int(self.ui.git_ac_sayac.text())
        functions.komut.git_create(a)
        self.ui.git_ac_sayac.clear()
        self.ekle()
        self.tum()

        self.ui.dizin_gir.clear()
    def sirali(self):
        a = (self.ui.textEdit.toPlainText()).split("\n")
        functions.komut.sirali_girme(a)
        self.ui.textEdit.clear()
        self.ekle()
        self.tum()




    def genel(self):
        self.ui.genel_ozellikler_yazma_yeri.setText(functions.Menu.__str__(self))

    def dosya_ekle(self):
        a=functions.komut.create(self.ui.dosya_acma_menu_dosya_adi.text())


        print(self.liste)
        if len(self.ui.dosya_acma_menu_dosya_adi.text())== 0:
            self.ui.label.setText("dosya ismi giriniz")
        elif self.ui.dosya_acma_menu_dosya_adi.text() not  in self.liste:
            self.ui.label.setText("dosya olusturuldu")
            self.ekle()
            self.tum()
            self.ui.dosya_acma_menu_dosya_adi.clear()
        elif self.ui.dosya_acma_menu_dosya_adi.text() in self.liste:
            self.ui.label.setText("olusturmaya calistginiz dosya zaten var")
            self.ui.dosya_acma_menu_dosya_adi.clear()






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
