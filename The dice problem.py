#You are given a cubic dice with 6 faces. All the individual faces have a number printed on them. 
#The numbers are in the range of 1 to 6, like any ordinary dice. You will be provided with a face of this cube, your task is to guess the number on the opposite face of the cube.
#6 is opposite to 1
#5 is opposite to 2
#4 is opposite to 3
#Solution
N=int(input("Enter the number on the dice"))
print("The opposite number on the dice is")
if N==6:
    print(1)
elif N==1:
    print(6)
elif N==5:
    print(2)
elif N==2:
    print(5)
elif N==3:
    print(4)
else:
    print(3)
