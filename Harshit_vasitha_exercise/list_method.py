# common method are use how to delete the data from a list :
fruits=["mango","banana","orange","grapes"]
print(fruits.pop()) # pop() method are return the data
print(fruits) 

fruits.pop(1)
print(fruits)

# del method 
fruit1=["mango","banana","orange","kiwi"]
del fruit1[1]
print(fruit1)


# remove() 
fruit2=["apple","kiwi","banana","orange"]
fruit2.remove("banana")
print(fruit2)

# in keyword  are use to check element present in the list :

fruit3=["apple","banana","kiwi","orange","`mango"]
if "orange" in fruit3 :
    print("present")
else:
    print("not present")  


# count() this method are used the check the list element frequency 
fruit4=["apple","mango","apple","orange","banana"] 
print(fruit4.count("apple"))   

# sort() this method are use to arrange the list element in alphabetical order:

fruit4.sort()
print(fruit4)

# sorted() function this will be generated sorted list original list will not be short :

l5=[1,2,56,4,3]
print(sorted(l5))
print(l5) 

# clear() this method are use the clear the list :

l5.clear()
print(l5)

# copy() this method generate the copy of the list 

l6=[1,2,3,4,5]
copy_list=l6.copy()
print(copy_list)

#split() this method are use convert string in to list :

name="abhishek, 24".split() 
print(name)


# join() method  this method are use convert list in to string 

l1=["abhishek","23"]
print(",".join(l1)) 