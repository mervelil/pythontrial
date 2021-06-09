Sad ={
    "ad: " : "Ahmet",
    "hesap no :":"234567",
    "bakiye": 2000,
    "ek hesap":2003

}
Meh ={
    "ad: " : "Ada",
    "hesap no :":"23674567",
    "bakiye": 2500,
    "ek hesap":2025

}
def paraCek(hesap,miktar):
    #print(f"Merhaba{hesap["ad"]}")
    if (hesap ["bakiye"] >= miktar):
        hesap["bakiye"] -=miktar
        print("paranı alabilirsin")
    else:
        toplam =hesap ["bakiye"] + hesap["ek hesap"]
        if (toplam >=miktar):
            ekHesapKull=input("ek hesap kullanılsın mı(e/h)")
            if ekHesapKull =="e":
                ekHesapKull=miktar-hesap["bakiye"]
                hesap["bakiye"]=0
                hesap["ekhesap"]-=ekHesapKull
                print("cekebilirsin")

               
            else:
               print(f" {hesap[bakiye]} bulunmakta.")
        else:
            print("bakiye yetersiz")
def bakiyeSor(hesap):
    print(f"{hesap[hesapno]}nolu hesapta {hesap[bakiye]}var")
paraCek(Meh,2000)