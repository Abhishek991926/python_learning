# python program to find the frequency of a given numbers:

a=[]
for i in range(int(input("enter the range you want :"))):
    val=int(input("enter the list element  "))
    a.append(val)
print(a)
key=int(input("enter the number you want to count :"))
count=0
for i in range(len(a)):
    if(a[i]==key):
        count+=1

print("frequency of a given number is =",count)        
