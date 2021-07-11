#Given an array A of positive integers. Your task is to find the leaders in the array. An element of array is leader if it is greater than or equal to all the elements to its right side. 
#The rightmost element is always a leader. 
#Solution
from array import *
N=int(input("Enter the length of array"))
arr=array('i',[])
print("Enter the values of  array")
for i in range(N):
    x=int(input())
    arr.append(x)
ar=array('i',[])
max=arr[N-1]
ar.append(max)
for i in range(N-2,-1,-1):
    if arr[i]>=max:
        ar.append(arr[i])
        max=arr[i]
ar.reverse()
print(*ar, sep=" ")
