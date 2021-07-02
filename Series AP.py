#Given the first 2 terms A1 and A2 of an Arithmetic Series.Find the Nth term of the series. 
#Solution
A1=int(input("Enter the first term of AP"))
A2= int(input("Enter the second term of AP"))
N=int(input("Enter the term you want"))
d=A2-A1 #CCommon difference
x= A1+(N-1)*d
print("Here is the nth term", x)
