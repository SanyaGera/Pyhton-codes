#Given a positive integer n, check if it is perfect square or not.
#Solution
a=int(input("Enter the number"))
if a**.5==int(a**.5):
    print("perfect square")
else:
    print("not a perfect square")
