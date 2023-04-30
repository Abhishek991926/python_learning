# how to add data in a tuple 

# answer is we can not add the data in tuple because tuple are immutable :

# but some method use we can add data in a tuple ;

tuple1=("ram","shyam","gita")
print(tuple1)

y=list(tuple1)
y.append("mango")
z=tuple(y)
print(z)

# how to determine the specific element is present in the tuple or not 
# using in keywords :

tuple2=("banana","mango","orange","kiwi")
if "kiwi" in tuple2:
    print("present ")
else:
    print("not present")    


# use del keyword we can delete all the tuple 

z=("aman","satyam","abhi") 
print(z)  