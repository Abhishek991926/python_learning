# filter odd even 
# define a function 
# input .......>[1,2,3,4,5,6,7,8]
# output .......>[[1,3,5,7],[2,4,6,8]]

l1=[1,2,3,4,5,6,7,8]
l2=[]
l3=[]
l4=[]
for i in l1:
    if(i%2==0):
        l2.append(i)

    else:
        l3.append(i)
l4.append(l2)
l4.append(l3)
print(l4)

# using function 

def filter_odd_even(l):
    even=[]
    odd=[]
    for i in l:
        if(i%2==0):
            even.append(i)
        else:
            odd.append(i)
    return [odd,even]

l2=list(range(1,int(input("enter the range you want : ")))) 
print(filter_odd_even(l2))               
     
