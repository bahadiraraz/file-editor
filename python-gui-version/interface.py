from PyQt5 import QtCore, QtGui, QtWidgets
import ctypes,time,random
### MADE BY BAHADIR54
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(628, 483)
        MainWindow.setStyleSheet(";\n"
"background-color: rgb(54, 54, 54);")
        MainWindow.setAnimated(True)
        MainWindow.setWindowIcon(QtGui.QIcon("python_1.ico"))


        self.b = f"QPushButton""{""border-radius : 50;""border : 2px solid black;""}""QPushButton::pressed""{""background-color : rgb(0, 0, 0) ;"f"color : rgb({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)});""}"

        self.a =( f"QPushButton""{"
	"border-style: solid;\n"
	"border-color: #050a0e;\n"
	"border-width: 1px;\n"
	"border-radius: 5px;\n"
	"color: rgb(255, 255, 255);\n"
	"padding: 2px;\n"
	"background-color: rgb(0, 0, 0);\n"
"}"
"QPushButton::default""{"
	"border-style: solid;\n"
	"border-color: #050a0e;\n"
	"border-width: 1px;\n"
	"border-radius: 5px;\n"
	"color: #FFFFFF;\n"
	"padding: 2px;\n"
	"background-color: #151a1e;\n"
"}"
"QPushButton:hover""{"
	"border-style: solid;\n"
    "border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #00FF00 stop:0.4 #00FF00 stop:0.5 #100E19, stop:1 #100E19);\n"
    "border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #00FF00 stop:1 #00FF00);\n"
    "border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #00FF00 stop:0.3 #00FF00 stop:0.7 #100E19, stop:1 #100E19);\n"
    "border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #00FF00 stop:0.3 #00FF00 stop:0.7 #100E19, stop:1 #100E19);\n"
	"border-width: 2px;\n"
    "border-radius: 1px;\n"
	"color: #d3dae3;\n"
	"padding: 2px;\n"
"}"
"QPushButton:pressed""{"
	"border-style: solid;\n"
    "border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #ff1100 stop:0.4 #ff1100 stop:0.5 #100E19, stop:1 #100E19);\n"
    "border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #ff1100 stop:1 #ff1100);\n"
    "border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ff1100 stop:0.3 #ff1100 stop:0.7 #100E19, stop:1 #100E19);\n"
    "border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #ff1100 stop:0.3 #ff1100 stop:0.7 #100E19, stop:1 #100E19);\n"
	"border-width: 2px;\n"
    "border-radius: 1px;\n"
	"color: #d3dae3;\n"
	"padding: 2px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("color: rgb(0, 0, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_pages = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(1)
        self.frame_pages.setFont(font)
        self.frame_pages.setToolTipDuration(-1)
        self.frame_pages.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));")
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frame_pages.setLineWidth(0)
        self.frame_pages.setObjectName("frame_pages")
        self.hboxlayout = QtWidgets.QHBoxLayout(self.frame_pages)
        self.hboxlayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.hboxlayout.setContentsMargins(2, 2, 2, 2)
        self.hboxlayout.setSpacing(0)
        self.hboxlayout.setObjectName("hboxlayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_pages)
        self.stackedWidget.setMinimumSize(QtCore.QSize(604, 459))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setToolTipDuration(-1)
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.ana_menu_sayfa = QtWidgets.QWidget()
        self.ana_menu_sayfa.setMinimumSize(QtCore.QSize(604, 459))
        self.ana_menu_sayfa.setMaximumSize(QtCore.QSize(999999, 999999))
        self.ana_menu_sayfa.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.ana_menu_sayfa.setObjectName("ana_menu_sayfa")
        self.menu_yazisi = QtWidgets.QLabel(self.ana_menu_sayfa)
        self.menu_yazisi.setGeometry(QtCore.QRect(260, 20, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(14)
        font.setItalic(True)
        self.menu_yazisi.setFont(font)
        self.menu_yazisi.setObjectName("menu_yazisi")
        self.dosya_islemleri_yazi = QtWidgets.QLabel(self.ana_menu_sayfa)
        self.dosya_islemleri_yazi.setGeometry(QtCore.QRect(80, 90, 71, 31))
        self.dosya_islemleri_yazi.setObjectName("dosya_islemleri_yazi")
        self.silme_islemleri_yazi = QtWidgets.QLabel(self.ana_menu_sayfa)
        self.silme_islemleri_yazi.setGeometry(QtCore.QRect(80, 130, 71, 21))
        self.silme_islemleri_yazi.setObjectName("silme_islemleri_yazi")
        self.dizin_degisme_yazi = QtWidgets.QLabel(self.ana_menu_sayfa)
        self.dizin_degisme_yazi.setGeometry(QtCore.QRect(80, 170, 71, 16))
        self.dizin_degisme_yazi.setObjectName("dizin_degisme_yazi")
        self.genel_ozellikler_yazi = QtWidgets.QLabel(self.ana_menu_sayfa)
        self.genel_ozellikler_yazi.setGeometry(QtCore.QRect(40, 330, 121, 21))
        self.genel_ozellikler_yazi.setObjectName("genel_ozellikler_yazi")
        self.dosya_islem_buton = QtWidgets.QPushButton(self.ana_menu_sayfa)
        self.dosya_islem_buton.setGeometry(QtCore.QRect(180, 100, 75, 23))
        self.dosya_islem_buton.setStyleSheet(self.a)
        self.dosya_islem_buton.setObjectName("dosya_islem_buton")
        self.silme_islem_buton = QtWidgets.QPushButton(self.ana_menu_sayfa)
        self.silme_islem_buton.setGeometry(QtCore.QRect(180, 130, 75, 23))
        self.silme_islem_buton.setStyleSheet(self.a)
        self.silme_islem_buton.setObjectName("silme_islem_buton")
        self.genel_ozellikler_yazma_yeri = QtWidgets.QLabel(self.ana_menu_sayfa)
        self.genel_ozellikler_yazma_yeri.setGeometry(QtCore.QRect(200, 300, 371, 121))
        self.genel_ozellikler_yazma_yeri.setText("")
        self.genel_ozellikler_yazma_yeri.setObjectName("genel_ozellikler_yazma_yeri")
        self.uyari = QtWidgets.QLabel(self.ana_menu_sayfa)
        self.uyari.setGeometry(QtCore.QRect(110, 220, 301, 61))
        self.uyari.setText("")
        self.uyari.setObjectName("uyari")
        self.dizin_degisme_buton = QtWidgets.QPushButton(self.ana_menu_sayfa)
        self.dizin_degisme_buton.setGeometry(QtCore.QRect(180, 170, 75, 23))
        self.dizin_degisme_buton.setStyleSheet(self.a)
        self.dizin_degisme_buton.setObjectName("dizin_degisme_buton")
        self.stackedWidget.addWidget(self.ana_menu_sayfa)
        self.dosya_menu = QtWidgets.QWidget()
        self.dosya_menu.setStyleSheet("background-color: rgb(106, 106, 106);\n"
"background-color: rgb(54, 54, 54);")
        self.dosya_menu.setObjectName("dosya_menu")
        self.dosya_acma_yazi = QtWidgets.QLabel(self.dosya_menu)
        self.dosya_acma_yazi.setGeometry(QtCore.QRect(60, 60, 131, 31))
        font = QtGui.QFont()
        self.dosya_acma_yazi.setFont(font)
        self.dosya_acma_yazi.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"border-radius: 6px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.dosya_acma_yazi.setObjectName("dosya_acma_yazi")
        self.dosya_menu_buton1 = QtWidgets.QPushButton(self.dosya_menu)
        self.dosya_menu_buton1.setGeometry(QtCore.QRect(210, 70, 75, 23))
        self.dosya_menu_buton1.setStyleSheet(self.a)
        self.dosya_menu_buton1.setObjectName("dosya_menu_buton1")
        self.dosya_menu_buton3 = QtWidgets.QPushButton(self.dosya_menu)
        self.dosya_menu_buton3.setGeometry(QtCore.QRect(210, 140, 75, 23))
        self.dosya_menu_buton3.setStyleSheet(self.a)
        self.dosya_menu_buton3.setObjectName("dosya_menu_buton3")
        self.sirali_dosya_acma_yazi = QtWidgets.QLabel(self.dosya_menu)
        self.sirali_dosya_acma_yazi.setGeometry(QtCore.QRect(60, 130, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.sirali_dosya_acma_yazi.setFont(font)
        self.sirali_dosya_acma_yazi.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"border-radius: 6px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.sirali_dosya_acma_yazi.setObjectName("sirali_dosya_acma_yazi")
        self.dosya_isim_degisme_yazi = QtWidgets.QLabel(self.dosya_menu)
        self.dosya_isim_degisme_yazi.setGeometry(QtCore.QRect(60, 210, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.dosya_isim_degisme_yazi.setFont(font)
        self.dosya_isim_degisme_yazi.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"border-radius: 6px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.dosya_isim_degisme_yazi.setObjectName("dosya_isim_degisme_yazi")
        self.dosya_menu_buton4 = QtWidgets.QPushButton(self.dosya_menu)
        self.dosya_menu_buton4.setGeometry(QtCore.QRect(210, 210, 75, 23))
        self.dosya_menu_buton4.setStyleSheet(self.a)
        self.dosya_menu_buton4.setObjectName("dosya_menu_buton4")
        self.tum_icerigi_goster_yazi = QtWidgets.QLabel(self.dosya_menu)
        self.tum_icerigi_goster_yazi.setGeometry(QtCore.QRect(60, 270, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tum_icerigi_goster_yazi.setFont(font)
        self.tum_icerigi_goster_yazi.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"border-radius: 6px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        font.setPointSize(8)
        self.tum_icerigi_goster_yazi.setObjectName("tum_icerigi_goster_yazi")
        self.dosya_menu_buton5 = QtWidgets.QPushButton(self.dosya_menu)
        self.dosya_menu_buton5.setGeometry(QtCore.QRect(210, 280, 75, 23))
        self.dosya_menu_buton5.setStyleSheet(self.a)
        self.dosya_menu_buton5.setObjectName("dosya_menu_buton5")
        self.sadece_dosya_yazi = QtWidgets.QLabel(self.dosya_menu)
        self.sadece_dosya_yazi.setGeometry(QtCore.QRect(60, 330, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.sadece_dosya_yazi.setFont(font)
        self.sadece_dosya_yazi.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"border-radius: 6px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.sadece_dosya_yazi.setObjectName("sadece_dosya_yazi")
        self.dosya_menu_buton6 = QtWidgets.QPushButton(self.dosya_menu)
        self.dosya_menu_buton6.setGeometry(QtCore.QRect(210, 340, 75, 23))
        self.dosya_menu_buton6.setStyleSheet(self.a)
        self.dosya_menu_buton6.setObjectName("dosya_menu_buton6")
        self.txt_yazi = QtWidgets.QLabel(self.dosya_menu)
        self.txt_yazi.setGeometry(QtCore.QRect(330, 70, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txt_yazi.setFont(font)
        self.txt_yazi.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"border-radius: 6px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.txt_yazi.setObjectName("txt_yazi")
        self.dosya_menu_buton7 = QtWidgets.QPushButton(self.dosya_menu)
        self.dosya_menu_buton7.setGeometry(QtCore.QRect(480, 70, 75, 23))
        self.dosya_menu_buton7.setStyleSheet(self.a)
        self.dosya_menu_buton7.setObjectName("dosya_menu_buton7")
        self.uzantili_dosya_bul_yazi = QtWidgets.QLabel(self.dosya_menu)
        self.uzantili_dosya_bul_yazi.setGeometry(QtCore.QRect(330, 140, 121, 31))
        self.uzantili_dosya_bul_yazi.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"border-radius: 6px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.uzantili_dosya_bul_yazi.setObjectName("uzantili_dosya_bul_yazi")
        self.ana_menu_buton_dosya = QtWidgets.QPushButton(self.dosya_menu)
        self.ana_menu_buton_dosya.setGeometry(QtCore.QRect(480, 390, 71, 21))
        self.ana_menu_buton_dosya.setStyleSheet(self.b)
        self.ana_menu_buton_dosya.setObjectName("ana_menu_buton_dosya")
        self.silme_islem_donus_dosya = QtWidgets.QPushButton(self.dosya_menu)
        self.silme_islem_donus_dosya.setGeometry(QtCore.QRect(360, 390, 81, 21))
        self.silme_islem_donus_dosya.setStyleSheet(self.b)
        self.silme_islem_donus_dosya.setObjectName("silme_islem_donus_dosya")
        self.dosya_menu_buton8 = QtWidgets.QPushButton(self.dosya_menu)
        self.dosya_menu_buton8.setGeometry(QtCore.QRect(480, 140, 75, 23))
        self.dosya_menu_buton8.setStyleSheet(self.a)
        self.dosya_menu_buton8.setObjectName("dosya_menu_buton8")
        self.stackedWidget.addWidget(self.dosya_menu)
        self.silme_menu = QtWidgets.QWidget()
        self.silme_menu.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.silme_menu.setObjectName("silme_menu")
        self.pushButton = QtWidgets.QPushButton(self.silme_menu)
        self.pushButton.setGeometry(QtCore.QRect(480, 390, 75, 23))
        self.pushButton.setStyleSheet(self.b)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.silme_menu)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 390, 75, 23))
        self.pushButton_2.setStyleSheet(self.b)
        self.pushButton_2.setObjectName("pushButton_2")
        self.yazi = QtWidgets.QLabel(self.silme_menu)
        self.yazi.setGeometry(QtCore.QRect(20, 20, 61, 16))
        self.yazi.setObjectName("yazi")
        self.yazi_2 = QtWidgets.QLabel(self.silme_menu)
        self.yazi_2.setGeometry(QtCore.QRect(20, 60, 91, 31))
        self.yazi_2.setObjectName("yazi_2")
        self.yazi_3 = QtWidgets.QLabel(self.silme_menu)
        self.yazi_3.setGeometry(QtCore.QRect(20, 130, 111, 21))
        self.yazi_3.setObjectName("yazi_3")
        self.full_temizle_buton = QtWidgets.QPushButton(self.silme_menu)
        self.full_temizle_buton.setGeometry(QtCore.QRect(150, 130, 75, 23))
        self.full_temizle_buton.setStyleSheet(self.a)
        self.full_temizle_buton.setObjectName("full_temizle_buton")
        self.silme_menu_yazi = QtWidgets.QLabel(self.silme_menu)
        self.silme_menu_yazi.setGeometry(QtCore.QRect(360, 30, 221, 41))
        self.silme_menu_yazi.setText("")
        self.silme_menu_yazi.setObjectName("silme_menu_yazi")
        self.dosya_silme_yazi = QtWidgets.QLineEdit(self.silme_menu)
        self.dosya_silme_yazi.setGeometry(QtCore.QRect(130, 20, 113, 20))
        self.dosya_silme_yazi.setObjectName("dosya_silme_yazi")
        self.dosya_silme_yazi.setStyleSheet("selection-background-color:#007b50;"
                                                   "background-color:#1e1d23;\n"
                                                   "border-style: solid;\n"
                                                   "border-top-color: transparent;\n"
                                                   "border-right-color: transparent;\n"
                                                   "border-left-color: transparent;\n"
                                                   "border-bottom-color: transparent;\n"
                                                   "border-width: 1px;\n"
                                                   "color: rgb(255, 255, 255);")
        self.dosya_silme_icerigiyazi = QtWidgets.QLineEdit(self.silme_menu)
        self.dosya_silme_icerigiyazi.setGeometry(QtCore.QRect(130, 70, 113, 20))
        self.dosya_silme_icerigiyazi.setObjectName("dosya_silme_icerigiyazi")
        self.dosya_silme_icerigiyazi.setStyleSheet("selection-background-color:#007b50;"
                                                     "background-color:#1e1d23;\n"
                                                     "border-style: solid;\n"
                                                     "border-top-color: transparent;\n"
                                                     "border-right-color: transparent;\n"
                                                     "border-left-color: transparent;\n"
                                                     "border-bottom-color: transparent;\n"
                                                     "border-width: 1px;\n"
                                                     "color: rgb(255, 255, 255);")
        self.dosya_sil_buton = QtWidgets.QPushButton(self.silme_menu)
        self.dosya_sil_buton.setGeometry(QtCore.QRect(250, 20, 75, 23))
        self.dosya_sil_buton.setStyleSheet(self.a)
        self.dosya_sil_buton.setObjectName("dosya_sil_buton")
        self.icerik_sil_buton = QtWidgets.QPushButton(self.silme_menu)
        self.icerik_sil_buton.setGeometry(QtCore.QRect(250, 70, 75, 23))
        self.icerik_sil_buton.setStyleSheet(self.a)
        self.icerik_sil_buton.setObjectName("icerik_sil_buton")
        self.silme_menu_liste = QtWidgets.QListWidget(self.silme_menu)
        self.silme_menu_liste.setGeometry(QtCore.QRect(10, 171, 241, 281))
        self.silme_menu_liste.setObjectName("silme_menu_liste")
        self.stackedWidget.addWidget(self.silme_menu)
        self.dizin_degisme_menu = QtWidgets.QWidget()
        self.dizin_degisme_menu.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.dizin_degisme_menu.setObjectName("dizin_degisme_menu")
        self.dizin_degis_tamam = QtWidgets.QPushButton(self.dizin_degisme_menu)
        self.dizin_degis_tamam.setGeometry(QtCore.QRect(500, 390, 75, 23))
        self.dizin_degis_tamam.setStyleSheet(self.b)
        self.dizin_degis_tamam.setObjectName("dizin_degis_tamam")
        self.dizin_gir_yazi = QtWidgets.QLabel(self.dizin_degisme_menu)
        self.dizin_gir_yazi.setGeometry(QtCore.QRect(70, 140, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dizin_gir_yazi.setFont(font)
        self.dizin_gir_yazi.setObjectName("dizin_gir_yazi")
        self.dizin_gir = QtWidgets.QLineEdit(self.dizin_degisme_menu)
        self.dizin_gir.setGeometry(QtCore.QRect(190, 140, 371, 31))
        self.dizin_gir.setStyleSheet("selection-background-color:#007b50;"
                                                     "background-color:#1e1d23;\n"
                                                     "border-style: solid;\n"
                                                     "border-top-color: transparent;\n"
                                                     "border-right-color: transparent;\n"
                                                     "border-left-color: transparent;\n"
                                                     "border-bottom-color: transparent;\n"
                                                     "border-width: 1px;\n"
                                                     "color: rgb(255, 255, 255);")

        font = QtGui.QFont()
        font.setPointSize(14)
        self.dizin_gir.setFont(font)
        self.dizin_gir.setStyleSheet(self.b)
        self.dizin_gir.setText("")
        self.dizin_gir.setObjectName("dizin_gir")
        self.dizin_uyari = QtWidgets.QLabel(self.dizin_degisme_menu)
        self.dizin_uyari.setGeometry(QtCore.QRect(120, 230, 281, 31))
        self.dizin_uyari.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"border-radius: 6px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.dizin_uyari.setText("")
        self.dizin_uyari.setObjectName("dizin_uyari")
        self.dizin_su_anki_dizin = QtWidgets.QLabel(self.dizin_degisme_menu)
        self.dizin_su_anki_dizin.setGeometry(QtCore.QRect(50, 50, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dizin_su_anki_dizin.setFont(font)
        self.dizin_su_anki_dizin.setText("")
        self.dizin_su_anki_dizin.setObjectName("dizin_su_anki_dizin")
        self.dizin_ana_menu = QtWidgets.QPushButton(self.dizin_degisme_menu)
        self.dizin_ana_menu.setGeometry(QtCore.QRect(10, 390, 75, 23))
        self.dizin_ana_menu.setStyleSheet(self.b)
        self.dizin_ana_menu.setObjectName("dizin_ana_menu")
        self.stackedWidget.addWidget(self.dizin_degisme_menu)
        self.dosya_acma_menu = QtWidgets.QWidget()
        self.dosya_acma_menu.setMouseTracking(False)
        self.dosya_acma_menu.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.dosya_acma_menu.setObjectName("dosya_acma_menu")
        self.dosya_acma_menu_dosya_adi = QtWidgets.QLineEdit(self.dosya_acma_menu)
        self.dosya_acma_menu_dosya_adi.setGeometry(QtCore.QRect(392, 40, 181, 20))
        self.dosya_acma_menu_dosya_adi.setObjectName("dosya_acma_menu_dosya_adi")
        self.dosya_acma_menu_dosya_adi.setStyleSheet("selection-background-color:#007b50;"
                                        "background-color:#1e1d23;\n"
                                        "border-style: solid;\n"
                                        "border-top-color: transparent;\n"
                                        "border-right-color: transparent;\n"
                                        "border-left-color: transparent;\n"
                                        "border-bottom-color: transparent;\n"
                                        "border-width: 1px;\n"
                                        "color: rgb(255, 255, 255);")
        self.geri_dosya_menu = QtWidgets.QPushButton(self.dosya_acma_menu)
        self.geri_dosya_menu.setGeometry(QtCore.QRect(490, 400, 75, 23))
        self.geri_dosya_menu.setStyleSheet(self.b)
        self.geri_dosya_menu.setObjectName("geri_dosya_menu")
        self.metin = QtWidgets.QLabel(self.dosya_acma_menu)
        self.metin.setGeometry(QtCore.QRect(220, 40, 161, 21))
        self.metin.setObjectName("metin")
        self.ana_menu = QtWidgets.QPushButton(self.dosya_acma_menu)
        self.ana_menu.setGeometry(QtCore.QRect(370, 400, 75, 23))
        self.ana_menu.setStyleSheet(self.b)
        self.ana_menu.setObjectName("ana_menu")
        self.pushButton_3 = QtWidgets.QPushButton(self.dosya_acma_menu)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 70, 71, 23))
        self.pushButton_3.setStyleSheet(self.a)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.dosya_acma_menu)
        self.label.setGeometry(QtCore.QRect(220, 310, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.dosya_acma_menu)
        self.listWidget.setGeometry(QtCore.QRect(15, 11, 201, 431))
        self.listWidget.setObjectName("listWidget")
        self.stackedWidget.addWidget(self.dosya_acma_menu)
        self.sirali_ac_menu = QtWidgets.QWidget()
        self.sirali_ac_menu.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.sirali_ac_menu.setObjectName("sirali_ac_menu")
        self.textEdit = QtWidgets.QTextEdit(self.sirali_ac_menu)
        self.textEdit.setGeometry(QtCore.QRect(460, 30, 131, 131))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setStyleSheet("selection-background-color:#007b50;"
	"background-color:#1e1d23;\n"
	"border-style: solid;\n"
	"border-top-color: transparent;\n"
	"border-right-color: transparent;\n"
	"border-left-color: transparent;\n"
	"border-bottom-color: transparent;\n"
	"border-width: 1px;\n"
	"color: #a9b7c6;")
        self.yazi_8 = QtWidgets.QLabel(self.sirali_ac_menu)
        self.yazi_8.setGeometry(QtCore.QRect(270, 30, 141, 31))
        self.yazi_8.setObjectName("yazi_8")
        self.sirali_ac_dosya_liste = QtWidgets.QListWidget(self.sirali_ac_menu)
        self.sirali_ac_dosya_liste.setGeometry(QtCore.QRect(10, 10, 201, 431))
        self.sirali_ac_dosya_liste.setObjectName("sirali_ac_dosya_liste")
        self.sirali_acma_buton = QtWidgets.QPushButton(self.sirali_ac_menu)
        self.sirali_acma_buton.setGeometry(QtCore.QRect(490, 180, 75, 23))
        self.sirali_acma_buton.setStyleSheet(self.a)
        self.sirali_acma_buton.setObjectName("sirali_acma_buton")
        self.git_ac_sayac = QtWidgets.QSpinBox(self.sirali_ac_menu)
        self.git_ac_sayac.setGeometry(QtCore.QRect(240, 140, 42, 22))
        self.git_ac_sayac.setObjectName("git_ac_sayac")
        self.git_acma_buton = QtWidgets.QPushButton(self.sirali_ac_menu)
        self.git_acma_buton.setGeometry(QtCore.QRect(320, 140, 75, 23))
        self.git_acma_buton.setStyleSheet(self.a)
        self.git_acma_buton.setObjectName("git_acma_buton")
        self.sirali_ac_menu__geri = QtWidgets.QPushButton(self.sirali_ac_menu)
        self.sirali_ac_menu__geri.setGeometry(QtCore.QRect(490, 400, 75, 23))
        self.sirali_ac_menu__geri.setStyleSheet(self.b)
        self.sirali_ac_menu__geri.setObjectName("sirali_ac_menu__geri")
        self.sirali_ac_menu_ana_menu = QtWidgets.QPushButton(self.sirali_ac_menu)
        self.sirali_ac_menu_ana_menu.setGeometry(QtCore.QRect(360, 400, 75, 23))
        self.sirali_ac_menu_ana_menu.setStyleSheet(self.b)
        self.sirali_ac_menu_ana_menu.setObjectName("sirali_ac_menu_ana_menu")
        self.sirali_ac_uyari = QtWidgets.QLabel(self.sirali_ac_menu)
        self.sirali_ac_uyari.setGeometry(QtCore.QRect(320, 270, 221, 16))
        self.sirali_ac_uyari.setObjectName("sirali_ac_uyari")
        self.stackedWidget.addWidget(self.sirali_ac_menu)
        self.sadece_dosyala_menu = QtWidgets.QWidget()
        self.sadece_dosyala_menu.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.sadece_dosyala_menu.setObjectName("sadece_dosyala_menu")
        self.tum_dosya_liste = QtWidgets.QListWidget(self.sadece_dosyala_menu)
        self.tum_dosya_liste.setGeometry(QtCore.QRect(10, 60, 211, 391))
        self.tum_dosya_liste.setObjectName("tum_dosya_liste")
        self.uzantili_dosya_liste = QtWidgets.QListWidget(self.sadece_dosyala_menu)
        self.uzantili_dosya_liste.setGeometry(QtCore.QRect(375, 240, 211, 161))
        self.uzantili_dosya_liste.setObjectName("uzantili_dosya_liste")
        self.yazi_5 = QtWidgets.QLabel(self.sadece_dosyala_menu)
        self.yazi_5.setGeometry(QtCore.QRect(40, 20, 131, 21))
        self.yazi_5.setObjectName("yazi_5")
        self.uzantili_dosya_yazi = QtWidgets.QLabel(self.sadece_dosyala_menu)
        self.uzantili_dosya_yazi.setGeometry(QtCore.QRect(390, 210, 151, 20))
        self.uzantili_dosya_yazi.setText("")
        self.uzantili_dosya_yazi.setObjectName("uzantili_dosya_yazi")
        self.uzanti_ara_buton = QtWidgets.QPushButton(self.sadece_dosyala_menu)
        self.uzanti_ara_buton.setGeometry(QtCore.QRect(460, 100, 75, 23))
        self.uzanti_ara_buton.setStyleSheet(self.a)
        self.uzanti_ara_buton.setObjectName("uzanti_ara_buton")
        self.uzanti_yazma = QtWidgets.QLineEdit(self.sadece_dosyala_menu)
        self.uzanti_yazma.setGeometry(QtCore.QRect(330, 100, 113, 20))
        self.uzanti_yazma.setObjectName("uzanti_yazma")
        self.uzanti_yazma.setStyleSheet("selection-background-color:#007b50;"
	"background-color:#1e1d23;\n"
	"border-style: solid;\n"
	"border-top-color: transparent;\n"
	"border-right-color: transparent;\n"
	"border-left-color: transparent;\n"
	"border-bottom-color: transparent;\n"
	"border-width: 1px;\n"
	"color: rgb(255, 255, 255);")
        self.yazi_6 = QtWidgets.QLabel(self.sadece_dosyala_menu)
        self.yazi_6.setGeometry(QtCore.QRect(240, 100, 71, 21))
        self.yazi_6.setObjectName("yazi_6")
        self.sadece_dosya_uyari = QtWidgets.QLabel(self.sadece_dosyala_menu)
        self.sadece_dosya_uyari.setGeometry(QtCore.QRect(250, 30, 321, 21))
        self.sadece_dosya_uyari.setText("")
        self.sadece_dosya_uyari.setObjectName("sadece_dosya_uyari")
        self.txt_olustur_yazma = QtWidgets.QLineEdit(self.sadece_dosyala_menu)
        self.txt_olustur_yazma.setGeometry(QtCore.QRect(330, 160, 113, 20))
        self.txt_olustur_yazma.setObjectName("txt_olustur_yazma")
        self.txt_olustur_yazma.setStyleSheet("selection-background-color:#007b50;"
                                                     "background-color:#1e1d23;\n"
                                                     "border-style: solid;\n"
                                                     "border-top-color: transparent;\n"
                                                     "border-right-color: transparent;\n"
                                                     "border-left-color: transparent;\n"
                                                     "border-bottom-color: transparent;\n"
                                                     "border-width: 1px;\n"
                                                     "color: rgb(255, 255, 255);")
        self.yazi_7 = QtWidgets.QLabel(self.sadece_dosyala_menu)
        self.yazi_7.setGeometry(QtCore.QRect(240, 160, 71, 16))
        self.yazi_7.setObjectName("yazi_7")
        self.txt_olustur_buton = QtWidgets.QPushButton(self.sadece_dosyala_menu)
        self.txt_olustur_buton.setGeometry(QtCore.QRect(460, 160, 75, 23))
        self.txt_olustur_buton.setStyleSheet(self.a)
        self.txt_olustur_buton.setObjectName("txt_olustur_buton")
        self.sadece_dosya_geri = QtWidgets.QPushButton(self.sadece_dosyala_menu)
        self.sadece_dosya_geri.setGeometry(QtCore.QRect(500, 420, 75, 23))
        self.sadece_dosya_geri.setStyleSheet(self.b)
        self.sadece_dosya_geri.setObjectName("sadece_dosya_geri")
        self.sadece_dosya_ana_menu = QtWidgets.QPushButton(self.sadece_dosyala_menu)
        self.sadece_dosya_ana_menu.setGeometry(QtCore.QRect(380, 420, 75, 23))
        self.sadece_dosya_ana_menu.setStyleSheet(self.b)
        self.sadece_dosya_ana_menu.setObjectName("sadece_dosya_ana_menu")
        self.stackedWidget.addWidget(self.sadece_dosyala_menu)
        self.tum_dosya_menu = QtWidgets.QWidget()
        self.tum_dosya_menu.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.tum_dosya_menu.setObjectName("tum_dosya_menu")
        self.tumdosyalar = QtWidgets.QListWidget(self.tum_dosya_menu)
        self.tumdosyalar.setGeometry(QtCore.QRect(5, 41, 591, 371))
        self.tumdosyalar.setObjectName("tumdosyalar")
        self.yazi_4 = QtWidgets.QLabel(self.tum_dosya_menu)
        self.yazi_4.setGeometry(QtCore.QRect(90, 10, 401, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.yazi_4.setFont(font)
        self.yazi_4.setObjectName("yazi_4")
        self.tum_dosyalar_geri_buton = QtWidgets.QPushButton(self.tum_dosya_menu)
        self.tum_dosyalar_geri_buton.setGeometry(QtCore.QRect(500, 430, 75, 23))
        self.tum_dosyalar_geri_buton.setStyleSheet(self.b)
        self.tum_dosyalar_geri_buton.setObjectName("tum_dosyalar_geri_buton")
        self.tum_dosyalar_ana_menu_buton = QtWidgets.QPushButton(self.tum_dosya_menu)
        self.tum_dosyalar_ana_menu_buton.setGeometry(QtCore.QRect(400, 430, 75, 23))
        self.tum_dosyalar_ana_menu_buton.setStyleSheet(self.b)
        self.tum_dosyalar_ana_menu_buton.setObjectName("tum_dosyalar_ana_menu_buton")
        self.stackedWidget.addWidget(self.tum_dosya_menu)
        self.hboxlayout.addWidget(self.stackedWidget)
        self.verticalLayout_2.addWidget(self.frame_pages)
        self.dizin_gir.update()
        MainWindow.setCentralWidget(self.centralwidget)

        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("bahadir")

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "file-editor"))

        self.menu_yazisi.setText(_translate("MainWindow", "menu"))
        self.dosya_islemleri_yazi.setText(_translate("MainWindow", "dosya islemleri:"))
        self.silme_islemleri_yazi.setText(_translate("MainWindow", "silme islemleri:"))
        self.dizin_degisme_yazi.setText(_translate("MainWindow", "dizin degisme:"))
        self.genel_ozellikler_yazi.setText(_translate("MainWindow", "genel ozellikler"))
        self.dosya_islem_buton.setText(_translate("MainWindow", "1"))
        self.silme_islem_buton.setText(_translate("MainWindow", "2"))
        self.dizin_degisme_buton.setText(_translate("MainWindow", "3"))
        self.dosya_acma_yazi.setText(_translate("MainWindow", "1.dosya acma"))
        self.dosya_menu_buton1.setText(_translate("MainWindow", "1"))
        self.dosya_menu_buton3.setText(_translate("MainWindow", "2"))
        self.sirali_dosya_acma_yazi.setText(_translate("MainWindow", "2.sirali dosya acma islemleri"))
        self.dosya_isim_degisme_yazi.setText(_translate("MainWindow", "3.dosya isim degisme"))
        self.dosya_menu_buton4.setText(_translate("MainWindow", "3"))
        self.tum_icerigi_goster_yazi.setText(_translate("MainWindow", "4.tum icerigi gorme"))
        self.dosya_menu_buton5.setText(_translate("MainWindow", "4"))
        self.sadece_dosya_yazi.setText(_translate("MainWindow", "5.sadece dosyalar"))
        self.dosya_menu_buton6.setText(_translate("MainWindow", "5"))
        self.txt_yazi.setText(_translate("MainWindow", "6.txt olustur"))
        self.dosya_menu_buton7.setText(_translate("MainWindow", "6"))
        self.uzantili_dosya_bul_yazi.setText(_translate("MainWindow", "7.uzantili dosya bul"))
        self.ana_menu_buton_dosya.setText(_translate("MainWindow", "ana_menu"))
        self.silme_islem_donus_dosya.setText(_translate("MainWindow", "silme_islemleri"))
        self.dosya_menu_buton8.setText(_translate("MainWindow", "7"))
        self.pushButton.setText(_translate("MainWindow", "ana_menu"))
        self.pushButton_2.setText(_translate("MainWindow", "dosya_menu"))
        self.yazi.setText(_translate("MainWindow", "dosya silme:"))
        self.yazi_2.setText(_translate("MainWindow", "dosya icerigi silme"))
        self.yazi_3.setText(_translate("MainWindow", "su anki klasoru temizle"))
        self.full_temizle_buton.setText(_translate("MainWindow", "temizle"))
        self.dosya_sil_buton.setText(_translate("MainWindow", "dosya_sil"))
        self.icerik_sil_buton.setText(_translate("MainWindow", "icerik sil"))
        self.dizin_degis_tamam.setText(_translate("MainWindow", "tamam"))
        self.dizin_gir_yazi.setText(_translate("MainWindow", "dizini girin:"))
        self.dizin_ana_menu.setText(_translate("MainWindow", "ana_menu"))
        self.geri_dosya_menu.setText(_translate("MainWindow", "geri"))
        self.metin.setText(_translate("MainWindow", "olusturmak istedigin dosya  adi:"))
        self.ana_menu.setText(_translate("MainWindow", "ana_menu"))
        self.pushButton_3.setText(_translate("MainWindow", "olustur"))
        self.yazi_8.setText(_translate("MainWindow", "sirali acma"))
        self.sirali_acma_buton.setText(_translate("MainWindow", "sirali"))
        self.git_acma_buton.setText(_translate("MainWindow", "git_acma"))
        self.sirali_ac_menu__geri.setText(_translate("MainWindow", "geri"))
        self.sirali_ac_menu_ana_menu.setText(_translate("MainWindow", "ana_menu"))
        self.sirali_ac_uyari.setText(_translate("MainWindow", ""))
        self.yazi_5.setText(_translate("MainWindow", "tum dosyalar"))
        self.uzanti_ara_buton.setText(_translate("MainWindow", "ara"))
        self.yazi_6.setText(_translate("MainWindow", "uzanti ara"))
        self.yazi_7.setText(_translate("MainWindow", "txt olustur"))
        self.txt_olustur_buton.setText(_translate("MainWindow", "olustur"))
        self.sadece_dosya_geri.setText(_translate("MainWindow", "geri"))
        self.sadece_dosya_ana_menu.setText(_translate("MainWindow", "ana_menu"))
        self.yazi_4.setText(_translate("MainWindow", "tum  dosyalar"))
        self.tum_dosyalar_geri_buton.setText(_translate("MainWindow", "geri"))
        self.tum_dosyalar_ana_menu_buton.setText(_translate("MainWindow", "ana_menu"))
