#You are given two arrays, A and B, of equal size N. The task is to find the minimum value of A[0] * B[0] + A[1] * B[1] +…+ A[N-1] * B[N-1], where shuffling of 
#elements of arrays A and B is allowed.
#Solution
from array import *
N=int(input("Enter the length of arrays"))
A=array('i',[])
print("Please enter the values of first array")
for i in range(N):
    u=int(input())
    A.append(u)
B = array('i', [])
print("Please enter the values of second array")
for i in range(N):
    u = int(input())
    B.append(u)
Sum = 0
A=sorted(A)
B=sorted(B)

for i in range(N):
    Prod = A[i] * B[N-1-i]
    Sum = Sum + Prod
print(Sum)
