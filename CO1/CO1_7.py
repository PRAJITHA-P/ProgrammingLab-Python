"""Enter 2 lists of integers. Check (a) Whether list are of same length (b) whether list sums
to same value (c) whether any value occur in both"""
l1=[2,4,6,7,8]
l2=[7,44,5,7,9]

print(l1)
print(l2)

#(a)Check Whether list are of same length
if len(l1)==len(l2):
    print("list are of same length")
else:
    print("List are not of same length")


#check whether list sums to same value (c) whether any value occur in both"""
if sum(l1)==sum(l2):
    print("List are of same sum")
else:
    print("List are not of same sum")

#check  whether any value occur in both
l3=[x for x in l1 if x in l2]
if len(l3)<1:
    print("No value occure in both")
else:
    print("common values:",l3)