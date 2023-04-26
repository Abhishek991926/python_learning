# python program to search a element present in the list or not 

a=[]
for i in range(int(input("enter the range you want :"))):
    val=int(input("enter the list elements :"))
    a.append(val)
print("original list =",a)
key=int(input("enter the key you want to search in a list :"))
flag=0
for i in range(len(a)): 
    if(a[i]==key):
        flag=1
        pos=i+1
        break
if(flag==1):
    print("element is present",pos,"position")
else:
    print("element is not present in the list")       