# defined kısaltmısı
def sayHello(name1 ="user"):
    print("hello "+name1)
def sayHello(name1 ="user"):
    return "hello "+name1
msg = sayHello("cınar") 
print(msg) 
sayHello()

sayHello("ada")
sayHello("deniz")

def total (num1,num2):
    return num1+num2
result =  total(10,20)
#print(help(result)) #help iceriigi falan kulllanır
def yasHesapla(bornyear):
    return 2020-bornyear
ageAda =yasHesapla(2001)
ageCinar = yasHesapla(2000)
print(ageAda,ageCinar)

def changeName (n):
    n ="ada"
name2 ="yigit"
changeName(name2)
print(name2)
def change(ni):
    ni[0]="ist"
sehirler=["anka","izmrie"]
#n =sehirler[:] #slicing birebir aslı olandır kopyası deıl o yzdn ank izmir yazar
change(sehirler)
print(sehirler)
def add (a,b,c=0):
     return sum((a,b,c))
print(add(34,67))

def adds(*params):
    """
    sum =0
    for n in params:
        sum +=n
        return sum
        """
    return sum((params)) #parsms is tuple
print(adds(345,56,45,456,456))
def displayuser(**args): #** dictinary oldugunu belirtiyoo
    for key,val in args.items():
        print("{} is {}".format(key,val))
result = displayuser(name ="cinar", age =4,city ="boston")
#displayuser(name = "ada",age =45,city ="boston")
print(result)
def myfunc (a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
myfunc (10,20,30,40,50,key1="value 1", key2 ="value 2")
import modudul
result =help(modudul)
print(result)