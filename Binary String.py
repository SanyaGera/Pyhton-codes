#Given a binary string S. The task is to count the number of substrings that start and end with 1. For example, if the input string is “00100101”, then there are three substrings 
#“1001”, “100101” and “101”.
#Solution
s=str(input("Enter the required string here"))
Count = 0
for i in range(len(s)):
    if s[i] == '1':
        Count += 1

ans = int(Count * (Count - 1) / 2)
print(ans)
