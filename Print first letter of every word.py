#Given a string S, the task is to create a string with the first letter of every word in the string.
#Solution
S=str(input("Enter the required string here"))
s1 = ""
s1 = s1 + S[0]
for j in range(1, len(S) - 1):
    if S[j] == ' ':
        s1 += S[j + 1]
print(s1)
