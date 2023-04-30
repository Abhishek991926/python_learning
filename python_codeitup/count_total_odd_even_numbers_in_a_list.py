# python program to count total odd and even numbers in a list :

a=[]
for i in range(int(input("enter the range you want : "))):
    x=int(input("enter the list elements :"))
    a.append(x)
print("original list =",a) 
even=0
odd=0 
for i in range(len(a)):
    if(a[i]%2==0):
        even+=1
    else:
        odd+=1
print("total even number= ",even)
print("total odd number =",odd)            