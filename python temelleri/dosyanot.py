 def nothes(s):
     s =s[:-1]
     liste=s.split(":")
     ogrenciad = liste[0]
     notlar=liste[1]
     not1=int(notlar[0])
     not2=int(notlar[1])
     not3=int(notlar[2])
     ort =int((not1+not2+not3) /3)

     if ort>=90 and ort<=100:
         harf =="aa"
     elif ort>=85 and ort <=89:
         harf =="bb"
     else:
         harf ="ff"
     return ogrenciad+ ": "+ harf+"\n"
def ortBul():
     with open("sinav.txt","r",encoding="utf-8") as file:
         for s in file:
             print(nothes(s))
def notkaydet():
    with open("sinav.txt","r",encoding="utf-8") as file:
        liste =[]
        for i in file:
            liste.append(nothes(i))
    with open ("sonuclar.txt","w",encoding= "utf-8") as file2:
        for i in liste:
            file2.write(i)

def notgir():
    ad =input("ad:")
    sad =input("soyad:")
    n1 =input("not1:")
    n2 =input("not2:")
    n3 =input("not3:")
    with open("sinav.txt","a",encoding="utf-8")as file:
        file.write(ad+" "+sad+" "+n1+","+n2+","+n3+" "+"\n")


while True:
    islem =input("1-Not  oku \n2-Not gir\n3-notları kaydet\n4-Cıkıs\n")
    if islem=="1":
        ortBul()
    elif islem =="2":
        notgir()
    elif islem=="3":
        notkaydet()
    else:
        break