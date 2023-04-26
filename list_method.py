# how to add data in a list :

l1=["apple","mango"]
l1.append("banana") # append method add the data in to the list in last position 
print(l1)

# when we want to add data in a list any position using insert method :

l1.insert(1,"chiki")
print(l1)

# how to concatenate a list 
l2=["orange","aman"]
l3=l1+l2
print(l3)

# using extend method same process will be done 
l1.extend(l2)
print(l1)

# we want to add the list inside the list use append method 
l1.append(l2)
print(l1)