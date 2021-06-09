numbers =[1,2,3,4,5,6]
for num in numbers:
    print(num) #hello yazarsan 5 kere yazar mesela

names =["cınar","samet","mehmeet"]
for a in names:
    print(f"my name is {a}")
name ="sadik turan"
for n in name :
    print(n)
tuple =[(1,2),(1,3),(3,5)]
for a,b in tuple:
    print(a,b)
d ={"k1":1,"k2": 2,"k3":3}
for key,value in d:
    print (key,value)
sayilar =[1,3,5,7,9,12,19,11]
for sayi in sayilar:
    if(sayi %3==0):
        print(sayi)
toplam =0
for sayi in sayilar:
    toplam +=sayi
    print("toplam " , toplam)
for sayi in sayilar:
    if(sayi%2==1):
       print(sayi**2)
sehirler =["kocaeli","istanbul","ankara","izmir","rize"]
for sehir in sehirler:
    if(len(sehir)<=5):
        print(sehir)
urunler = [
    {"name": "samsung S6","price": "3000"},
    {"name": "samsung S7","price": "4000"},
    {"name": "samsung S8","price": "4000"},
    {"name": "samsung S9","price": "7000"},
    {"name": "samsung S10","price": "8000"},
]
for urun in urunler:
    fiyat = int(urun["price"])
    toplam +=fiyat
print("toplam urun fiyati" ,toplam)

for urun  in urunler:
    if (int (urun["price"])<=5000):
        print(urun["name"])

