# list is a data structure 
# we can store anything in a list 

l1=[1,2,3,4]
print(l1)

#in a list we can store intger ,floating number and string 

l2=[1,2,"abhishek",1.2,4.5]
print(l2)

# how to access list element :

l3=[1,2,3,4,5,6,"aman","satyam",1.2]
print(l3[6])

# how to assign a list element 
l3[5]="satyam"
print(l3)

l3[5:]=["aman","satyam"]
print(l3)

# how to add data in our list using append method :
# append method add the data in to the last of the list :

fruits=["mango","banana"]
fruits.append("kiwi")
print(fruits)

#using insert() method we are add the data give the position 

name=["aman","harshit"]
name.insert(0,"satyam")
print(name)

name.insert(1,"kumar")
print(name)

name.insert(2,"ankit")
print(name)

# how to concatenate two list 

l4=fruits+name
print(l4)

# using extend() method we are concatenate two list :

fruits.extend(name)
print(fruits)

# using append method() we are find list inside the list 
fruits.append(name)
print(fruits)