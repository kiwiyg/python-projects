import random
import time

def naive_search(l, target):
    # example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    
    midpoint = (low + high) // 2  

    
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        return binary_search(l, target, midpoint+1, high)


x=[]
y=int(input("Enter the length of the array: "))
i=0
while(i<y):
    f=int(input(f"{i} : "))
    x.append(f)
    i=i+1

sorted_list=sorted(list(x))
m=int(input("Enter the value to be searched: "))
z=int(input("Do you want to run a Naive search(0) or a Binary search(1)? : "))
if(z==1):
    print(binary_search(sorted_list, m))
else:
    print(naive_search(sorted_list, m))