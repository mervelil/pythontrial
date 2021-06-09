
        #Tuple
 
# tupled = (1,"iki",3)   

#print(tupled[2])
 #print(type(tuple))
 #list=["ali","ayse"] ##eskisi yazmaz bu yazar artık
 #ayni sekilde tuple da gecerl,
      #dictionary
sehirler=["kocaeli","ist"]    
#plakalar=[41,34]
plakalar={"kocaeli": 41,"ist":34}
plakalar["ankara"]=6
#print(plakalar[sehirler.index("ist")]) 
print(plakalar["kocaeli"])
#print(plakalar)
ogrenciler={}

number = input("og no")
name = input("ogrenci name")
surname = input("ogrenci soyad")
phone = input("phone")

ogrenciler[number] = {


    "ad": name,
    "soyad": surname,
    "tel": phone
      
}
 
#ogrenciler.update ayni islevde
print(ogrenciler) 
