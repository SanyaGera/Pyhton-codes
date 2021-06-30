#Given a number, N. Find the sum of all the digits of N
#Solution
Number=int(input("Enter your number"))
N=str(Number) #Converting the integer number into String
Sum=0
for i in range(len(N)):
    Sum+=int(N[i])
print(Sum)
