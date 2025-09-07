

# aile:str
# ad:str
# soyad:str
# no:int
# adres:str
# evliMi:bool
# bosh:None


# ad="Eşref Mahmut Karaca ÖZBEK T"
# soyad="ÖZBEK"
# no=332


# degiskenKutusu=ad.split()


# print(type(degiskenKutusu))
# print(degiskenKutusu[2])

# print(degiskenKutusu[0])

# print(ad.replace(" ","").upper())

# print("tipim:  ",type(ad[5]))

# ad.upper()

# degiskenKutusu.append("4444")


# print("yeni eklenmiş :",  degiskenKutusu)
# print("upperlenmiş  : ",ad)


# yeniListe=degiskenKutusu


# print  ("yeni listem :  ",yeniListe)

# print(id(degiskenKutusu))
# print(id(yeniListe)) 

# """ ad2=ad
# print(id(ad))
# print(id(ad2))

# no2=no
# print(id(no))
# print(id(no2))

# print(len(ad))
#  """

kurum = ["Btk","kızılay","yeşilay","TÜİK","Afad","YSK"]   
    
# print(kurum[1:3]) 
    
    
    
# isim="kamil"

# isim2=isim


# print(isim, isim2)
# print(id(isim), id(isim2))


# isim="zeynep"
# print(isim, isim2)
# print(id(isim), id(isim2))

# isim2="zeynep"

# print(id(isim), id(isim2))

# ogrenci = [["Ahmet" ,"Kaya",60,50,70],["Memmet" ,"Demirtaş",10,90,60],["Serpil" ,"Öcalan",51,72,62    ] ]
# # ortalama= str((ogrenci[2] + ogrenci [3] + ogrenci [4])/3)

# # print(ogrenci[0]+ " " + ogrenci[1], ortalama )

# print(ogrenci[0])
# print(ogrenci[1])
# print(ogrenci[2])

# print(ogrenci[0][0:2])
# print(ogrenci[0][3])


programlamaDiller = ["python","C#","Java","Javascript","PHP","Dart","C++","C","Rust","Go"]

sonuc = programlamaDiller


"""
print(sonuc)
print(id(sonuc),id(programlamaDiller))
sonuc = type(programlamaDiller)
print(sonuc)
sonuc = programlamaDiller[0:2]

print(sonuc)

programlamaDiller[0] = "Pythoncuk"


print(programlamaDiller)

isim="maamut"   
isim.upper()
print(isim)

başlık="pyton'da Listeler"  # ["p","y","t","'", " ",  ........., "r"]

print(başlık.title())

print  (  len(başlık)     )

print(len(programlamaDiller))

programlamaDiller.append("Delphi")  
print(programlamaDiller)


programlamaDiller= programlamaDiller + ["Cobol","Pascal"]

print(programlamaDiller)

print (başlık.find("dam"))
print ("dam" in başlık)

for i in programlamaDiller:
    print (i)
    
print("----------------------------------------------------")
    
for i in başlık:
    print (i, " bir harftir")
    
    
    
print("----------------------------------------------------")
"""

    
# Uygulama




# arabaMarkaları =["Toyota","BMW","Renault","Tofaş","Mercedes"] 

# print("listenin uzunluğu:", len(arabaMarkaları))

# print("ilk eleman:", arabaMarkaları[0])
# print("son eleman:", arabaMarkaları[-1])
# print("son eleman:", arabaMarkaları[4])


# print("Renonun indeks numarası:",arabaMarkaları.index("Renault"))

# arabaMarkaları [2]="Togg";

# print("Togg listede mi?  :", "Togg" in arabaMarkaları)

# if "Toggx" in arabaMarkaları:
#     print("Togg listede var!");
# else:
#     print("Togg listede yok!");
    
# print(arabaMarkaları[:2])

# ilaveMarkalar=["Ford","Citroen"]
# arabaMarkaları.append("sada")

# listemci=[]

# listemci.extend("315")


# print("İki Marka eklendi:", arabaMarkaları)

# print("listemci  :",   listemci)

# list1=["elma"]
# list2=["muz"]

# print(id(list1),id(list2))

# list1=list2
# print(list1)

# print(id(list1))

    
# eşitlikte aktarılan eleman daima sağdaki elemandır.
# = işareti atama , aktarma ve yeni değeri verme anlamına gelir 


 

# isim="eşref özbek"
# isim=isim.upper()
# print(isim)

# for marka in "arabaMarkaları":
    
#     print(marka, type(marka), id(marka))
    
    
# liste1=["elma"]
# liste2=["muz"]

# liste3= liste1 + liste2
    
# print(liste1, liste3)  


# yeniListe=["Şavrolet"," Tofaş","Skoda"]
# arabaMarkaları.extend(yeniListe)
# print (arabaMarkaları)

# arabaMarkaları.pop()

# # print(arabaMarkaları)

# # del arabaMarkaları[-1]

# # print(arabaMarkaları)


from datetime import datetime

yil = datetime.now().year
print(yil)

isim="Mehmet Çınar";
dt=2010; 
not1=65;  
not2=32;  
not3=43;


veriler = [
    
 [isim, dt ,[not1,not2,not3]],
 
 ["Ada Bilgi", 2012 ,[70,7,8]],
 ["Maamut Taş", 2017 ,[75,83,92]],
 ["Aarif Toprakses", 2007 ,[7,81,3]],
 ]


for talebe in veriler: 
        #kişi= ["Maamut Taş", 2017 ,75,83,92],
        
        
      ort=(talebe[2][0] + talebe[2][1] + talebe[2][2])/3  ;
      

      if ort > 49:
            print(talebe[0],"geçtin!",  "   ..........    ", talebe[0],talebe[1],"doğumlu,","ve yaşı:",(yil-talebe[1]), " ...........  Ortalama notu: ",round(ort,1))
      else:
            print(talebe[0],"KALDIN!","     ...........    ", talebe[0],talebe[1],"doğumlu,","ve yaşı:",(yil-talebe[1]), " ............  Ortalama notu: ",round(ort,1))
      
    #   sayi1=int("315")
    #   print(type(ort))
        


ad="salih özşeker";

listecik=[ad] 


for i in range(0, len(veriler)):
    print("Hello World");
    

def topla (a,b):
    return a+b;



