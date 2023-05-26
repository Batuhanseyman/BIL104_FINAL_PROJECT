class Insan:

    #Nesnenin özelliklerini gönderilen parametrelere eşitleyip nesneyi başlatan init metodu
    def __init__ (self, tc_no, ad, soyad, yas, cinsiyet, uyruk):
        self.__tc_no = tc_no
        self.__ad = ad
        self.__soyad = soyad
        self.__yas = yas
        self.__cinsiyet = cinsiyet
        self.__uyruk = uyruk

    #11-46 satırları arasında attributelar için yazılmış olan mutator ve accessor metotlar bulunmaktadır. 
    def get_tc_no (self):
        return self.__tc_no
    
    def set_tc_no (self, tc_no):
        self.__tc_no = tc_no

    def get_ad (self):
        return self.__ad
    
    def set_ad (self, ad):
        self.__ad = ad

    def get_soyad (self):
        return self.__soyad
    
    def set_soyad (self, soyad):
        self.__soyad = soyad

    def get_yas (self):
        return self.__yas
    
    def set_yas (self, yas):
        self.__yas = yas

    def get_cinsiyet (self):
        return self.__cinsiyet
    
    def set_cinsiyet (self, cinsiyet):
        self.__cinsiyet = cinsiyet

    def get_uyruk (self):
        return self.__uyruk
    
    def set_uyruk (self, uyruk):
        self.__uyruk = uyruk

    #Nesnenin attributelarını ekrana yazdırmak üzere return eden str metodu
    def __str__(self):
        return f"Tc No : {self.__tc_no}\t Ad : {self.__ad}\t Soyad : {self.__soyad}\t   Yas : {self.__yas}\t Cinsiyet : {self.__cinsiyet}\t Uyruk : {self.__uyruk}"
