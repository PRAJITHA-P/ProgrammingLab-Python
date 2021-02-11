"""Create a list of colors from comma-separated color names entered by user. Display
first and last colors."""
cname=input("enter the color names separated by comma=")
list1=cname.split(",")
print("first color=",list1[0])
print("last color=",list1[-1])