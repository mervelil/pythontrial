def yazdir(kelime,adet):
    print(kelime * adet)
yazdir("merhaba\n",10)
def listeyecevir(*params):
    liste=[]
    for param in  params:
        liste.append(param)
    return liste

lresult =listeyecevir(10,20,30,"Merhaba")
print(lresult)

def asalSayilariBul(num1,num2):
    for sayi in range(num1,num2+1):
        if sayi>1:
            for i in range(2,sayi):
                if(sayi % i ==0):
                   break
            else:
                print(sayi)
num1 =int (input("sayi  1:"))
num2 =int (input("sayi  2:"))
asalSayilariBul(num1,num2)
def tambolen(snum):
    tambolen=[]

    for i in range (2,snum):
        if (snum %i ==0):
            tambolen.append(i)
    return tambolen
print(tambolen(20))
def outer(sayii1):
    print(  "out")
    def inner(sayii1):
        print("in")
        return sayii1+1
    sayii2 =inner(sayii1)
outer(10)
print(sayii1,sayii2)
def usalma(number1):
    def inner(power):
        return number1**power
    return inner
t=usalma(2)
print(t)  
def toplama (a,b):
    return a+b 
def cık(a,b):
    return a-b

def carp(a,b):
    return a*b
def islem (f1,f2,f3,islemad):
    if islemad=="toplama":
        print(f1(2,3))
    elif islemad=="cikarma":
        print(f2(3,3))
    else:
        print("gecrsiz")
islem(toplama,cık,carp,"toplama")

def my_decorate(func):
    def wrapper(name):
        print("func onceki islemler")
        func(name)
        print( "func sonrası islem")
    return wrapper
def hello:
    print("hello",name)
@my_decorate
hello =my_decorate(hello)
hello("ali")
import time
import math
@calculate
def faktoriyel (num):
    start =time.time()
    time.sleep(1)

    print (math.factorial(num))
    finish =time.time()
    print("fonlk"+str(finish-start)+"saniye surdu")
return inner

def calculate(func):
    def inner (*args,**kwargs):
    start =time.time()
    time.sleep(1)
    func(*args,**kwargs)
    finish =time.time()
    print("fonlk"+str(finish-start)+"saniye surdu")
faktoriyel(5)