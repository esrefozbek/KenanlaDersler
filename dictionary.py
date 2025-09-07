# # obj = {
# #     "username":"sadikturan",
# #     "order_total":10000,
# #     "date":"10.10.2024",
# #     "memleket":"adana",
# # }



#  # sehirler = ["ağrı","siirt","ığdır"]
# # plakalar= ["10","20","40"]


# şehirler ={ "34":"istanbul",
#              "06":"ankara", 
# }


# # print(sehirler,şehirler)

# # index=sehirler.index("siirt")
# # # print(plakalar[index])

# # for i in sehirler:
# #         index=sehirler.index(i)
# #         print(sehirler.index(i), plakalar[index])
  
# şehirler["01"]="adana"
# şehirler["44"]="malatya"
# şehirler["46"]="malatya"
# print(şehirler)


# öğrenciler = {
#     101: {
#         "ad": "Yiğit Bilgi",
#         "dogum_yili": 2010,
#         "notlar": [70, 80, 90]
#     },
#     102: {
#         "ad": "Ada Bilgi",
#         "dogum_yili": 2011,
#         "notlar": [85, 75, 90]
#     },
#     103: {
#         "ad": "Çınar Turan",
#         "dogum_yili": 2012,
#         "notlar": [70, 70, 70]
#     },
#     104: {
#         "ad": "Elif Yılmaz",
#         "dogum_yili": 2013,
#         "notlar": [88, 92, 85]
#     },
#     105: {
#         "ad": "Mert Kaya",
#         "dogum_yili": 2011,
#         "notlar": [78, 81, 79]
#     },    
# }

# from datetime import datetime
# yil = datetime.now().year

# #örgenciNumarası=input("Öğrenci Numarasını Giriniz: ");
# # print(type(int(örgenciNumarası)),(örgenciNumarası))

# print("benim tipim: ",type(öğrenciler[103][0]["numara"]))

# for i in range(1, len(öğrenciler)):
#    # if örgenciNumarası==öğrenciler["numara"]:
#     yaş=yil-öğrenciler[103]["dogum_yili"];
#     ortalamaNot=(     öğrenciler[103]["notlar"][0]  +   öğrenciler[103]["notlar"][1]    +    öğrenciler[103]["notlar"][2])/3;
    
    
#     print(yaş)
    
öğrenciler = {
    101: {
        "ad": "Yiğit Bilgi",
        "dogum_yili": 2010,
        "notlar": [70, 80, 90]
    },
    102: {
        "ad": "Ada Bilgi",
        "dogum_yili": 2011,
        "notlar": [85, 75, 90]
    },
    103: {
        "ad": "Çınar Turan",
        "dogum_yili": 2012,
        "notlar": [70, 70, 70]
    },
    104: {
        "ad": "Elif Yılmaz",
        "dogum_yili": 2013,
        "notlar": [88, 92, 85]
    },
    105: {
        "ad": "Mert Kaya",
        "dogum_yili": 2011,
        "notlar": [78, 81, 79]
    },    
    
    106: {
        "ad": "Eşref Özbek",
        "dogum_yili": 2001,
        "notlar": [38, 83, 64]
    },  
}

from datetime import datetime

yil = datetime.now().year
ogrenci_numarasi = int(input("Öğrenci Numarasını Giriniz: "))

if ogrenci_numarasi in öğrenciler:
    ogrenci = öğrenciler[ogrenci_numarasi]
    yas = yil - ogrenci["dogum_yili"]
    ortalama = sum(ogrenci["notlar"]) / len(ogrenci["notlar"])
    
    print(f"\nAd: {ogrenci['ad']}")
    print(f"Yaş: {yas}")
    print(f"Not Ortalaması: {ortalama:.2f}")
else:
    print("Bu numaraya ait bir öğrenci bulunamadı.")
    
    

    
