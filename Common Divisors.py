#Given two integer numbers a and b, the task is to find count of all common divisors of given numbers.
#Solution
a=int(input("Enter th first number"))
b=int(input("Enter the second number"))
Count=0
for i in range(1,(b//2)+1): #because all the divisors of a particular number to be found can be found till its half
    if a%i==0 and b%i==0:
        Count+=1

print(Count)
