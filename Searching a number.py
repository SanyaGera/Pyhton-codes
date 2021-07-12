#Given an array Arr of N elements and a integer K. Your task is to return the position of first occurence of K in the given array.
#Note: Position of first element is considered as 1.
#Solution
from array import *
N=int(input("Enter the length of array"))
k=int(input("Enter the value of k"))
arr=array('i',[])
print("Enter the values of  array")
for i in range(N):
    x=int(input())
    arr.append(x)
x=-1
for i in range(N):
    if arr[i]==k:
        x=i+1
        break
print(x)
