my_list=[1,2,4]
message ="Hello there.My name is Merve".split()
my_list=["bir",2,True,5.6]
print(my_list)
list=["one","two","three"]
list2=["four","five","six"]
print(list2)
numbers =list+list2
print(numbers)
print(len(numbers))
print(message[0])
print(numbers[2])
userA =["Sadik ",36]
userB =["Cinar ",26]
print(userA)
#users =userA+userB
users =[userA,userB]
#print(users)
print(users[1][1])
#uygulama 
liste=["bmv","mercedes","opel","suv"]
print(len(liste))
lenf=len(liste)
print(liste[0])
print(liste[lenf-1])
liste[-1]="toyata"

result=liste
result="mercedes" in liste
print(result)
result=liste[-2]
print(result)
result=liste[:3]
print(result)
liste[-2:]=["totoya","renault"]
result=liste
print(result)
result=liste+["audi","nissan"]
del liste[-1]
result=liste
result=liste[::-1]
print(result)

studentA =["yigit","bilgi",2010,[70,80,85]]
studentB =["ali","TURAN",2010,[77,80,95]]
studentX =["emir","bilgi",2010,[90,80,95]]
result=f" {studentA[0]} {studentA[1]} {2019-studentA[2]} yasında ve not ortalamasi {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}"
print(result)
result=studentA[0]
result=studentB[1]
result=studentA[3][1]
print(result)

