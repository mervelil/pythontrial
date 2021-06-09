x =0
"""
while x <100:
    if(x%2==0):
        print(f"sayi cift: {x}")
    else:
        print(f"sayi tek: {x}")
    x =x+1
print("done...")t
"""
name ="" #false
while not name:
    name=input("enter your name")
print(f"Merhaba, {name}")
sayilar =[1,3,5,7,9,12,19,11]
i=0
while (i<len(sayilar)):
    print(sayilar[i])
    i +=1
baslangic =int (input("baslangıc: "))
bitis =int (input("finish: "))
i =baslangic
while (i<bitis):
    i +=1
    if( i %2 ==1):
        print (i)
k =100
while k>0:
    print(k)
    k-=5
nmuberss =[]
say =0
while say<5:
    nsay=int(input("sayi "))
    nmuberss.append(nsay)
    say +=1
print(nmuberss)
"""
products =[]
count = int (input ("how many have you wanna add"))
l=0
while(l<count):
    names =input("product name: ")
    prices = input("product price")
    products.append({
        "name": names,
        "price ":prices,
    })
    l +=1
for pro in products:
    print(f"product name: {pro["name"]} pro price: {pro["price"]})
"""
