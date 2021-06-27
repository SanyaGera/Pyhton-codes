#Midori like chocolates and he loves to try different ones. There are N shops in a market labelled from 1 to N and each shop offers a different variety of chocolate.
#Midori starts from ith shop and goes ahead to each and every shop. But as there are too many shops Midori would like to know how many more shops he has to visit.
#You have been given L denoting number of bits required to represent N. You need to return the maximum number of shops he can visit.
#Solution
L=int(input("Enter the number of bits of N shops Midori vists"))
i=int(input("Enter the shop she is at"))
print("No.of shops left")
print(2**L-i)
#2**L gives the integer where L are the number of bits
