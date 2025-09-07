from rich import print
from rich.console import Console
console = Console()


def selam(MESAJ):
    for i in range(1,4):
      
        print(i,MESAJ,"[yellow]Merhaba Dünya  [/yellow]")
    


selam("Mustafa")
