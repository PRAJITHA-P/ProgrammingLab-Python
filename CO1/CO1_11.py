#Find biggest of 3 numbers entered.

#method1
n1,n2,n3=[int(x) for x in input("enter 3 numbers=").split()]
print("Biggest number=",max(n1,n2,n3))

#method2
li=[n1,n2,n3]
li.sort()
print("Biggest number=",li[-1])