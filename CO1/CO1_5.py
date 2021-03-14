#Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead

lst = []
lst = [int(item) for item in input("Enter the list items : ").split()]
print("INPUT IS", lst)
x = ["over" if x > 100 else x for x in lst]
lst = list(x)
print(lst)
