#Given a non-empty sequence of characters str, return true if sequence is Binary, else return false
#Solution
s=str(input("Enter the required string here"))
for i in range(len(s)):
    if s[i]!='0' and s[i]!='1' and s[i]!=' ':
        print(0)
        break
else:
    print(1)
