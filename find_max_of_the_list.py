# python program to find the max of the list:

a=[]
for i in range(int(input("enter the range you want : "))):
    val=int(input("enter the list elements :"))
    a.append(val)
print(a)

max=a[0]
for i in range(len(a)):
    if(a[i]>max):
        max=a[i]
print("max of the list=",max)        