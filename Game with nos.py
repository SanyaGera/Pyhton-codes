#You are given an array arr[], you have to re-construct an array arr[].
#The values in arr[] are obtained by doing Xor of consecutive elements in the array.
#Solution
from array import *
N=int(input("Enter the length of array"))
arr=array('i',[])
print("Please enter the values of array")
for i in range(N):
    x=int(input())
    arr.append(x)
ar=array('i',[])
for i in range(len(arr)):
    if i==len(arr)-1:
        x=arr[i]
    else:
        x=arr[i]^arr[i+1]
    ar.append(x)
print(*ar,sep=" ")
