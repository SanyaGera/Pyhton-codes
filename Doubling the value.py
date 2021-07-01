#Given an array and an integer B, traverse the array (from the beginning) and if the element in array is B, double B and continue traversal.
#Find the value of B after the complete traversal.
#Solution
from array import *
n=int(input("Enter the length of array"))
arr=array('i',[])
print("Enter the values of array")
for i in range(n):
    x=int(input())
    arr.append(x)
b=int(input("Enter b"))
for i in range(n):
    if arr[i]==b:
        b=b*2
print(b)
