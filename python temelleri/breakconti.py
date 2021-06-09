name = "sali evren"
for letter in name:
    if letter =='e':
      #  break olursa e den sonrasonı yazmaz
        continue # e yazmayıp diywrleri yazar
    print(letter)
x =0
while x<5:
    x+=1 #eher x iften sonra yzarsan 2 de den sonrasını contın olsa da devam etmez
    if x ==2:
        continue
    print(x)
    
    #dongu operatorleri
    print("***********")
for item in range(5,10,2): #1o dahil degil
    print(item)
print(list(range(50,100,20)))
#enumrate
greeting =  "hello"
for item in enumerate(greeting):
    print(item)
alist =[1,2,3,4,5]
blist =[ "a","v","c","v","b","s"] #6 nosta kaldı 

print(list(zip(alist,blist)))
for a,b in zip(alist,blist):
    print(a,b)

for m in range (10):
    print(m)
numbers =[x**2 for x in range (10) ]
print(numbers)
numbers =[x**2 for x in range (10) if x %3==0]
print(numbers)

myString ="hello"
mylist =[]
for letter in myString:
    mylist.append(letter) 
print(mylist)

mylist =[letter for letter in myString]
print (mylist)

years =[12345,3456,345,3456]
ages = [2020- year for year in years]
print(ages)
result = [s if s%2==0 else  "tek" for s in range(1,10)]
print(result)

for f in range(3):
    for fi in range(3):
        result.append((f,fi))
#diger yazımıyla
numberss=[(x,y) for x in range(3) for y in range (3)]
print(numberss)