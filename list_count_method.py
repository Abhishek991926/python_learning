# code list count method 
# count method are count the frequency of element that are present in the list :

a=[]
for i in range(int(input("enter the range you want:"))):
    x=input("enter the list element :")
    a.append(x)
x1=input("enter the list element that you are count :")    
j=a.count(x1)
print("frequency of element is =" x1,j)