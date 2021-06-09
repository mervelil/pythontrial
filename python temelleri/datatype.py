name ="Merve"
surname="c"
age=36
print("my name is "+name+" "+surname+" and\nI am "+str(age)+" years old")
greeting = "my name is "+name+" "+surname+" and\nI am "+str(age)+" years old"
#print(greeting)
length =len(greeting)
print (greeting[0])
print(greeting[3])
print(greeting[length-1]) #0 dan basladigindan -1 yaptik
print(greeting[2:5])
print(greeting[3:])
print(greeting[:15])
print(greeting[2:40:3])#her harfi almaz


namee="cinar"
surname2 ="Turan"
age2=23
print("my name is {} {}".format(namee,surname2))
print("my name is {s} {n}".format(n=namee,s= surname2))
print("my name is {} {} and I'm {} years old.".format(namee,surname2,age2))

result1=200/700
print('The result is {} '.format(result1))
print('The result is {r: 1.3} '.format(r=result1))
print(f"my name is {namee} {surname2} and I'm {age2} years old.")