fruits={'orange','apple','banana'}
print(fruits)#indexle elemana ulasamazsın sette

for x in fruits :
    print(x)
fruits.add('cherry')
fruits.update(['mango','moon'])#olan eleman listeye eklenmez
fruits.discard('mango')
fruits.remove('apple')
fruits.pop()
print(fruits)
my_list=[1,2,3,5,67,5,5,2]
print(my_list)
print(set(my_list))
#value types
X=5
y=2345
x=y
y=10
#print(x,y)
#referance type list
a=["apple","banana"]
b=["apple","banana"]
a=b
b[0]="mango"
print(a,b)