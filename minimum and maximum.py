#Given an array A of size N of integers. Your task is to find the minimum and maximum elements in the array.
#Solution
from array import *
N=int(input("Enter the length of array"))
a=array('i',[])
print("Please enter the values of array")
for i in range(N):
    y=int(input())
    a.append(y)
Min=min(a)
Max=max(a)
print("Maximum: ",Max)
print("Minimum: ",Min)
