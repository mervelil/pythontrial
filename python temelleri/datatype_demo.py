website="http://www.sadikturan.com"
course ="Python Kursu: Bastan Sona Python Programlama Rehberiniz (40 saat)"
length=len(course)
print(length-1)
print(website[7:10])
print(website[22:25])#length-3
print(course[0:15])#:15  ya da -15: diyebilirsin
print(course[length-15:length])
s ="12345" *5
print(s[::5])
print(course[::-1])

name="bora"
sname ="yilmaz"
yas=24
meslek="muhendis"
#yaz="benim adim {} {} yasim {} meslegim {}".format(name,sname,yas,meslek)
yaz=f"benim adim {name} {sname} yasim {yas} meslegim {meslek}"
print(yaz)
s= "Hello world"
s=s[0:6]+"W"+s[-4:]
print(s)
a="abc"*3
print(a)

message =" Hello There. My name is Buse Ak"
message=message.upper()
message=message.lower()
message=message.capitalize()
#message=message.title()
message=message.strip()
#message=message.split(".")
# message=message.split()
# message="---".join(message)
#indec=message.find('Buse')
isFound=message.endswith("k")
message=message.center(100)
message=message.replace(" ","*" )
print(isFound)
# print(indec)
print(message)