"""
print(a) name error
int ("12a) value error 
10/0 zerodivision eror
"deneme"w syntax eroro
"""
while True:
    try:
        x =int(input("x: "))
        y =int(input("y: "))
        print(x/y)
    except ZeroDivisionError:
        print ("y icin 0 olmaz") 
    except ValueError:
        print("sayi girmelisin")
    else:
        print("her sey yolunda")
        break

    finally:
        print("somnlandi")

"""
e =10
if e>5:
    raise Exception("x 5 den buyuk olamaz")
"""
def check(psw):
    import re
    if len(psw) < 8:
        raise Exception("parolo en az 7char icermeli.")
    elif not re.search("[a-z]",psw):
        raise Exception("parolo kucuk harf icermeli.")
    elif not re.search("[A-Z]",psw):
        raise Exception("parolo byk  harf icermeli.")

password ="122456"
try:
    check(password)
except Exception as ex:
    print(ex)
else:
    print("geecrli")
    """
class P:
    def __init__(self,name,year):
        if len(name) >10:
            raise Exception ("name alanı fazla karakter iceriyor")
        else:
            self.name=name
p =P ("ALİİİİİİİİİİİİİİİİİİİİİİİ",1345)    
"""   
""" 
liste = [1,2,3,6,8,"5a","10","abc"]
    for a in liste:5
       try:
           result =int (a)
           print(result)
       except ValueError:
           continue
    """
"""
while True:
    print(sayi =input("Sayi: "))
    if sayi =="q":
        break
    try: 
        result =float(sayi)
    except:
        print("gecrsiz")
        continue
        """