# python program to find the min value in a lsit :

a=[]
for i in range(int(input("enter the range you want : "))):
    val=int(input("enter the value of the list :"))
    a.append(val)
print(a)
min=a[0]
for i in range(len(a)):
    if(a[i]<min):
        min=a[i]
print("min of the list = ",min)            