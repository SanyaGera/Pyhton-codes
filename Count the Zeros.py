#Given an array of size N consisting of only 0's and 1's.Find the count of all the 0's.
#Solution
from array import *
N=int(input("Enter the length of array"))
arr=array('i',[])
print("Enter the values of  array")
for i in range(N):
    x=int(input())
    arr.append(x)
Count=0
for i in range(N):
    if arr[i]==0:
        Count=Count+1
print(Count)
