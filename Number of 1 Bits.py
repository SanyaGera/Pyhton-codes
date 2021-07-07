#Given a positive integer N, print count of set bits in it
#Solution
N=int(input("Enter the integer"))
binary = bin(N)
Count = 0
for i in range(2, len(binary)):
    if binary[i] == "1":
        Count += 1
print(Count)
