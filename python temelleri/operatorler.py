x=45
result =(x>5 ) and (x<10)
result=(x >5 ) or (x%2==0)
print(result)
sayi =int(input("sayi: "))
result =(sayi>0) and (sayi%2==0)
print (f"cift mi {result}")
name =input("adınız")
kg =float(input("kılo"))
hg =float(input("boy"))
index =(kg)/(hg**2)
"""
zayif =(index>=0)and (index<=18.4)

normal = (index>18.4)and (index<34.4)
kilolu = (index>35.4)and (index<39.4)
obez = (index>40.4)and (index<43.4)

print(f"{name} kilo indexin zayif {zayif}")
print(f"{name} kilo indexin normal {normal}")
print(f"{name} kilo indexin kilolu {kilolu}")
print(f"{name} kilo indexin obez {obez}")
"""
if (index>=0)and (index<=18.4) :
    print(f"{name} kiloindeksin: {index} ve zayif ")
elif  (index>35.4)and (index<39.4):
    print(f"{name} kilo indexin normal {index}")
elif (index>35.4)and (index<39.4):
    print(f"{name} kilo indexin kilolu {index}") 
elif(index>40.4)and (index<43.4):
 print(f"{name} kilo indexin obez {index}")   

 xa  = [1 ,2 ,3]
 y = [1 ,2 ,3]
 xa =y
 z =[1,2,3]
print(xa==y )
print(xa==z )
print(xa is not y )

print(xa is z )

x =["apple ", "banana"]
print("banana " not  in x)
print("banana "   in x)
