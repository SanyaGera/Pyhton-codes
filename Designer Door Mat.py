#Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

#Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
#The design should have 'WELCOME' written in the center.
#The design pattern should only use |, . and - characters.
#Solution
N,M=map(int,input().split())

pattern=".|."
for i in range(1,((N//2)+1)):
    c=pattern*(2*i-1)
    print(c.center(M,"-"))
print("WELCOME".center(M,"-"))
for j in range(((N//2)+1),N):
    k=pattern*(2*(N-j)-1)
    print(k.center(M,"-"))
