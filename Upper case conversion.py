#Given a string str, convert the first letter of each word in the string to uppercase. 
#Solution
s=str(input("Enter the required string here"))
s = list(s)
s[0] = s[0].upper()
for i in range(1, len(s)):

    if s[i - 1] == ' ':
        s[i] = s[i].upper()
s1 = ""
print(s1.join(s))
