# x=70
# y=70

# if( x <y):
#     print("x, y'den küçüktür")
# elif( x > y):
#     print("x, y'den büyüktür")
# else:
#     print("x, y'ye eşittir")



# benzin= 39.35
# dizel= 41.71
# lpg= 20.28
# MESAFE=50




# ARAÇ=input("Araç türünü giriniz (benzin, dizel, lpg): ")







# if ARAÇ == "benzin":
#     print("Benzinli araç ile", MESAFE, "km yolculuk maliyeti:", benzin * MESAFE)
# elif ARAÇ == "dizel":
#     print("Dizel araç ile", MESAFE, "km yolculuk maliyeti:", dizel * MESAFE)
# elif ARAÇ == "lpg":
#     print("LPG'li araç ile", MESAFE, "km yolculuk maliyeti:", lpg * MESAFE)
# else:
#     print("Geçersiz araç türü girdiniz. Lütfen 'benzin', 'dizel' veya 'lpg' giriniz.")

y1=int(input("1. Yazılıyı giriniz: "))
y2=int(input("2. Yazılıyı giriniz: "))
y3=int(input("3. Sözlüyü giriniz: "))

ortalama=(y1+y2+y3)/3

if ortalama >= 85:
    print("Harf Notunuz: 5")
elif ortalama >= 70:
    pass  # This line was missing in the original code
    print("Harf Notunuz: 4")
elif ortalama >= 55:
    print("Harf Notunuz: 3")
elif ortalama >= 45:
    print("Harf Notunuz: 2")
elif ortalama >= 25:
    print("Harf Notunuz: 1")
else:
    print("Harf Notunuz: 0")
print("Ortalamanız:", ortalama)


#ANCHOR - değişiklik yaptım
