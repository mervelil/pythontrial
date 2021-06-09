lsit=[1,2,3] #class instance =object  
#person claası var mesela age =semih.calculateAge(): bu instancefdir
resuly =type(lsit)
print(resuly)
class Person:
   # pass #yer tutar sınıfı tanımlatır
#attributes
    adress ="no info"
        #constructor method
    def __init__(self,name,year):
        self.name=name
        self.year=year
    print("ınıt calıstı")
#instance method
    def intro (self):
        print("hello there")
p22 =Person(name ="ahme",year =24)#nesne   
p1 =Person("ahme",24)#nesne
p1.intro()
print(f"name: {p1.name} year: {p1.year}adress:{p1.adress}")
print(type(p1))

class Circle:
    pi=3.24
    def __init__(self,r =1):
        self.r=r
    def cevre(self):
        return 2*self.pi*self.r
c1 =Circle()
c2 =Circle(3)
print(f"c1 cevre= {c2.cevre()}dir.")
