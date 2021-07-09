#Given an array Arr of N positive integers, find K largest elements from the array.  The output elements should be printed in decreasing order.
#Solution
from array import *
N=int(input("Enter the length of first array"))
K=int(input("Enter the value of k"))
Arr=array('i',[])
print("Please enter the values of first array")
for i in range(N):
    u=int(input())
    Arr.append(u)
ar=array('i',[])
Arr=sorted(Arr)
for i in range(K):
    ar.append(Arr[N-i-1])
print(*ar,sep=" ")
