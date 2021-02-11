#Print out all colors from color-list1 not contained in color-list2.
clrli1=["violet","yellow","blue","white","black"]
clrli2=["violet","black","orange","green","yellow"]

#method1
print(clrli1)
print(clrli2)
print("all colors from color-list1 not contained in color-list2")
print([x for x in clrli1 if x not in clrli2])

#method2
s1=set(clrli1)
s2=set(clrli2)
s3=s1.difference(s2)
print("all colors from color-list1 not contained in color-list2")
print(list(s3))