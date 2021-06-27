#Given a positive integer n. Find the sum of product of x and y such that floor(n/x) = y 
#Solution
n=int(input("Enter the integer n"))
x=0 #intialise x
y=0 #initialise y
sum=0 #initialise sum
for i in range(1,n+1):
    x=i
    y=n//x
    c=x*y
    sum+=c
print(sum)
