#Given an array arr representing heights of buildings. You have to count the buildings which will see the sunrise (Assume : Sun rise on the side of array starting point).
#Solution
from array import *
N=int(input("Enter the length of array"))
arr=array('i',[])
print("Enter the values of  array")
for i in range(N):
    x=int(input())
    arr.append(x)
max=arr[0]
Count=1
for i in range(1,N):
    if arr[i]>max:
        Count=Count+1
        max=arr[i]
print(Count)
