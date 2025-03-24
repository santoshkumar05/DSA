# recursion - a function call by it self is called recursion.
# stack over flow - when a function runs infinte times until the stack is full is called the stack over flow.
"""def fact(n):
   if n==0:
    return 1;
   else:
    return n*fact(n-1)
def sum(n):
   if n==0:
    return 0;
   else:
    return n+sum(n-1)

def num(n):
 
    if n==0:
        return 0;
    else:
        print(9-n+1)
        return num(n-1)
    
print(sum(3))
print(fact(4))
num(9)
import numpy as np
var=[22,4,55,77]
arr=np.array(var)
print("original array:",arr)
def reverse(arr,start,end):
    if start>=end:
        return 
    arr[start],arr[end] = arr[end],arr[start]
    reverse(arr,start+1,end-1)
reverse(arr,0,len(arr)-1)
print("reversed array:",arr)"""
def f(n):
    if n<=1:
        return n;
    else:
        l= f(n-1);
        s = f(n-2);
    print(l + s);
f(4)