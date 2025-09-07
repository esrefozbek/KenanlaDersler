from rich.console import Console
import math as m




z = Console()
z.print(m.sqrt(25))

with open("dosyam1.txt", encoding="utf-8") as f:
    satir1 = f.readline()
    satir2 = f.readline()

    z.print("[bold green]1. Satır:[/]", satir1)
    z.print("[bold green]2. Satır:[/]", satir2)

    karakterler = f.read(23)
    pozisyon = f.tell()

    z.print("23 karakterlik veri:", karakterler, style="bold yellow")
    z.print(f"Şu anki konum (byte): [italic]{pozisyon}[/]")

# Diğer dosya
with open("c:/Users/Pavlus/Desktop/got.txt", encoding="utf-8") as d:
    z.print("[bold cyan]Diğer dosya ilk satır:[/]", d.readline())
    z.print("[bold cyan]Diğer dosya ilk satır:[/]", d.readline())

file=open("dosyam1.txt", encoding="utf-8")
try:
    with open("dosyam1.txt", encoding="utf-8") as file:
        for i in file:
            z.print(f"[italic]{i}[/]", end="",style="bold green")

except FileNotFoundError as e:
    z.print("Dosya okuma hatası oldu.", style="bold red")


