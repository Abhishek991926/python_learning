# using reduce function find the max of the list :
from functools import reduce
l1=[]
for i in range(int(input("enter the range you want : "))):
    x=int(input("enter the list element :"))
    l1.append(x)
print(l1)

def maxFunc(a,b):
    if a>b:
        return a
    else:
        return b
    
max=reduce(maxFunc,l1)
print("max =",max)    


# using lambda function :

max=reduce(lambda a,b:a if a>b else b,l1)
print("Max=",max)