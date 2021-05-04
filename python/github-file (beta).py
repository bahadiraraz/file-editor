import sys,os,shutil
class konum():
    def __init__(self,path=r"C:\Users\b123q\OneDrive\Masaüstü\testbu",dosyaicerigi=os.listdir(r"C:\Users\b123q\OneDrive\Masaüstü\testbu")):
        self.path = path
        self.dosyaicerigi = dosyaicerigi
        os.chdir(path)
konum= konum()
class komut():

    def create(self, a):
        if os.path.exists(a):
            print("olusturmaya calistiginiz klasor  zaten var")
            pass
        else:
            print("dosya olusturuldu")
            os.makedirs(a)



    def silme(self):
        try:
            self.icerikgoster()
            a = input("silmek istediginiz dosya adi:")
            def dene(a):
                shutil.rmtree(a)
                print("silme islemi basarili")
                konum.dosyaicerigi.remove(a)
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

        except FileNotFoundError:
            print("boyle bir klasor yok")
            return self.delete()



    def git_create(self):
        try:
            a = int(input("kac tane dosya olusturmak istiyorsunuz"))
            for i in range(1, a +1):
                os.makedirs(rf"{konum.path}\00{i}")
        except  ValueError:
            print("sayi gir aqdum")
            return self.git_create()
        except FileExistsError:
            print("olusturmaya calistiginiz sayilarda dosya var")
            return self.git_create()



    def dizin_degis(self):
        a = input("yeni dizin")
        konum.path = rf"{a}"
        konum.dosyaicerigi = os.listdir(rf"{a}")



    def icerikgoster(self):
        for i in konum.dosyaicerigi: print(i)



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
            "3":komut.isim_degis,
            "4":komut.tumicerik,
            "5":komut.dosyalar,
            "6":komut.txt_olstur,
            "7":komut.dosya_bul_uzanti,
            "q": self.quit
        }

    def menu_goster(self):
            print(f"""
{konum.path}
menu
1.dosya acma
2.git acma
3.isim degisme
4.tum icerik
5.sadece dosyalar
6.txt dosyasi olustur
7.uzantili dosya bul
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
    def __init__(self):
        self.secenek = {
            "1": komut.silme,
            "2": komut.delete,
            "q": self.quit
        }

    def menu_goster(self):
        print("""
menu
1.dosya silme
2.dosya icerik silme
3.ana menuye donme 
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
    def degis(a=r"C:\Users\b123q\OneDrive\Masaüstü\testbu"):
        b = input("pathi girin:")
        if b == "":
            konum.path = a
            konum.dosyaicerigi = a
        else:
            konum.path = b
            konum.dosyaicerigi = b


    degis()
    Menu().asil()