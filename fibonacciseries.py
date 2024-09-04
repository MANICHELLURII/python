n= int(input("enter number"))
a=0
b=1

if n<0:
    print("enter a positive integer")
else:
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(b)