#Find gcd of 2 numbers.
#method1
x=int(input("enter 1st number="))
y=int(input("enter 2nd number="))
i=1

while i<=min(x,y):
    if (x%i==0 and y%i==0):
         gcd=i
    i+=1

print(gcd)


#method2
import math
print(math.gcd(x,y))

