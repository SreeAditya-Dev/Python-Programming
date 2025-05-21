num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

def max():
    l=0
    for i in [num_1,num_2,num_3]:
        if i>l:
            l=i
    return l

def min():
    l=num_1
    for i in [num_1,num_2,num_3]:
        if i<l:
            l=i
    return l

print("sum of three number:",num_1+num_2+num_3)
print("max of three number:",max())
print("min of three number:",min())
