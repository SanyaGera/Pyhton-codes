#Given a string consisting of lowercase english alphabets, reverse only the vowels present in it and print the resulting string.
#Solution
s=str(input("Enter the required string here"))
i = 0
j = len(s) - 1
while (i < j):
    c = s[i]
    if not (c == 'a' or c == 'A' or c == 'e' or
            c == 'E' or c == 'i' or c == 'I' or
            c == 'o' or c == 'O' or c == 'u' or
            c == 'U'):
        i += 1
        continue
    x = s[j]
    if not (x == 'a' or x == 'A' or x == 'e' or
            x == 'E' or x == 'i' or x == 'I' or
            x == 'o' or x == 'O' or x == 'u' or
            x == 'U'):
        j -= 1
        continue
    else:
        s = list(s)
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
s2 = ""
print(s2.join(s))
