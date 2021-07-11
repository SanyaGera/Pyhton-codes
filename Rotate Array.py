#Given an unsorted array arr[] of size N, rotate it by D elements (clockwise).
#Solution
from array import *
N=int(input("Enter the length of array"))
D=int(input("Enter the value of D"))
arr=array('i',[])
print("Enter the values of  array")
for i in range(N):
    x=int(input())
    arr.append(x)
ar=array('i',[])
k=D
while k<=(N-1):
    ar.append(arr[k])
    k+=1
for p in range(D):
    ar.append(arr[p])
print(*ar, sep =' ')
