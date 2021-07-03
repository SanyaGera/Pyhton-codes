#For a given 3 digit number, find whether it is armstrong number or not. An Armstrong number of three digits is an integer such that the sum of the cubes of its
#digits is equal to the number itself. Return "Yes" if it is a armstrong number else return "No".
#NOTE: 371 is an Armstrong number since 3**3 + 7**3 + 1**3 = 371
#Solution
N=int(input("Enter your 3 digit number"))
Sum=0
S=str(N) #Convert the integer into string
for i in range(len(S)):
    j=int(S[i])
    Sum=Sum+j**3

if Sum==N:
    print("YES")

else:
    print("NO")
