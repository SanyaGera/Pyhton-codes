#Task
#Given an integer,n , perform the following conditional actions:

#If n is odd, print Weird
#If n is even and in the inclusive range of 2 to 5 , print Not Weird
#If n is even and in the inclusive range of 6 to 20 , print Weird
#If n  is even and greater than 20 , print Not Weird
#Solution
n = int(input("Enter the required number"))
if n%2!=0:
  print("Weird")
elif n%2==0 and 2<=n<=5:
  print("Not Weird")
elif n%2==0 and 6<=n<=20:
  print("Weird")
else:
  print("Not Weird")