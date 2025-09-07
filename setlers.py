
meyvalar = ["elma", "armut", "muz"] 
meyvalar1 = ("elma", "armut", "muz")
meyvalar2 = {"elma", "armut", "muz", "vişne"}
meyvalar3={"elma", "armut", "muz", "çilek","kivi","karpuz","erik", }

sonuc=meyvalar2
print(sonuc)



for i in meyvalar2:
    print(i)
    
meyvalar2.add("çilek")
print(meyvalar2) 


print("çilek" in meyvalar2) 

meyvalar2.update(meyvalar3)
print(meyvalar2)    





   

