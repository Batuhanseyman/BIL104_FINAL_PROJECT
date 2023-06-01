from Calisan import Calisan

class MaviYaka (Calisan):

    #Class icin uygun parametreleri alan ve Calisan class'inda bulunan ozellikleri Calisan adli class'in init metoduna yollayan,
    #kendisine has özniteliklleri de gelen parametrelere esitleyen init metodu
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        Calisan.__init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__yipranma_payi = yipranma_payi

    #11-16 satirlari arasinda MaviYaka sinifina has olan ozellikler icin yazilmis accessor/mutator metotlar.
    def get_yipranma_payi (self):
        return self.__yipranma_payi
    
    def set_yipranma_payi (self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    #MaviYakali'nin  zam hakki oranini hesaplayip degeri donduren metot.
    def zam_hakki (self):
        zam_orani_onerisi = 0

        try:
            if self.get_tecrube() < 24:
                zam_orani_onerisi = self.__yipranma_payi*10

            elif self.get_tecrube() >= 24 and self.get_tecrube() <= 48 and self.get_maas() < 15000:
                zam_orani_onerisi = (self.get_maas()%self.get_tecrube())/2 + (self.__yipranma_payi*10)
            
            elif self.get_tecrube() > 48 and self.get_maas() < 25000:
                zam_orani_onerisi = (self.get_maas()%self.get_tecrube())/3 + (self.__yipranma_payi*10)
            
            return zam_orani_onerisi

        except Exception as err:
            print(err)  

    #Zam hakki metodundan gelen zam oranini yuzdesel olarak kullanip yeni maasi bulan metot.
    #Ornegin zam hakki metodundan 10 degeri geldiyse maasa %10 zam yapip yeni maasa atar. 
    def yeni_maas (self):
        try:
            zamli_maas = self.get_maas() + self.get_maas() * self.zam_hakki()/100

            if zamli_maas == self.get_maas():
                self.maas_yeni = self.get_maas()
                
            else:
                self.maas_yeni = zamli_maas

            return self.maas_yeni
            
        except Exception as err:
            print(err)

    #istenen bilgileri ekrana yazdirmak icin string return eden str metodu.       
    def __str__ (self):
        return (f"Ad : {self.get_ad()}\t Soyad : {self.get_soyad()}\t Tecrube : {self.get_tecrube()//12} yil {self.get_tecrube()%12} ay\t Yeni Maasi : {self.yeni_maas()}") 


