#Given an array, rotate the array by one position in clock-wise direction.
#Solution
from array import *
n=int(input("Enter the length of array"))
arr=array('i',[])
print("Please enter the values of array")
for i in range(n):
    y=int(input())
    arr.append(y)
x = arr[n - 1]
for i in range(n - 1, 0, -1):
    arr[i] = arr[i - 1]
arr[0] = x
print(*arr,sep=" ")
