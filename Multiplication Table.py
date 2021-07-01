#Print the multiplication table of a given number N
#Solution
from array import *
N=int(input("Enter the required number"))
table=array('i',[])
for i in range(1,11):
    x=N*i
    table.append(x)
print("here is the required multiplication table", *table,sep=' ')
