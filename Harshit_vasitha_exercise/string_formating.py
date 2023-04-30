# using string formation 

name="abhishek"
age=25
print("hello {} your age is {}".format(name,age)) # this string formating are use python 3.0

print(f" hello {name} your age is {age}") # this string formating are use python 3.6


#two or more input take in one line using split functions :

name,age=input("enter the name and age ").split()
print("hello {} your age is {}".format(name,age))
print(f"hello {name} your age is {age}")