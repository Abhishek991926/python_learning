# sort method sort the element in ascending order or decendimg order :

a=[]
for i in range(int(input("enter the range you want : "))):
    x=int(input("enter the list element : "))
    a.append(x)
print(a)

a.sort(reverse=False)
print(a)