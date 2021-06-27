#Problem
#Given a set of numbers from 1 to N, each number is exactly present twice so there are N pairs.
#In the worst-case scenario, how many numbers should be picked and removed from the set until we find a matching pair?
#Solution
N=int(input("Enter the number of pairs"))
print("Here are the number that should be picked and removed from the set until we find a matching pair")
if N==1:
    print(2)
else:
    print (N+1)
