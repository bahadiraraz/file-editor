import sys,os,shutil,time
class konum():
    def __init__(self,path=rf"{os.getcwd()}",dosyaicerigi=os.listdir(rf"{os.getcwd()}")):
        self.path = path
        self.dosyaicerigi = dosyaicerigi

konum= konum()
class komut():
    konum.dosyaicerigi = os.listdir(konum.path)
    def create(self, a):
        konum.dosyaicerigi = os.listdir(konum.path)
        if os.path.exists(a):
            print("olusturmaya calistiginiz klasor  zaten var")
            pass
        else:
            print("dosya olusturuldu")
            os.makedirs(a)
            konum.dosyaicerigi = os.listdir(konum.path)



    def silme(self):
        try:
            self.icerikgoster()
            a = input("silmek istediginiz dosya adi:")
            def dene(a):
                shutil.rmtree(a)
                print("silme islemi basarili")
                konum.dosyaicerigi = os.listdir(konum.path)
            dene(a)
            return silme.asil()
        except FileNotFoundError:
            print("boyle bir klasor yok")
            return self.silme()



    def delete(self):
        try:
            self.icerikgoster()
            a = input("icerigini silmek istediginiz dosya adi")
            d = f"{konum.path}{a}"
            icerik = os.listdir(d)
            for file in icerik:
                os.rmdir(rf'{d}\{file}')
            konum.dosyaicerigi = os.listdir(konum.path)
        except FileNotFoundError:
            print("boyle bir klasor yok")
            return self.delete()



    def git_create(self):
        try:
            a = int(input("kac tane dosya olusturmak istiyorsunuz"))
            for i in range(1, a +1):
                os.makedirs(rf"{konum.path}\00{i}")
            konum.dosyaicerigi = os.listdir(konum.path)
        except  ValueError:
            print("sayi gir aqdum")
            return self.git_create()
        except FileExistsError:
            print("olusturmaya calistiginiz sayilarda dosya var")
            return self.git_create()

    def sirali_girme(self):
        try:
            a = int(input("kac tane dosya olusturmak istiyorsunuz"))
            for i in range(1, a + 1):
                v = input(rf"{i}'inci dosyanin adini giriniz")
                os.makedirs(rf"{konum.path}\{str(i).zfill(2)}-{v}")
            konum.dosyaicerigi = os.listdir(konum.path)

        except FileExistsError:
            print("olusturmaya calistiginiz dosya var")
            pass


    def dizin_degis(self):
        a = input("yeni dizin")
        konum.path = rf"{a}"
        konum.dosyaicerigi = os.listdir(rf"{a}")
        os.chdir(a)
    def ilk(self):
        try:
            a = input("path giriniz")
            konum.path = rf"{a}"
            konum.dosyaicerigi = os.listdir(rf"{a}")
            os.chdir(a)
        except:
            print("boyle bir path bulunamadi")
            return self.ilk()

    def icerikgoster(self):
        konum.dosyaicerigi = (os.listdir(konum.path))
        for i in (konum.dosyaicerigi): print(i)
    def full_temizle(self):
        konum.dosyaicerigi = os.listdir(konum.path)
        icerik = konum.dosyaicerigi
        for file in icerik:
            os.rmdir(rf'{konum.path}\{file}')
        konum.dosyaicerigi = os.listdir(konum.path)


    def tumicerik(self):
        for i, j, k in os.walk(konum.path):
            print("klasor yolu", i)
            print("klasor isimleri", j)
            print("dosya isimleri", k)
            print("----------------------")



    def isim_degis(self):
        try:
            komut.icerikgoster()
            a = input("ismini degismek isediginiz dosya adi:")
            b = input("ne yapacaksin:")
            def degis(a,b):

                os.rename(a, b)
                print("islem basarili")
            degis(a,b)
            return dosya.asil()
        except FileNotFoundError:
            print("boyle bir dosya yok")
            return komut.isim_degis()


    def dosyalar(self):
        sayi = 0
        print(f"su anki konum: {konum.path}")
        print("icindeki dosyalar:")
        for i, j, k in os.walk(konum.path):

            for t in k:
                sayi += 1
                print(t)
        if sayi == 0:
            print("dosya bulunamadi")



    def txt_olstur(self):
        a = input("txt isim")
        def basarisz(a):
            try:
                if rf"{a}.txt" not in konum.dosyaicerigi:
                    with open(rf"{a}.txt","a") as fp:
                        pass
                    print(rf"{a}.txt olusturuldu")
                else:
                    print("bu dosya zaten var")
            except FileExistsError:
                print("bu dosya zaten var")
                return
        basarisz(a)
        return



    def dosya_bul_uzanti(self):
        a = input("aradiginiz dosya uzantisi")
        for i, j, k in os.walk(konum.path):
            sayi =0
            for t in k:
                if t.endswith(rf"{a}"):
                    print(i,t,"-----------",sep="\n")
                    sayi +=1
        if sayi == 0:
            print(rf"bu klasorde {a} uzantili dosya bulunamadi")




    def dosya_ac(self):
        while True:
            try:
                komut.icerikgoster()
                b = input("olusturmak istediginiz klasor adini giriniz")

                komut.create(b)
                konum.dosyaicerigi.append(b)

                return dosya.asil()
            except FileExistsError:
                print("oldusturdugunuz dosya  zaten var")
                return self.dosya_ac()

    def __len__(self):
        return len((konum.dosyaicerigi))





komut = komut()
class dosya():
    def __init__(self):
        self.secenek = {
            "1": komut.dosya_ac,
            "2":komut.git_create,
            "3":komut.sirali_girme,
            "4":komut.isim_degis,
            "5":komut.tumicerik,
            "6":komut.dosyalar,
            "7":komut.txt_olstur,
            "8":komut.dosya_bul_uzanti,
            "q": self.quit
        }

    def menu_goster(self):
            print(f"""
{konum.path}
menu
1.dosya acma
2.git acma
3.sirali dosya acma
4.isim degisme
5.tum icerik
6.sadece dosyalar
7.txt dosyasi olustur
8.uzantili dosya bul
ana menuye donmek icin q 
    """)


    def asil(self):

        while True:
            self.menu_goster()
            secenek = input("secenegini giriniz : ")
            dogrulama = self.secenek.get(secenek)
            if dogrulama:
                dogrulama()
            else:
                print(f"{secenek} yanlis bir islem")
    def quit(self):
        return Menu().asil()
dosya = dosya()
class silme():
    konum.dosyaicerigi = os.listdir(konum.path)
    def __init__(self):
        self.secenek = {
            "1": komut.silme,
            "2": komut.delete,
            "3": komut.full_temizle,
            "q": self.quit
        }

    def menu_goster(self):
        print("""
menu
1.dosya silme
2.dosya icerik silme
3.su anki klasoru temizleme
q.ana menuye donme 
        """)

    def asil(self):

        while True:
            self.menu_goster()
            secenek = input("secenegini giriniz : ")
            dogrulama = self.secenek.get(secenek)
            if dogrulama:
                dogrulama()
            else:
                print(f"{secenek} yanlis bir islem")

    def quit(self):
        return Menu().asil()
silme = silme()
class Menu:
    try:

        def __init__(self):

            self.secenek = {
                    "1":dosya.asil,
                    "2":silme.asil,
                    "3":komut.dizin_degis,
                    "4":lambda: print(Menu.__str__(self)),
                    "q":self.quit
                    }


        def menu_goster(self,):
            print("""
menu
1.dosya islemleri
2.silme islemleri
3.dizin degis
4.genel ozelliklleri
cikmak icin q ya basin
    """)

        def asil(self):

            while True:
                self.menu_goster()
                secenek = input("secenegini giriniz : ")
                dogrulama = self.secenek.get(secenek)
                if dogrulama:
                    dogrulama()
                else:
                    print(rf"{secenek} yanlis bir islem")




        def quit(self):
            print("gorusuruz")
            sys.exit(0)

        def __str__(self):
            liste = ["\nklasor konumu: " + konum.path]
            if konum.dosyaicerigi == list():
                liste.append("dosya bulunamadi")
            else:
                liste.append("dosyanin icindekiler: " + " ".join(map(str, konum.dosyaicerigi)))
                liste.append("ozellikleri: " + " ".join(map(str, os.stat(konum.path))))
            return "\n".join(liste)
    except FileNotFoundError:
        print("boye bir path yok")




if __name__ == "__main__":
    print("programa hos geldin")
    komut.ilk()
    Menu().asil()