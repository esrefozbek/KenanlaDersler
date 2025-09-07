
import datetime
from rich.console import Console
console=Console()

def yıl():
    yıl=datetime.datetime.now().year
    return int(yıl)

def yasHesapla(dogumYili):
    return yıl() - dogumYili

def emekliligeKacYilKaldi(dogumyili,isim):
    yas = yasHesapla(dogumyili)
    console.print(f"Yaşınız: {yas}", style="bold magenta")
    if yas < 65:
        console.print(f"{isim} emekliliğe {65 - yas} yıl kaldı", style="bold green")
    else:
        console.print(f"{isim} emekli oldu.", style="bold red")



emekliligeKacYilKaldi(1980, "Ahmet")