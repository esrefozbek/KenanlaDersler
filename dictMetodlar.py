

yemekTarifi={
    
     "yemekAdi":"Musakka",
    "yemekTarifi":"tarif açıklaması",
    "resim2":"https://images.pexels.com/photos/33118519/pexels-photo-33118519.jpeg",
    "malzemeler":["1 kg patlıcan", "500 gr kıyma",],
    
    "yemekPuan":4.5,
    
    "yemekYorumlar":[
        "Patlıcanlar çok güzel kızartılmış.",
        "Kıymanın baharatları çok iyi ayarlanmış.",
        "Yemeğin sunumu harikaydı.:)",       
        "Yemek çok lezzetliydi.",
        "Patlıcanın tadı harikaydı.",
        "Kıyması çok iyi pişirilmişti."     
    ]
    }



yemekTarifi["yemekAdi"]
print(yemekTarifi.get("yemekAdi"))


print(yemekTarifi.items())




print(yemekTarifi.get("yemekAdi"))


yemekTarifi["yemekAdi"]="Zumpir"
yemekTarifi.update({"yemekPuan":4.8})

print("Yemeğin Puan Ortalaması:",yemekTarifi.get("yemekPuan"))

yemekTarifi.pop("yemekAdi")
print(yemekTarifi.get("yemekAdi"))


print(yemekTarifi["yemekAdi"] if "yemekAdi" in yemekTarifi else "Yemek adı bulunamadı." )

    
print(yemekTarifi.get("yemekAdi","Yemek adı bulunamadı."))

print(yemekTarifi.get("yemekPuan",0))