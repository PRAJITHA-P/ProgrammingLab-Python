#Generate Fibonacci series of N terms
n=int(input("Enter the limit="))
f=0
s=1
t=1

if n>=1:
   print(f)
if n>=2:
   print(s)

for x in range(3,n+1):
    print(t)
    f=s
    s=t
    t=f+s