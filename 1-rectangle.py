class Rectangle:
    def __init__(self ,breadth, length):
        self.breadth = breadth
        self.length = length
    def area(self):
        return self.breadth * self.length
    def perimeter(self):
        return 2 * (self.breadth + self.length)
print("Rectangle 1")
a=int(input("enter the length:"))
b= int(input("enter the breadth:"))
rect1=Rectangle(a,b)

print("Area  = ",rect1.area())
print("Perimeter = ",rect1.perimeter())

print("Rectangle 2")
a=int(input("enter the length:"))
b= int(input("enter the breadth:"))
rect2=Rectangle(a,b)

print("Area 2= ",rect2.area())
print("Perimeter=",rect2.perimeter())

if  rect1.area() > rect2.area():
    print("Rectangle 1 has larger area")
elif rect1.area() < rect2.area():
    print("Rectangle 2 has larger area")
else:
    print("Area equal")