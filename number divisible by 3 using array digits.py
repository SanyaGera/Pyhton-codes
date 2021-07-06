#Given an array arr of integers of length N, the task is to find whether it’s possible to construct an integer using all the digits of these numbers such that it would be divisible by 3.
#If it is possible then print “1” and if not print “0”.
#Solution
from array import *
N=int(input("Enter the length of array"))
a=array('i',[])
print("Please enter the values of array")
for i in range(N):
    u=int(input())
    a.append(u)
y=str()
for i in a:
    y=y+str(i)
n=int(y)
if n%3==0:
    print(1)
else:
    print(0)
