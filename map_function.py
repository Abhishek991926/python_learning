# using map function as iterator :
age=[]
for i in range(int(input("enter the range you want : "))):
    x=int(input("enter the age :"))
    age.append(x)
print(age)   
  
adults=list(filter(lambda x:x>18,age)) 
print(adults)

square=list(map(lambda a:a*a,adults))
print(square)            