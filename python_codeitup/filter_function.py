# filter function use as a iterator :

age=[12,15,17,22,24,26,28]

def myFunc(x):
    if x<18:
        return False
    else:
        return True
    
adults=list(filter(myFunc,age))

for x in adults:
    print(x)