import keyboard

liste = []

def sayi_ekle():
    try:
        sayi = int(input("Lütfen bir sayı gir: "))
        liste.append(sayi)
        print("Liste:", liste)
    except ValueError:
        print("Geçerli bir sayı girilmedi!")

print("Program çalışıyor. '+' tuşuna basarak sayı ekleyebilirsin. (Çıkmak için Ctrl+C)")



while True:
    keyboard.wait('+')  # '+' tuşu bekleniyor
    sayi_ekle()
    
    
    