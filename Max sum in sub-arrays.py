#Given an array, find maximum sum of smallest and second smallest elements chosen from all possible sub-arrays. More formally, if we write all (nC2) sub-arrays of array of size >=2 and find the sum of smallest and 
#second smallest, then our answer will be maximum sum among them.
#Solution
from array import *
N=int(input("Enter the length of array"))
arr=array('i',[])
print("Enter the values of  array")
for i in range(N):
    x=int(input())
    arr.append(x)
res=arr[0]+arr[1]
for i in range(1,N-1):
    res=max(res,arr[i]+arr[i+1])
print(res)
