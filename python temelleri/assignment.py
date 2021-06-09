x,y,z =5,10,120
#x,y = y,x
x += 5
x -=5
x *=5
x /=5
x %=5
y**=4
values=1,2,5  #3den fazla ya da az olursa hata 
print(type(values))
x,y, *z=values
print(values)
print(x,y,z)
a,b,c,d = 5,5,10,4
password ='1234'
username = "ali"
result = (a==b)
print(result)
result = (a==c)
result="ali"
print(result)
vize1=float(input("1.vize: "))
vize2=float(input("2.vize: "))
fi=float(input("final"))
ort=((vize1+vize2/2*0.6)+(fi*0.4))
print(f"not ort:{ort}dersren gecme durumunuz: {ort>=50}")
sayi =int(input("sayi"))
tekcift=(sayi%2==0)
print(f"girilen sayi cift olma durumu: {tekcift}")
