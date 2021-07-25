#You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
#Solution1
s=str(input("Enter your String here"))
p=list(s)
for i in range(len(s)):
  if p[i].isupper():
    p[i]=p[i].lower()
  else:
    p[i]=p[i].upper()
c=''.join(p)
print(c)

#Solution2
s=str(input("Enter your String here"))
c=s.swapcase()
print(c)
