#Given a string S which consists of alphabets , numbers and special characters. You need to write a program to split the strings in three different strings S1, S2 and S3 such that
#the string S1 will contain all the alphabets present in S , the string S2 will contain all the numbers present in S and S3 will contain all special characters present in S.  
#The strings S1, S2 and S3 should have characters in same order as they appear in input.
#Solution
S=str(input("Enter the required string here"))
s1 = ""
s2 = ""
s3 = ""
for i in range(len(S)):
    if S[i].isalpha():
        s1 += S[i]
    elif S[i].isdigit():
        s2 += S[i]
    else:
        s3 += S[i]
print(s1, s2, s3)
