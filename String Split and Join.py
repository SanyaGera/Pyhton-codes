#You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
#Solution
line=str(input("Enter your string here"))
line=line.split(" ")
line="-".join(line)
print(line)
