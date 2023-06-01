from Insan import Insan

class Issiz (Insan):

    #Issiz nesnesinin gecmis tecrubelerine bakilarak onerilen uygun statuyu tutan public class degiskeni.
    uygun_statu = ""

    #Class icin uygun parametreleri alan ve Insan class'inda bulunan ozellikleri Insan adli class'in init metoduna yollayan,
    #kendisine has özniteliklleri de gelen parametrelere esitleyen init metodu
    def __init__ (self, tc_no, ad, soyad, yas, cinsiyet, uyruk, oz_gecmis):
        Insan.__init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__oz_gecmis = oz_gecmis
        
    #14-19 satirlari arasi Issiz sinifina has olan ozellikler icin yazilmis accessor/mutator metotlar.
    def get_oz_gecmis (self):
        return self.__oz_gecmis
    
    def set_oz_gecmis (self, oz_gecmis):
        self.__oz_gecmis = oz_gecmis

    #Dictionary olarak yollanan mavi yaka, beyaz yaka, yonetici pozisyonlarina ait gecmis tecrubelerine gore 
    #Issiz nesnesinin  calismaya uygun oldugu statuyu bulan metot.Buldugu degeri uygun_statu public degiskenine atip bu degiskeni return ediyor.
    def statu_bul (self):
        try:
            my = self.__oz_gecmis["mavi yaka"]*20/100
            by = self.__oz_gecmis["beyaz yaka"]*35/100
            yn = self.__oz_gecmis["yonetici"]*45/100

            if my > by:
                if my > yn:
                    self.uygun_statu = "mavi yaka"
                else:
                    self.uygun_statu = "yonetici"
                    
            elif by > yn:
                self.uygun_statu ="beyaz yaka"

            else:
                self.uygun_statu = "yonetici"
        
            return self.uygun_statu
            
        except Exception as err:
            print(err)

    #istenen bilgileri ekrana yazdirmak icin string return eden str metodu.
    def __str__ (self):
        return f"Su anda issiz olan {self.get_ad()} {self.get_soyad()} adli kisinin calismaya uygun olduğu statu : {self.statu_bul()}"


    
