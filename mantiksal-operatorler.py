# x = 3
# if x > 0 and x % 2 == 0:
#     print("x, 0'dan büyüktür ve çift sayıdır.")
# else:
#     if x > 0 and x % 2 != 0:
#         print("x, 0'dan büyüktür ve tek sayıdır.")
   
   
# yas = int(input("Yaşınızı giriniz: "))
# izin = (input("Çalışma izniniz var mı? (True/False): "))
# izin = bool(izin.lower().capitalize().strip())
   
# if yas >= 18 and izin == True:
#     print("Çalışabilirsiniz.")
# else:
#      print("Çalışamazsınız.")

# sınavnotu = int(input("Sınav notunuzu giriniz: "))
# if sınavnotu >= 50 and sınavnotu <= 100:
#     if sınavnotu >= 85:
#         print("Tebrikler, A aldınız!")
#     elif sınavnotu >= 70:
#         print("Tebrikler, B aldınız!") 
#     elif sınavnotu >= 50:
#         print("Tebrikler, C aldınız!")
# else:
#     # print("Lütfen 50 ile 100 arasında bir not giriniz.")
#     if sınavnotu < 50 and sınavnotu >= 0:
#         print("Üzgünüm, D aldınız. Daha çok çalışmalısınız.")
#     else:
#         print("Lütfen 50 ile 100 arasında bir not giriniz.")
    
# notOrt=80;
# zayıfDersYok = False;
# if notOrt >= 70 and zayıfDersYok == True:
#     print("Tebrikler, teşekkür belgesi kazandınız.")
# else:
#     if notOrt >= 70 and zayıfDersYok == False:
#         print("Üzgünüm, teşekkür belgesi kazanamadınız.")
#     else:
#         print("Bi' bok kazanamadınız, not ortalamanız 70'in altında.")

# sigaraKullanmıyor = True;
# egitimDurumu = "Lisans"
# if sigaraKullanmıyor and (egitimDurumu == "Lisans" or egitimDurumu == "Yüksek Lisans"):
#     print("İşe alındınız.")
# else:
#     print("İşe alınmadınız.")
    
    
    
kullanıcıAdı = input("Kullanıcı adınızı giriniz: ")
şifre = input("Şifrenizi giriniz: ")
email = input("E-posta adresinizi giriniz: ")

if (kullanıcıAdı == "admin" and şifre == "12345" and email =="kenanbaba@gmail.com"):
    print("Giriş başarılı!")
else:
    if kullanıcıAdı != "admin":
        print("Kullanıcı adı yanlış.")
    if şifre != "12345":
        print("Şifre yanlış.")
    if email !="kenanbaba@gmail.com:":
        print("E-posta adresi yanlış.")
        
        
        
        
        
        
        
        