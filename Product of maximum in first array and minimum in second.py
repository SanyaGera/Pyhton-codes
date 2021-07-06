#Given two arrays of A and B respectively of sizes N1 and N2, the task is to calculate the product of the maximum element of the first
#array and minimum element of the second array.
#Solution
from array import *
N1=int(input("Enter the length of first array"))
A=array('i',[])
print("Please enter the values of first array")
for i in range(N1):
    u=int(input())
    A.append(u)
N2=int(input("Enter the length of second array"))
B=array('i',[])
print("Please enter the values of second array")
for i in range(N2):
    u=int(input())
    B.append(u)
Max=max(A)
Min=min(B)
Product=Max*Min
print(Product)
