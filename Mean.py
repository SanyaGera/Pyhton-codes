#Given the marks of N students in an Array A, calculate the mean.
#Note: If result is a Decimal Value, find it's floor Value.
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
    Sum+=arr[i]
print("the required average is", Sum//n)
