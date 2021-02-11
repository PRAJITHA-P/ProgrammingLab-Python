#Accept a list of words and return length of longest word
li=[]
m=[]
for x in range(0,4):
    w=input("enter the word=")
    m.append(len(w))
    li.append(w)
print(li)
print("length of longest word=",max(m))
