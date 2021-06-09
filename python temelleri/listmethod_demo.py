names=["ali","yagmur","hakan","deniz"]
years=[1998,1999,2000,1987]
names.append("cenk")

names.insert(0,"sena")
result=names.index("deniz")
#names=insert(len(names),"mehmet")
names.pop(result)

result2="ali" in names
#names.remove("deniz")
names.reverse()
names.sort()
print(result2)
print(names)
years.sort()
print(years)
str="chev.dacia"
result=str.split(",")
min=min(years)
max=max(years)
a= years.count(1998)
years.clear()
print(max)
print(a)
print(years)
markalar =[]
marka =input("marka: ")
markalar.append(marka)
marka =input("marka: ")
markalar.append(marka)
marka =input("marka: ")
markalar.append(marka)
print(markalar)