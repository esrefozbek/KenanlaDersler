# kelime = input("Kelimeyi Giriniz :")
# kez=int(input("Kaç kez :"))

# def tekrarmaqinesi():
#     for i in range(abs(kez)):
#         print(kelime)
# tekrarmaqinesi()

# uk=int(input("UZUN KENARI GİRİNİZ :"))
# kk=int(input("KISA KENARI GİRİNİZ :"))

# def alanVEçevre():
#     alan=kk*uk
#     ÇEVRE=(uk+kk)*2
#     print(f"""
# alanı: {alan}
# çevresi: {ÇEVRE}
#         olarak bulunmuştur      
#           """)
# alanVEçevre()

import random
# LİRA=["yazı","tura"]
# def YAZITURA():
#     print(random.choice(LİRA))
# YAZITURA()
from sympy import isprime
from rich.console import Console
from rich.panel import Panel

console = Console()

# def asallar(a:int,b:int):
#     for i in range(a+1,b):
#         if isprime(i):
#             console.print(f"{i} ",style=" black",end="")            
    
       
# s1=int(input("Sayı 1:"))
# s2=int(input("Sayı 2:"))

# asallar(s1,s2)

import random
from sympy import isprime
from rich.console import Console
from rich.panel import Panel

console = Console()
console.print(Panel("[bold cyan]Tam Bölenler Listesi[/bold cyan]"))

def TAMbölücüler(a: int):
    kaçBölenVar = 0
    renk_listesi = ["yellow", "red", "white", "green", "cyan", "magenta"]
    adı="Eşref"
    for i in range(1, a + 1):
        if a % i == 0:
            renk = random.choice(renk_listesi)
           
            
            console.print(adı,i, style=random.choice(renk_listesi), )
            kaçBölenVar += 1

    console.print(f"\n\n[bold magenta]{a} sayısının Allah'ın izniyle {kaçBölenVar} böleni var.[/bold magenta]")

# Kullanıcıdan sayı al
console.print("Bir sayı giriniz:", style="yellow", )
try:
    SAYI = int(input())
    TAMbölücüler(SAYI)
except ValueError:
    console.print("[red]Hatalı giriş! Lütfen tam sayı girin.[/red]")

          
          


    