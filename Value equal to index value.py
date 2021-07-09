#Given an array Arr of N positive integers. Your task is to find the elements whose value is equal to that of its index value.
#Solution
from array import *
N=int(input("Enter the length of first array"))

Arr=array('i',[])
print("Please enter the values of first array")
for i in range(N):
    u=int(input())
    Arr.append(u)
ar=array('i',[])
for i in range(N):
	if Arr[i]==(i+1):
		ar.append(Arr[i])
print(*ar,sep=" ")
