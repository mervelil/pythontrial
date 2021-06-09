website="http://www.sadikturan.com"
course ="Python Kursu: Bastan Sona Python Programlama Rehberiniz (40 saat)"
#" Hello World " str bastaki ve sondaki string karakteri silin.
result = " Hello World ".strip()
result = " Hello World ".lstrip()
result = " Hello World ".rstrip()
result= website.lstrip("/:pth")
#www.sadikturan.com  sadikturan harici bilgileri silin
result="www.sadikturan.com".strip("w.com")
print(result)
#"webiste" icinde kac tane a harfi vardir
result =website.count("a")
result =website.count("www")
result =website.count("www",0,10)
print(result)
#website  icinde wwww baslatip .com ile biten varmi
result=website.startswith("www")

result=website.endswith(".com")
print(result)
#website icinde com ile biten ifade varmi
result= website.find("com")
result= website.find("com",0,10)
result=course.find("Python")
result=course.rfind("Python")

result=website.index("com")
#print =22
result=website.rindex("com")
#print =22
#result=website.rindex("comm")
#print(result)
#course icindeki karaktrler hepsi alfabetik mi 
result=course.isalpha()
result="Hello".isalpha()
result=course.isdigit()
result="12345".isdigit()
print(result)
#contents  ifadesini satirda 50 karakter icine yerlestirip sag ve soluna ekle
result="contents".center(50)
result="contents".center(50,"*")
result="contents".ljust(50,"*")
result="contents".rjust(50,"*")
print(result)
#course stringini tum bosluk karakterlerini "-" ile degistirin 
result=course.replace(" ","-")
result=course.replace(" ","-",5)
result=course.replace(" ","")
result="Hello World".replace("World","there")
print(result)
#course bpsluk karakterinden ayirin
result=course.split(" ")
result=result[2]
print(result)



