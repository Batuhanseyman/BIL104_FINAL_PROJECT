from Insan import Insan

class Calisan (Insan):
    #Yeni maasi tutan public class degiskeni. 
    #Bu public degisken Calisan sinifindan miras alan MaviYaka ve BeyazYaka siniflarinda da ayni amacla kullaniliyor.
    maas_yeni = 0

    #Class icin uygun parametreleri alan ve Insan class'inda bulunan ozellikleri Insan adli class'in init metoduna yollayan,
    #kendisine has özniteliklleri de gelen parametrelere esitleyen init metodu.Nesne icin girilen sektör, istenen sektör değilse 
    #geçerli bir sektör girilene kadar klavyeden veri girişi sağlanıyor.
    def __init__ (self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        Insan.__init__ (self, tc_no, ad, soyad, yas, cinsiyet, uyruk)
        
        self.__tecrube = tecrube
        self.__maas = maas
        
        try:
            while sektor not in ["teknoloji", "muhasebe", "inşaat", "diğer"]:
                sektor = input(f"{self.get_ad()} {self.get_soyad()} için girilen sektör geçersizdir.Lütfen şu sektörlerden birini giriniz : teknoloji, inşaat, muhasebe, diğer : ")
            
        except Exception as err:
            print(err)

        self.__sektor = sektor

    #23-40 satirlari arasinda Calisan sinifina has olan ozellikler icin yazilmis accessor/mutator metotlar.
    def get_sektor (self):
        return self.__sektor
    
    def set_sektor (self, sektor):
        self.__sektor = sektor

    def get_tecrube (self):
        return self.__tecrube
    
    def set_tecrube (self, tecrube):
        self.__tecrube = tecrube

    def get_maas (self):
        return self.__maas
    
    def set_maas (self, maas):
        self.__maas = maas

    #Calisanin zam hakki oranini hesaplayip degeri donduren metot.
    def zam_hakki (self):
        zam_orani_onerisi = 0
        
        try:
            if self.__tecrube < 24:
                zam_orani_onerisi = 0

            elif self.__tecrube >= 24 and self.__tecrube <= 48 and self.__maas < 15000:
                zam_orani_onerisi = self.__maas % self.__tecrube

            elif self.__tecrube > 48 and self.__maas < 25000:
                zam_orani_onerisi = (self.__maas % self.__tecrube)/2


            return zam_orani_onerisi
        
        except Exception as err:
            print(err)
    
    #Zam hakki metodundan gelen zam oranini yuzdesel olarak kullanip yeni maasi bulan metot.
    #Ornegin zam hakki metodundan 10 degeri geldiyse maasa %10 zam yapip yeni maasa atar. 
    def yeni_maas (self):
        try:
            zamli_maas = self.__maas + self.__maas * self.zam_hakki()/100

            if zamli_maas == self.__maas:
                self.maas_yeni = self.__maas
        
            else:
                self.maas_yeni = zamli_maas
            
            return self.maas_yeni
            
        except Exception as err:
            print(err)
            
    #istenen bilgileri ekrana yazdirmak icin string return eden str metodu.
    def __str__(self):
        return f"Ad : {self.get_ad()}\t Soyad : {self.get_soyad()}\t Tecrube : {self.__tecrube//12} yil {self.__tecrube%12} ay\t Yeni maasi : {self.yeni_maas()}"
      
