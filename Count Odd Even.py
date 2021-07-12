#Given an array A[] of N elements. The task is to count number of even and odd elements in the array.
#Solution
from array import *
N=int(input("Enter the length of array"))
arr=array('i',[])
print("Enter the values of  array")
for i in range(N):
    x=int(input())
    arr.append(x)
Odd=0
Even=0
for i in arr:
    if i%2==0:
	    Even+=1
    else:
	    Odd+=1
print(Odd, Even)
