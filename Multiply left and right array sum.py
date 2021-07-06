#Pitsy needs help in the given task by her teacher. The task is to divide a array into two sub array (left and right) containing n/2 elements each and do the sum of the 
#subarrays and then multiply both the subarrays.
#Solution
from array import *
N=int(input("Enter the length of array"))
a=array('i',[])
print("Please enter the values of array")
for i in range(N):
    u=int(input())
    a.append(u)
Sum1=0
Sum2=0
Product=1
for i in range(N//2):
    Sum1=Sum1+a[i]
for j in range(N//2,N):
    Sum2=Sum2+a[j]
Product=Sum1*Sum2
print(Product)
