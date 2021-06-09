class Person():
    def __init__(self,fn,ln):
        self.fin =fn
        self.lst=ln
        print("person created")
    def eat (self):
        print("I sm eating")
class Student(Person):
     def __init__(self,fn,ln,nimber):
        Person.__init__(self,fn,ln)
        self.num =nimber
        #super().init(fname,lame) self gerek yok super yazinca
        print("stu")
    #overrride
     def eat (self):
        print("I sm eating too")

p1= Person("maya", "ak")

s1= Student("ali","kul","12345")
print(p1.fin +" "+ p1.lst)
print(s1.fin +" "+ s1.lst+s1.num +" "+s1.num)
s1.eat()

class Q:
    def __init__ (self,text,cho,ans):
        self.text=text
        self.cho=cho
        self.ans=ans 
    def check(self,ans):
        return self.ans==ans
 
class Qi:
    def __init__(self,q):
        self.ques=q
        self.score =0
        self.qi=0
    def get (self):
        return self.ques[self.qi]
    def display (self):
       question =self.get()
       print(f"soru{self.qi+1}: ")

       for q in quest.cho:
           print("-"+q)
       answer =input("cevap ")
       self.guess(answer)
       self.load()
    def guess(self,answer):
        question =self.get()
        if ques.check(answer):
           self.score +=1
        self.qi +=1
     
    def load (self):
        if len(self.ques)==self.qi:
            print("veri yeterli")
            

q1 =Q("en iyi dil hangisi",["c","python","java"],"python")
q2 =Q("en populer dil hangisi",["c","python""java"],"python")
q3 =Q("en eglenceli dil hangisi",["c","python","java"],"python")
liste4=[q1,q2,q3]
quiz =  Qi(liste4)
questi=quiz.get()
de=display()
