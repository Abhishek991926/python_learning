#python program to find the sum of list element

a=[]
for i in range(int(input("enter the numbers :"))):
    x=int(input("enter the list element :"))
    a.append(x)
print(a)   
sum=0
for i in range(len(a)):
    sum=sum+a[i]
print("sum of list element = ",sum)     
