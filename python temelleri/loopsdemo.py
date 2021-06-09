import random
sayi = random.randint(1,10)
hak=5
say=0
while hak>0:
    hak-=1
    say +=1
    tahmin = int (input("tahmin "))
    if sayi== tahmin:

        print(f"tebriksss {say}. defada bildin.Toplam puan : {100-(20)*(say-1)}")
        break
    elif sayi>tahmin:
        print("yukarı")
    else:
        print("asagı")
    if hak==0 :
        print("hakkınız bitti")   
        #asal bulma
    number=int (input("sayi: "))
    asalmi=True
    if number==1:
        asalmi=False
    for i in range(2,sayi):
        if(sayi%i==0):
            asalmi=False
            break
   if asalmi:     
       print("sayi asal")
   else :     
       print("sayi asal degil ")
       #fonksiyon ile method arasındaki fark fonksiyonlar classın bunyesinde degıl