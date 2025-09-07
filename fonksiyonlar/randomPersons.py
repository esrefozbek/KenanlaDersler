musteriler = [
    {"ad": "Ahmet", "soyad": "Yaman", "iban": "TR23423425432525", "bakiye": 420000},
    {"ad": "Mehmet", "soyad": "Yaman", "iban": "TR234234253452525", "bakiye": 330000},
    {"ad": "Pakize", "soyad": "Yaman", "iban": "TR23fdsdf3425525", "bakiye": 2500},
]

# Örnek isimler ve soyisimler
isimler = [
    "Ali", "Ayşe", "Fatma", "Emre", "Deniz", "Selin", "Murat", "Burak", "Elif", "Cem",
    "Ece", "Hasan", "Hüseyin", "Gül", "Berk", "Okan", "Seda", "Özge", "Barış", "Derya",
    "Sibel", "Tolga", "Yusuf", "Fikret", "Kemal", "Merve", "Neşe", "Rıza", "Suat", "Zehra"
]

soyisimler = [
    "Yaman", "Demir", "Kaya", "Çelik", "Şahin", "Yılmaz", "Öztürk", "Arslan", "Doğan", "Güneş",
    "Korkmaz", "Polat", "Aslan", "Erdoğan", "Kılıç", "Aydın", "Çetin", "Kara", "Özkan", "Kaya",
    "Uysal", "Sever", "Gür", "Taş", "Aksoy", "Turan", "Yalçın", "Duran", "Coşkun", "Çalışkan"
]

edevletler   = range(1,31)

# Mevcut 3 elemanı koruyup kalanını dolduralım
import random

while len(musteriler) < 30:
    ad = random.choice(isimler)
    soyad = random.choice(soyisimler)
    eDevlet = random.choice(edevletler)
    iban = "TR" + "".join([str(random.randint(0,9)) for _ in range(16)])
    bakiye = random.randint(1000, 500000)
    musteriler.append({
        "eDevlet": eDevlet,
        "ad": ad,
        "soyad": soyad,
        "iban": iban,
        "bakiye": bakiye
    })
print((musteriler))
# Kontrol için yazdırma
for musteri in musteriler:
    
    print(musteri, end=",\n")
