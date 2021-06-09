"""
import math

value =dir (math)
#help(math)
value =math.floor(5.9)
print (value)
"""
from math import *
value =factorial(5)
print(value)

import random 
result =random.random()
result=random.uniform(10,100)
print(result)
names =["aki", "se","ee"]
result = names[random.randint(0,len(names)-1)]
result=random.choice(names)
liste =list(range(10))
random.shuffle(liste)
result=liste
liste =range(100)
result =random.sample(liste,3)
print(result)


# my module
print("modul yazıldı")
numners=[1,2,3]
person ={
    "name": "Ali",
    "age": "45",
    "city": "ist"
}


