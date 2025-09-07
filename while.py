# i=0
# while i<10:
#     print("Merhaba Dünya")
    
#     i += 1
#     if i == 10:
#         print("Döngü bitti")
#         break

# sayılar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# i=0
# while i < len(sayılar):
#     print(sayılar[i])
#     i += 1
#     if i == 10:
#         print("Döngü bitti")
#         break

# başlangıç = int(input("Bir sayı giriniz: "))
# bitiş= int((input)("Bir sayı giriniz: "))


# while başlangıç<bitiş:
#     if(başlangıç+1)%2==1:
#         pass
#     else:
#         print(başlangıç+1)
#     başlangıç+=1    



# for i in range(100, 0, -1):
#     print(i)

# i=int(input("Büyük sayıyı giriniz:"))
# j=int(input("Küçük sayıyı giriniz:"))
# while i>(j+1):
#     print(i-1)
#     i-=1; 

#

# sayilar=[11,12,3,4,5,6,6]
# sayilar.sort()
# print(type(sayilar.sort()))
# print(sayilar)
# sayilar=[]
# # for sayı in range(1,6):
# #     sayilar.append(int(input(f"{sayı}.sayıyı gir:")))
# #     sayilar.sort()
# # print(sayilar)

# i=1
# while i<6:
#     sayilar.append(int(input(f"{i}.sayıyı gir:")))
#     sayilar.sort()
#     i+=1;
# print(sayilar)



# while True:
#     name=input("Kullanıcı adınızı giriniz:")
#     if name=="":
#         print(f"Kullanıcı adınızı lütfen dogri girin")
#     else:        
#         print(f"Kullanıcı adınız {name} ")
#         break



# username=""
# print (bool(username))


# while  not username:
#      username=input("kullanıcı adını gir :")
    
# print ("kullanıcı adı "+ username)
    

# listem=[]
# sayi=0

# if not listem:
#     print("liste boştur")

# if not sayi:
#     print("sayı 0'dır.")

ogrenciler=[]



while True:
   
    ogrenci={"ogrenciNo":int,"ögrenciAdı":str, "ögrenciSoyadı":str    }
    
    print(  "Öğrencinin " )
    ogrenci["ogrenciNo"]=int(input("     numarasını giriniz: "))
    ogrenci["ögrenciAdı"]=input("     adını  giriniz: ")
    ogrenci["ögrenciSoyadı"]=input("    soyadını giriniz: ")
   
    ogrenciler.append(ogrenci)
   
    devamMi=input("devam için 'e', çıkmak içinm 'h' ye basınız ") 
    if devamMi=="e": 
        pass
    elif devamMi=="h":
        break  
        
for ogrenci in ogrenciler:  
    print(ogrenci)
 
# liste=[{ogrenci1},{ogrenci2},{ogrenci3},.....]
    
    
   