n=int(input("enter a number:"))
temp=n
rev=0
while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10
if (temp==rev):
    print(f"{temp} is a palindrome")
else:
    print(f"{temp} is not a palindrome")