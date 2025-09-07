my_list = [1,2,3]
my_tuple =1,2,3 # değiştirilemez

print(type(my_list))
print(type(my_tuple))


my_list[0] = 2
# my_tuple[0] = 2

my_tuple2 = tuple([2,3,4])

my_list.append(3)
sonuc=my_tuple.count(1)

sonuc1=my_list[0]
sonuc2=my_tuple[0]
print(sonuc1,sonuc2)

my_list=tuple(my_list)

print(my_list,type(my_list))

my_list=list(my_list)
print(type(my_list))


