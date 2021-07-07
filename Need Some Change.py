#Given an array arr of n positive integers. The task is to swap every ith element of the array with (i+2)th element.
#Solution
from array import *
N=int(input("Enter the length of first array"))
Arr=array('i',[])
print("Please enter the values of first array")
for i in range(N):
    u=int(input())
    Arr.append(u)
for i in range(2, N):
    x = Arr[i - 2]
    Arr[i - 2] = Arr[i]
    Arr[i] = x
print(*Arr, sep=" ")
