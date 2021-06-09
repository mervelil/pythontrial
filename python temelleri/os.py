import os 
result =os.name
result =os.getcwd()
#os.rename("newdır","yeniklasor")
#os.chdir("do") #bigisayarda
#os.mkdir("newdır") #visualda yeni clasor olusturuldu
#os.makedirs("newdir/yenikl") #icine baska clasor
result =os.listdir("C:\\")
for dosya in os.listdir():
    if dosya.endswith(".py"):
        print(dosya)
os.system("notepad.exe")

#path

result =os.path.abspath("os.py")
result=os.path.dirname(os.path.abspath("os.py"))
result =os.path.exists("os.py")
result =os.path.split("C:\\deneme")
result =os.path.splitext("os.py")
result=result[0]
print(result)