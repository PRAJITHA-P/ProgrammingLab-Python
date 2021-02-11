#Accept a file name from user and print extension of that.
fname=input("Enter the filename with extension=")
li=fname.split(".")
print("file extension=" +li[-1])
