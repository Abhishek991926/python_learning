# dictionary in chngeable ,unordred collection of data 

# in a dictionary there are a key and there values :

dict1={'brand':'suzuki','model':'dzire','year':2020}
print(dict1)

# in a dictionary we want to print the only keys value use 

for x in dict1:
    print(dict1[x])

# we want tomprint only keys :

for x in dict1:
    print(x)    

# some other method we are use to print the keys :

for x in dict1.keys():
    print(x)

# some other method we want to print the keys values :
for x in dict1.values():
    print(x)   


# we want to print keys and values :

for x,y in dict1.items():
    print(x,y)     

# how to change the keys values :

x=dict1["year"]=2018
print(x)  

print(dict1)


# adding a new keys and their values in the dictionary 

dict1['satyam']='seth'
print(dict1)

# check a keys exist in a dictionary or not 

if "satyam" in dict1:
    print("present ")
else:
    print("not present")   