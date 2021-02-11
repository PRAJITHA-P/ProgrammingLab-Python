#Generate all factors of a number.
n=int(input("Enter a number="))

print("the factors of the number=")
for x in range(1,n+1):
    if n%x==0:
        print(x," ",end="")