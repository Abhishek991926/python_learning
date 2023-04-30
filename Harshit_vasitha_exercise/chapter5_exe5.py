# common element finder :
# define a function which take 2 list as a input and return a list :
# which contains common element in both list :
# example [1,2,5,8] [1,2,7,6]  output ...>[1,2]

l1=[1,2,3,4,5,6]
l2=[1,2,7,8,9,10]
l3=[]
for i in l1:
    if i in l2:

        l3.append(i)

print(l3)  

def common_element_finder(l1,l2):
    l3=[]
    for i in l1:
        if i in l2:
            l3.append(i)

    return l3

l1=[1,2,3,4,5,6]
l2=[1,2,7,8,9,10]
print(common_element_finder(l1,l2))            