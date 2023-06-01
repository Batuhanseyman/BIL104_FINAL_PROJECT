from Insan import Insan as In
from Issiz import Issiz as Iz
from Calisan import Calisan as Cn
from MaviYaka import MaviYaka as MY
from BeyazYaka import BeyazYaka as BY
import pandas as pd 

def main ():
    #Insan sinifindan uretilen nesneler
    human1 = In (12345678910, "Ahmet", "Taş", 62, "Erkek", "Türk")
    human2 = In (32541541111, "John", "Marston", 32, "Erkek", "Amerikan")

    #Issiz sinifindan uretilen nesneler
    issiz1 = Iz (54321012345, "Veli", "Deli", 32, "Erkek", "Türk", oz_gecmis = {"mavi yaka": 10, "beyaz yaka": 2, "yonetici" : 0})
    issiz2 = Iz (78456324781, "Halis", "Çelik", 45, "Erkek", "Türk", oz_gecmis = {"mavi yaka": 0, "beyaz yaka": 24, "yonetici" : 0})
    issiz3 = Iz (45464978453, "Nur", "Gül", 48, "Kadin", "Türk", oz_gecmis = {"mavi yaka": 3, "beyaz yaka": 14, "yonetici" : 10})

    #Calisan sinifindan uretilen nesneler
    cn1 = Cn (65432178901, "Arthur", "Morgan", 43, "Erkek", "Amerikan", "diğer", 241, 21540)
    cn2 = Cn (29346708006, "Ayşe", "Nur", 28, "Kadin", "Türk", "muhasebe", 39, 14782)
    cn3 = Cn (55521343154, "Ömer", "Faruk", 22, "Erkek", "Türk", "teknoloji", 21, 13600)

    #MaviYaka sinifindan uretilen nesneler
    my1 = MY (47822219821, "Murat", "Sert", 21, "Erkek", "Türk", "teknoloji", 21, 8500, 0.2)
    my2 = MY (23213123159, "İpek", "Can", 21, "Kadin", "Türk", "diğer", 42, 10000, 0.5)
    my3 = MY (34654062423, "Ali", "Dayi", 54, "Erkek", "Türk", "inşaat", 298, 23465, 0.5)

    #BeyazYaka sinifindan uretilen nesneler
    by1 = BY (26586584566, "Batuhan", "Seyman", 26, "Erkek", "Türk", "teknoloji", 21, 16750, 2500)
    by2 = BY (64625347631, "Mehmet", "Karagöz", 31, "Erkek", "Türk", "muhasebe", 42, 14000, 2500)
    by3 = BY (87056856569, "Gwen", "Stacy", 41, "Kadin", "Ingiliz", "teknoloji", 195, 29546, 2500)

    #Olusturulan nesneleri str metotlari ile yazdiriyoruz.
    print("Nesneler")
    print("------------------------------------------------------")
    print ("1. insan Nesnesi\n", human1)
    print ("\n2. insan Nesnesi\n", human2)
    print ("\n1. issiz nesnesi\n", issiz1)
    print ("\n2. issiz nesnesi\n", issiz2)
    print ("\n3. issiz nesnesi\n", issiz3)
    print ("\n1. calisan nesnesi\n", cn1)
    print ("\n2. calisan nesnesi\n", cn2)
    print ("\n3. calisan nesnesi\n", cn3)
    print ("\n1. mavi yaka nesnesi\n",my1)
    print ("\n2. mavi yaka nesnesi\n",my2)
    print ("\n3. mavi yaka nesnesi\n",my3)
    print ("\n1. beyaz yaka nesnesi\n",by1)
    print ("\n2. beyaz yaka nesnesi\n",by2)
    print ("\n3. beyaz yaka nesnesi\n",by3)
    print("------------------------------------------------------\n\n\n")
    
    #Data Frame nesnesini olusturmak icin kullanacagim degerleri tutan data isimli dictionary.
    data = {"Calisan Tipi": ["Calisan", "Mavi yaka", "Beyaz yaka", "Calisan", "Calisan", "Mavi yaka", "Beyaz yaka", "Mavi yaka", "Beyaz yaka"], 
            "Tc no": [cn1.get_tc_no(), my1.get_tc_no(), by1.get_tc_no(), cn2.get_tc_no(), cn3.get_tc_no(), 
                      my2.get_tc_no(), by2.get_tc_no(), my3.get_tc_no(), by3.get_tc_no()], 

            "Ad":[cn1.get_ad(), my1.get_ad(), by1.get_ad(), cn2.get_ad(), cn3.get_ad(), 
                  my2.get_ad(), by2.get_ad(), my3.get_ad(), by3.get_ad()], 

            "Soyad":[cn1.get_soyad(), my1.get_soyad(), by1.get_soyad(), cn2.get_soyad(), 
                     cn3.get_soyad(), my2.get_soyad(), by2.get_soyad(), my3.get_soyad(), by3.get_soyad()], 

            "Yas":[cn1.get_yas(), my1.get_yas(), by1.get_yas(), cn2.get_yas(), cn3.get_yas(), 
                   my2.get_yas(), by2.get_yas(), my3.get_yas(), by3.get_yas()], 

            "Cinsiyet":[cn1.get_cinsiyet(),my1.get_cinsiyet(),by1.get_cinsiyet(),cn2.get_cinsiyet(),
                        cn3.get_cinsiyet(),my2.get_cinsiyet(),by2.get_cinsiyet(),my3.get_cinsiyet(), by3.get_cinsiyet()],

            "Uyruk":[cn1.get_uyruk(), my1.get_uyruk(), by1.get_uyruk(), cn2.get_uyruk(), cn3.get_uyruk(), 
                     my2.get_uyruk(), by2.get_uyruk(),my3.get_uyruk(), by3.get_uyruk()], 

            "Sektor":[cn1.get_sektor(), my1.get_sektor(), by1.get_sektor(), cn2.get_sektor(), cn3.get_sektor(), 
                      my2.get_sektor(), by2.get_sektor(),my3.get_sektor(), by3.get_sektor()], 

            "Tecrube(yil)":[float(f"{cn1.get_tecrube()/12:.2f}"), 
                            float(f"{my1.get_tecrube()/12:.2f}"), 
                            float(f"{by1.get_tecrube()/12:.2f}"),
                            float(f"{cn2.get_tecrube()/12:.2f}"),
                            float(f"{cn3.get_tecrube()/12:.2f}"),
                            float(f"{my2.get_tecrube()/12:.2f}"),
                            float(f"{by2.get_tecrube()/12:.2f}"),
                            float(f"{my3.get_tecrube()/12:.2f}"),
                            float(f"{by3.get_tecrube()/12:.2f}")], 
            "Maas":[cn1.get_maas(), my1.get_maas(), by1.get_maas(), cn2.get_maas(), cn3.get_maas(), my2.get_maas(), 
                    by2.get_maas(), my3.get_maas(), by3.get_maas()], 

            "Yipranma Payi":[None, my1.get_yipranma_payi(), None, None, None, my2.get_yipranma_payi(), None, 
                             my3.get_yipranma_payi(), None], 

            "Tesvik Primi":[None, None, by1.get_tesvik_primi(), None, None, None, by2.get_tesvik_primi(), None, by3.get_tesvik_primi()],

            "Yeni Maas":[cn1.yeni_maas(), my1.yeni_maas(), by1.yeni_maas(), cn2.yeni_maas(), cn3.yeni_maas(), my2.yeni_maas(), 
                         by2.yeni_maas(), my3.yeni_maas(), by3.yeni_maas()]}

    #Dictionaryden uretilen data frame nesnesi.
    df_first = pd.DataFrame (data)
    print("ilk oluşturulan ve üzerinde herhangi bir işlem uygulanmamis data frame")
    print(df_first, "\n\n")

    #Data frame nesnesinde NaN olan degerlere 0 atama islemi.
    df = df_first.fillna(0)
    print("Bos olan nesne degerlerine sifir atama isleminden sonra data frame")
    print(df, "\n\n")

    #Calisan, mavi yaka ve beyaz yaka icin groupby metoduyla 
    #gruplandirilarak tecrübe ve yeni maaş ortalamalarinin hesaplanip, data frame olarak yazdirilmasi
    df_sub = df.groupby (["Calisan Tipi"]) [["Tecrube(yil)","Yeni Maas"]].mean()
    print("Calisan, mavi yaka ve beyaz yaka icin gruplandirilarak tecrübe ve yeni maaş ortalamalarinin hesaplanmasi")
    print(df_sub, "\n\n")
  
    #Maasi 15.000 tl üzerinde olanlarin toplam sayisinin ekrana yazdirilmasi
    print("Maasi 15.000 tl uzerinde olanlarin sayisi = ", end = "")
    print (len(df [ df ["Maas"] > 15000 ]), "\n\n")

    #Data frame'i yeni maasa gore kucukten buyuge gore siralayip ekrana yazdirma islemi
    print("Yeni maasa gore kucukten buyuge siralama islemi")
    df_sorted = df.sort_values (by = "Yeni Maas")
    print(df_sorted, "\n\n")
    
    #Beyaz yakalilardan yeni bir data frame olusturulup, bu data framede tecrubesi 3 yildan buyuk olanlarin ekrana yazdirilmasi
    print("Tecrubesi 3 yildan fazla olan beyaz yakalilar")
    df_sub = df [ df["Calisan Tipi"] == "Beyaz yaka"] 
    print (df_sub [ df_sub ["Tecrube(yil)"] > 3], "\n\n")

    #Tecrubesi 10.000 tl uzerinde olanlarin loc methoduyla 2-5 satir arasi olanlarin tc ve yenimaas sutunlari kullanılarak 
    #yeni bir data framede gosterilmesi
    print(" Yeni maasi 10000 TL üzerinde olanlar için; 2-5 satir arasi olanlarin, tc_no ve yeni_maaş  sütunlarinin secilerek gosterilmesi")
    df_sub = df [ df["Yeni Maas"] > 10000]
    print(df_sub.loc[1:4, ["Tc no", "Yeni Maas"]], "\n\n")

    #ad, soyad, sektor ve yeni maas sutunlarini iceren yeni bir data frame el edip ekrana yazdirilmasi
    print("Var olan DataFrame'den ad, soyad, sektör ve yeni maasi iceren yeni bir DataFrame elde edilmesi.")
    df_sub = df [["Ad", "Soyad", "Sektor", "Yeni Maas"]]
    print(df_sub)



if __name__ == "__main__":
    main()