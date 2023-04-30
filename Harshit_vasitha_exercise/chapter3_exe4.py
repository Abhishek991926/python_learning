# input user name and count each words:

name=input("enter the name :")
tem_var=""
i=0
while len(name)>i:
    if name[i] not in tem_var:
        tem_var+=name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i+=1