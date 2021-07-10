#You are given an integer n. You need to convert all zeroes of n to 5.
#Solution
n=int(input("Enter your number"))
N=str(n) #Conversion of integer to string
N=N.replace('0','5')
n=int(N)
print("Output: ",n)
