#Given an array Arr of size N, print all its elements.
#Solution
from array import *
N=int(input("Enter the length of array"))
arr=array('i',[])
print("Enter the values of  array")
for i in range(N):
    x=int(input())
    arr.append(x)
for i in range(N):
    print (arr[i],end=' ')
