from rich.console import Console
from rich.table import Table
from rich.align import Align
import json
from rich.console import Console
from sympy import isprime
from rich.panel import Panel
from rich import box
from rich.align import Align

console = Console()


#global müsteriler
musteriler=[]
musteri={}


def menu():
    icerik = """[bold green]1.[/] Para Çekme
[bold green]2.[/] Para Yatırma
[bold green]3.[/] Bakiye Sorgulama"""
    panel = Panel(          
        Align.center(icerik, vertical="middle",style="yellow"),
        title="[bold white]İşlem Menüsü[/]",
        subtitle="Lütfen bir işlem seçiniz",
        padding=(1, 2),
        border_style="bright_blue")
    console.print(panel)
    
    


def islemseçimi():
    console.print("Yapmak istediğiniz işlemi seçiniz (1, 2, 3):", style="yellow", end="")
    işlem = input()
    if işlem == "1":
        console.print("[bold red]Para Çekme İşlemi Seçildi[/]")
        console.print("[yellow]Ne kadar çekmek istiyorsunuz?   [/yellow]")
        çekilenMiktar=int(input())
        paraçekme(çekilenMiktar)
        
    elif işlem == "2":
        console.print("[red]Para Yatırma İşlemi Seçildi[/]")
        console.print("[yellow]Ne kadar para yatıracaksınız ?   [/yellow]")
        yatırılanMiktar=int(input())
        parayatırma(yatırılanMiktar)
        
        
    elif işlem == "3":
        console.print("[green]Bakiye Sorgulama İşlemi Seçildi[/green]")
        bakiyeSorgula()
        
    else:
        console.print("[red]Geçersiz işlem. Lütfen 1, 2 veya 3 girin.[/red]")
        

def jsondanYukleme():
    global musteriler
    with open("musteriler.json", "r", encoding="utf-8") as dosya:
        musteriler = json.load(dosya)
       
    # console.print("\n\njson yüklendi:  ",musteriler,style="magenta")    
    # console.print("\n\njson yüklendi[0]:  \n",musteriler[0],style="green")    
        
        
def jsonaKaydet():
    global musteriler
    with open("musteriler.json", "w", encoding="utf-8") as dosya:
        json.dump(musteriler, dosya, indent=4, ensure_ascii=False)
    console.print("[green]Müşteri verileri başarıyla kaydedildi.[/green]")
     
  
def musteriBul(): 
    while True:
        müşteriBulunduMu = False
        console.print("Müşterinin [bold green][italic]e-devlet[/italic][/bold green] numarasını  Giriniz:", style="yellow", end="")
        Edevlet=int(input())
        global musteri
        for musteri in musteriler:
            if musteri["eDevlet"] == Edevlet:
                müşteriBulunduMu = True
                console.print("\n\nMüşteri bulundu:",style="bold green")
                console.print(f"Ad: {musteri['ad']}",style="bold blue")
                console.print(f"Soyad: {musteri['soyad']}",style="bold blue")
                console.print(f"IBAN: {musteri['iban']}",style="bold blue",end="\n")
                #console.print(f"Bakiye: {musteri['bakiye']} TL",style="bold blue", end="\n")

                #print("Bul içinde musteri bulundu", musteri["ad"])
                console.print("[yellow]Ne Yapmak İstiyorsunuz[/yellow]")
                menu()
                return musteri


        else:
                console.print("Müşteri bulunamadı.", style="bold red")
                müşteriBulunduMu = False


def paraçekme(çekilenMiktar:int):
    global musteriler, musteri
    #console.print("paraçekme içinde müşteri :",musteri)
    bakiye=musteri["bakiye"] 
    # print(bakiye)
    if çekilenMiktar<=bakiye:
         bakiye-=çekilenMiktar
         musteri["bakiye"] = bakiye
         jsonaKaydet()
         console.print(f"{musteri["ad"]}'in bakiyesi {bakiye} TL dir.", style="bold magenta")
    else:
         print("Bakiyeniz yetersiz.")
    

def parayatırma(yatırılanMiktar:int):
    global musteriler, musteri
    bakiye=musteri["bakiye"] 
    if yatırılanMiktar>0:
        bakiye+=yatırılanMiktar
        musteri["bakiye"] = bakiye
        jsonaKaydet()
        console.print(f"{musteri["ad"]}'in bakiyesi {bakiye} TL dir.", style="bold magenta")

from rich.console import Console
from rich.table import Table
from rich import box
console = Console()
def bakiyeSorgula():
    global musteriler, musteri
    bakiye = musteri["bakiye"]
    table = Table(
        title="Bakiye Bilgisi",
        show_header=True,
        header_style="bold cyan",
        box=box.ROUNDED
    )
    table.add_column("e-Devlet", style="bold green")
    table.add_column("Ad", style="bold green")
    table.add_column("Soyad", style="bold green")
    table.add_column("IBAN", style="bold green")
    table.add_column("Bakiye (TL)", justify="right", style="bold magenta")
    # Güvenli erişim ve str dönüşümü
    e_devlet = str(musteri.get("eDevlet", "-"))
    table.add_row(
        e_devlet,
        musteri["ad"],
        musteri["soyad"],
        musteri["iban"],
        f"{bakiye:,}"  # Örn: 120,000
    )
    console.print(table, justify="center",end="\n")
    
         


    
if __name__=="__main__":
  
    jsondanYukleme()
    musteriBul()
    islemseçimi()