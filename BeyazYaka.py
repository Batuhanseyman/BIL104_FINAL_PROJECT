from Calisan import Calisan

class BeyazYaka (Calisan):

    #Class icin uygun parametreleri alan ve Calisan class'inda bulunan ozellikleri Calisan adli class'in init metoduna yollayan,
    #kendisine has özniteliklleri de gelen parametrelere esitleyen init metodu
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        Calisan.__init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi

    #11-16 satirlari arasinda BeyazYaka sinifina has olan ozellikler icin yazilmis accessor/mutator metotlar.
    def get_tesvik_primi (self):
        return self.__tesvik_primi
    
    def set_tesvik_primi (self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    #Beyaz yakalinin zam hakkini hesaplayip, tutar olarak return eden metot. 
    #Örneğin hesaplamalarin sonucu 1000 cikarsa 1000 tl zam hakki var demektir.
    def zam_hakki (self):
        zam_orani_onerisi = 0

        try:
            if self.get_tecrube() < 24:
                zam_orani_onerisi = self.__tesvik_primi

            elif self.get_tecrube() >= 24 and self.get_tecrube() <= 48 and self.get_maas() < 15000:
                zam_orani_onerisi = (self.get_maas()%self.get_tecrube())*5 + self.__tesvik_primi
            
            elif self.get_tecrube() > 48 and self.get_maas() < 25000:
                zam_orani_onerisi = (self.get_maas()%self.get_tecrube())*4 + self.__tesvik_primi
            
            return zam_orani_onerisi

        except Exception as err:
            print(err)

    #Zam hakki metodundan gelen zam tutarini kullanarak yeni maasi hesaplayan ve donduren metot.
    def yeni_maas (self):

        try:
            zamli_maas = self.get_maas() + self.zam_hakki()

            if zamli_maas == self.get_maas():
                self.maas_yeni = self.get_maas()
        
            else:
                self.maas_yeni = zamli_maas

            return self.maas_yeni

        except Exception as err:
            print(err)

    #istenen bilgileri ekrana yazdirmak icin string return eden str metodu.
    def __str__ (self):
        return f"Ad : {self.get_ad()}\t Soyad : {self.get_soyad()}\t Tecrube : {self.get_tecrube()//12} yil {self.get_tecrube()%12} ay\t Yeni Maasi : {self.yeni_maas()}"
    

