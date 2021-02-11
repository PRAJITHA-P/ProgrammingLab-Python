#Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly’
s=input("enter a string=")

if s[-3:]=="ing":
    print(s+"ly")
else:
    print(s+"ing")



