#A professor went to a party. Being an erudite person, he classified the party into two categories. He proposed that if all the persons in the party are wearing different colored robes, then that is a girl’s only party. If we even get one duplicate color, it must be a boy’s party. 
#The colors of the robes are represented by positive integers.
#Solution
from array import *
N=int(input("Enter the length of array"))
arr=array('i',[])
print("Enter the values of  array")
for i in range(N):
    x=int(input())
    arr.append(x)
for i in range(N-1):
    for j in range(i+1,N):
        if arr[i] == arr[j]:
            print('BOYS')
            break
    break

else:
    print('GIRLS')
