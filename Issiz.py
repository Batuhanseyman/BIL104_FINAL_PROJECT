from Insan import Insan

class Issiz (Insan):

    uygun_statu = ""

    def __init__ (self, tc_no, ad, soyad, yas, cinsiyet, uyruk, oz_gecmis):
        Insan.__init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__oz_gecmis = oz_gecmis

    def get_oz_gecmis (self):
        return self.__oz_gecmis
    
    def set_oz_gecmis (self, oz_gecmis):
        self.__oz_gecmis = oz_gecmis

    def statu_bul (self):
        try:
            my = self.__oz_gecmis["mavi yaka"]*20/100
            by = self.__oz_gecmis["beyaz yaka"]*35/100
            yn = self.__oz_gecmis["yonetici"]*45/100

            if my > by:
                if my > yn:
                    Issiz.uygun_statu = "mavi yaka"
                else:
                    Issiz.uygun_statu = "yonetici"
            elif by > yn:
                Issiz.uygun_statu ="beyaz yaka"

            else:
                Issiz.uygun_statu = "yonetici"
        
            return Issiz.uygun_statu
            
        except Exception as err:
            print(err)

    def __str__ (self):
        return f"Su anda issiz olan {self.get_ad()} {self.get_soyad()} adli kisinin calismaya uygun olduğu statu : {self.statu_bul()}"


    
