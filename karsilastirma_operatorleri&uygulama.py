# # a="ahmet"
# # b="Ahmet"
# # print(a>b)


# # print(c < d)
# # print(c > d)

# # print("eşit değil mi?", c != d)


# # c = input("c sayısını giriniz: ")
# # d = input("d sayısını giriniz: ")

# # if c.isdigit() :
# #     c = int(c)  # c'yi tamsayıya dönüştür
# # else:
# #     print("c sayısı sayısal bir değer değil.")
     
# # if d.isdigit() : 
# #     d = int(d)  # d'yi tamsayıya dönüştür   
# # else:
# #     print("d sayısı sayısal bir değer değil.")


# # if c>=d:
# #     if c > d:
# #         print("c d'den büyüktür")
# #     else:
# #         print("c d'ye eşittir")
# # else:
# #     print("c d'den küçüktür")
    
# # sonuc=True;



# # parola=123;

# # while True:
# #     try:
# #         parola = int(input("Parolanızı giriniz: "))
# #         break  # Doğru bir giriş yapıldığında döngüden çık
# #     except ValueError:
# #         print("Lütfen geçerli bir sayı giriniz.")   
        
        
# x=[1, 2, 3, 4, 5]
# y=[1, 2, 3, 4, 5]


# z=y

# print(id(x),id(y),id(z))
# print(x==y)
# print(x is y)  # Kimlik karşılaştırması

# print(x is not y)  # Kimlik karşılaştırması 

# j = 5;
# h = 30;
# print(j>h)
# if j > h:
#     print("j, h'den büyüktür")
# else:
#     print("j, h'den küçük veya eşittir")

# sayi = int(input("Sayıyı giriniz: "))
# if sayi%2==0 :
#     print("Sayı çifttir")
# else:
#     print("Sayı tektir")

not1=int(input("Notunuzu giriniz: "))
not2=int(input("Notunuzu giriniz: "))
not3=int(input("Notunuzu giriniz: "))

ortalama = (not1 + not2 + not3) / 3

if ortalama >= 50:
    print("Tebrikler, geçtin!")
else:
    print("Üzgünüm, kaldın. Daha çok çalışmalısın.")