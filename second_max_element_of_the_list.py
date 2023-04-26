# python program to find the second max of the list element

a=[]
for i in range(int(input("enter the range you want : "))):
    val=int(input("enter the list element : "))
    a.append(val)
print(a)
a.remove(max(a))
smax=max(a)
print("second max element of the list =",smax)