n=int(input("enter number"))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("the reverse of given number is:",rev)