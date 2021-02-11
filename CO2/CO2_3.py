#Find the sum of all items in a list
li=input("enter the numbers separated with commas=")
li1=li.split(",")

#method1
s=0
print("list elements are...")
print(li1)

for x in li1:
    s=s+int(x)
print("sum of all items in a list=",s)

#method2
list = [54,89,66,32,74]
print("another list=",list)
print("Sum of List : "+ str(sum(list)))
