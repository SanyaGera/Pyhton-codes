#Given a string S, write a program to count the occurrence of Lowercase characters, Uppercase characters, Special characters and Numeric values in the string.
#Note: There are no white spaces in the string.
#Solution
s=str(input("Enter the required string here"))
Upper = 0
Lower = 0
Special = 0
Numeric = 0
for i in range(len(s)):
    if s[i].isupper():
        Upper += 1
    elif s[i].islower():
        Lower += 1
    elif s[i].isdigit():
        Numeric += 1
    else:
        Special += 1
print(Upper, Lower, Numeric, Special)
