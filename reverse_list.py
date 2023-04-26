# python program to reverse the list :

a=[]
for i in range(int(input("enter the range you want : "))):
    val=int(input("enter the list element :"))
    a.append(val)
print(a)

c=a.reverse()
print(c)