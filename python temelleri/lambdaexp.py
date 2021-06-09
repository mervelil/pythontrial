def square (num): return num**2
#squ=lambda num :num**2
numbers =[1,3,5,9,2]


#result =list( map(lambda num:num**2,numbers))


result =list( map(square,numbers))
def check_even(num):  return num %2==0

result= list(filter(check_even,numbers))
"""
result= list(filter(lambda num: num %2==0,numbers))
for ite in map(square,numbers):
    print(ite)
    """
print(result)

x = "global x"
#x alttaki cx local o yuzden adı degıstırnmez
def function ():
    x ="local x"
function()
print (x)
##3###
name ="global"
def greeting():
    name ="cınaer"
    def hello():
        name ="ada"
        print("hello "+name)
    hello()
greeting()

x = 50
def test (x:
    print("x "+x)

    x=100
    print(f"changedx   to {x}")
test(x)
print(x)
