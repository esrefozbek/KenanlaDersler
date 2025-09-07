# kurum='BTK'

# sayilar=[3,6,2,8]


# sayi1=15.9;
# text="Dalyarrak Necmi  ";

# myMail="esrefozbek@hotmail.com";

# dalMi=      text.startswith("Dal");

# dalmi=str.startswith(text,"dal");

# tipim=        type(myMail)

# print(dalMi, )


# print(dalmi)

# kursAdi = "C# İle Proglamlama" 
# kursAciklama = "güzel bir kurs"
# kursSuresi = "2000"

# mesaj = "Kursun Adı: " + str(kursAdi) + ", " + "Kursun Açıklaması: " + str(kursAciklama) + ", " + "Kurs Süresi: " + str(kursSuresi)

# print(mesaj)



# # stringler.py

# from degiskenler import DegiskenNedir
# from degiskenler import Aritmetik

# # Doğrudan sınıf değişkenine eriş
# print(DegiskenNedir.neresi)

# # veya metod üzerinden:
# print(DegiskenNedir.city())


# print(DegiskenNedir.neresi[0])

# listem=["i","s","t","a","n","b","u","l"]
# print (listem[3])


# print(Aritmetik.toplama(3,5) )


# uzunluk= len(mesaj)

# print(len(mesaj))

# kurs = "Python ile Proglamlama"

# indexim="Python ile Proglamlama"[7]


# listemm=["r","f","g"]
# print(listemm[1],   indexim)

# print (kurs[-22:])

# print('-----------------------------------------')

# # string concat 

# ad = "Kenan"
# soyad = "Özbek"
# yas = 14

# """ msj = "My Name is " + ad + " " + soyad + "."+ "I'm " + str(yas) + " years old."
# print(msj) """

# msj = "My Name is {1} {0} I'm {2} years old.".format(ad, soyad, yas)
# print(msj)

# msj = "My Name is {a} {s} I'm {y} years old.".format(a=ad,s= soyad,y= yas)
# print(msj)


# msj = f"My Name is {ad} {soyad} I'm {yas} years old.,,,,,"
# print(msj)

title = "Python ile proglamlama dersleri"

uzunluk=len(title)
print(uzunluk) 
# print(title[0:6],title[-6:-1])
print(title[::-4])


adSoyad=input("adınızı giriniz: ")
not1=input("1. notu giriniz: ")
not2=input("2. notu giriniz: ")
ortalama=(float(not1)+float(not2))/2

print("{} adlı öğrencinin 1.notu {} , 2.notu {} ve not ortalaması {} olarak hesaplanmıştır.".format(adSoyad, not1 , not2 ,ortalama))

print(f"{adSoyad} adlı öğrencinin 1.notu {not1} , 2.notu {not2} ve not ortalaması {ortalama} olarak hesaplanmıştır.")

