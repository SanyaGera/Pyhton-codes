#Given an array Arr of N positive integers and a number K where K is used as a threshold value to divide each element of the array into sum of different numbers. 
#Find the sum of count of the numbers in which array elements are divided.
#Solution
from array import *
N=int(input("Enter the length of first array"))
K=int(input("Enter the value of K"))
Arr=array('i',[])
print("Please enter the values of first array")
for i in range(N):
    u=int(input())
    Arr.append(u)
div=1
Sum=0
for i in range(N):
    div=Arr[i]//K
    if Arr[i]%K==0:
        div=div+0
    else:
        div=div+1
        Sum+=div
print(Sum)
