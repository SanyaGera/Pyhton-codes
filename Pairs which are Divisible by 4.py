#Given an array, if ‘n’ positive integers, count the number of pairs of integers in the array that have the sum divisible by 4.
#Solution
from array import *
N=int(input("Enter the length of array"))
arr=array('i',[])
print("Enter the values of  array")
for i in range(N):
    x=int(input())
    arr.append(x)
l=list(0 for i in range(4))
for j in range(N):
    l[arr[j]%4]+=1
ans=l[2]*(l[2]-1)//2+l[0]*(l[0]-1)//2+l[1]*l[3]
print(ans)
