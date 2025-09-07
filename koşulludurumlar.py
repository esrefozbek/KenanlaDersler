i=0
while True:
    print("i:", i)
    i+=1    
    if i == 5:
        break

şifre=input("Şifrenizi giriniz: ")
login = (şifre == "123456")


while True:
    if login:
        print("Giriş başarılı")
        break 
    else:
        print("Giriş başarısız")
        şifre=input("Şifrenizi tekrar giriniz: ")
        login = (şifre == "123456")

