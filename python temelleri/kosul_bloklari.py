if 3 ==3:
    print('Hosgeldin')
# if isLoggedin =False


user="barbabra"
passw="1234"

if(user =="barbabra"):
     if(passw=="1234"):
         print("hosgeldin")
     else:
         print("parola yanlis")  
else:
    print(" usernaame false")

x = int(input("x: "))
y =int(input("y: "))
if x>y:
    print("x y den buyuk") 
elif x ==y:
    print(" x y ye esit")
else:
    print("y x den buyuk")      

isim = input("isminiz") 
yas =int (input("yas: "))
egitim = input("egitim: ")   
if (yas >=18) and (egitim=="lise" or egitim=="uni") :
    print("ehliyet alabilir")
else:
    print("ehliyet alamaz")

s1 =float(input("1.yazılı ")) 
s2 =float(input("2.yazılı ")) 
s3 =float(input("sozlu ")) 
orta=(s1 + s2 + s3) /3
if (orta>=0) and (orta <25):
    print(f"ortalamanız: {orta} notun : 0 ")
elif (orta>=25) and (orta <45):
    print(f"ortalamanız: {orta} notun : 1 ")
elif (orta>=45) and (orta <55):
    print(f"ortalamanız: {orta} notun : 2 ")
elif (orta>=55) and (orta <69):
    print(f"ortalamanız: {orta} notun : 3 ")
elif (orta>=70) and (orta <85):
    print(f"ortalamanız: {orta} notun : 4 ")
elif (orta>=85) and (orta <100):
    print(f"ortalamanız: {orta} notun : 5 ")
else:
    print("yanlıs bilgi girdiniz")

import datetime
^#days = int(input ("Aracınız kac gundur trafikte: "))
tarih = input ("Aracınız hangi tarihten beri trafikte: ")
tarih = tarih.split("/")
trafik = datetime.datetime(int(tarih[0]),int(tarih[1]),int (tarih[2]))
simdi = datetime.datetime.now()
fark = simdi -trafik
days =fark.days
if days<=365:
    print("1. servis aralıgı")
elif days>365 and days <=365*2:
    print("2. servis aralıgı")
elif days>365*2 and days <=365*3:
    print("3. servis aralıgı")
else:
    print("hatalı sure")

