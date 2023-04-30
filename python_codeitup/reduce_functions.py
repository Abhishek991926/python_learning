# reduce function take two value at a time
from functools import reduce
a=[]
for i in range(int(input("enter the range you want : "))):
    x=int(input("enter the list element :"))
    a.append(x)
print(a)  

def myFunc(a,b):
    return a+b

add=reduce(myFunc,a)
print("Addition =",add) 

# using lambda function 
add=reduce(lambda a,b:a+b,a)
print("Addition= ",add)