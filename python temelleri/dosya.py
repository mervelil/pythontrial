"""
file =open("newfile.txt","w") #obje bilgisi resultta
file.close()

file =open("newfile.txt","w",encoding="utf-8")
file.write("Merve Ç")
file.close()

#print(result) siliyo mevcutta bilgi varsa
"""
"""
file =open("newfile.txt","a",encoding="utf-8")
file.write("ada a")
file.close()
"""
try:
    file =open("newfile.txt","r",encoding="utf-8")
    print(file)
    for i in file:
        print(i,end="")
except FileNotFoundError:
    print("dosya okuma hatasi")
finally:
    print("maybe done...")

com =file.read()
print("icerik 1")
print(com)
com2=file.read()
print("icerik 2")
print(com2)
readi=file.read(3)
print(readi)
readin=file.read(6)
print(readin)
print(file.readline(),end="")
liste =file.readlines()

"""

    #with ile close yazmaya gerek kalmadi
    file.seek(4)
   
    print(file.tell())
    content =file.read()
    print(content)
"""
#r+ dosyayi hep acma hem okuma
with open("newfile.txt","r+",encoding="utf-8") as file:
    file.seek(20)
    file.write("dneeme")

with open ("newfile.txt","a",encoding="utf-8")as file:
    file.write("\nEmel Turan")
with open ("newfile.txt","r",encoding="utf-8") as file:
    content =file.read()
    content ="efe tyran"+content
    file.seek(0)
    print.write(content)
with open("newfile.txt","r+",encoding="utf-8") as file:
    list =file.readlines()
    list.insert(1,"Ali Korkmaz")
    file.seek(0)
    for i in list:
        file.write(i)
print(list)
