# take two comma seprated input from user :
# 1) user`s name 
# 2) a single charcter 

# output will be 2 
# user name lenghth 
# count the charcter the user input 

name,char=input("enter the name and char comma seprated  ").split(",")
print(f" length of the name is {len(name)}")
print(f" count the char : {name.lower().count(char.lower())}")