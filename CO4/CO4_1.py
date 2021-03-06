"""Create Rectangle class with attributes length and breadth and methods to find area and
perimeter. Compare two Rectangle objects by their area."""
class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
    def perimeter(self):
        return 2*(self.breadth+self.length)

a=int(input("Enter length of rectangle 1: "))
b=int(input("Enter breadth of rectangle 1: "))
c=int(input("Enter length of rectangle 2: "))
d=int(input("Enter breadth of rectangle 2: "))

print()
obj1=rectangle(a,b)
obj2=rectangle(c,d)

print()
print("Area of rectangle1:",obj1.area())
print("perimeter of rectangle1:",obj1.perimeter())

print()
print("Area of rectangle2:",obj2.area())
print("perimeter of rectangle2:",obj2.perimeter())

print()
if (obj1.area()==obj2.area()):
   print("area of both rectangles are same")
elif obj1.area() > obj2.area():
   print("Area of First reactangle is greater ",obj1.area())
else:
   print("Area of Second reactangle is greater ",obj2.area())


