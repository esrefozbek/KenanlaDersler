# x=10
# y=20

# x=y
# print(id(x), id(y))
# y=30

# print(x, y)
# print(id(x), id(y))

a=["elma","armut", "muz"]
b=["kiraz","çilek", "kivi"]
print(id(a), id(b))


a=b
print(a, b)
print(id(a), id(b)) 

a[0]="karpuz"
print(a, b)
print(id(a), id(b))
# a ve b aynı referansı gösteriyor
# bu yüzden a'da yapılan değişiklik b'yi de etkiler

print(a==b)
