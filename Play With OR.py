# You are given an array arr[], you have to re-construct an array arr[].
#The values in arr[] are obtained by doing OR(bitwise or) of consecutive elements in the array.
#Solution
from array import *
print("please enter the lenght of array")
n=int(input())
print("please enter the values of array")
arr=array('i',[])
for i in range(0,n):
    x=int(input())
    arr.append(x)
ar=list(0 for i in range(len(arr))) #create a new list for OR values of the previous list
for i in range(len(arr)):
    if i==len(arr)-1:
        ar[i]=arr[i] #the last number will remain the same
    else:
        ar[i]=arr[i]|arr[i+1]
print("here is the new array", ar)
