#Given an integer array Arr[] of size N. The task is to find sum of it.
#Solution
from array import *
n=int(input("Enter the length of array"))
arr=array('i',[])
print("Enter the values of array")
for i in range(n):
    x=int(input())
    arr.append(x)
Sum=0
for i in range(n):
    Sum=Sum+arr[i]
print(Sum)
