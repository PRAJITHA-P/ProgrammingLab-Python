#From a list of integers, create a list removing even numbers.
li=[-5,-4,-3,-2,-1,0,1,2,3,4,5,6]
print(li)
print([x for x in li if x%2!=0])

#method2
for x in li:
    if x%2==0:
        li.remove(x)

print(li)