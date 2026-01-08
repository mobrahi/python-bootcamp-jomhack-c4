# inheritance example
class Shape: # parent class
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

class Circle(Shape): # child inherits from Shape
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self): # override parent method
        return 3.14 * self.radius * self.radius

class Square(Shape): # child inherits from Shape
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self): # override parent method
        return self.side * self.side

# Both Circle and Square inherit 'name' attribute from Shape
circle = Circle(5)
square = Square(4)

print(circle.name)
print(square.name)
print("Circle area:", circle.area())
print("Square area:", square.area())

# Polymorphism example

def print_area(shape): # function takes a Shape object
    print(f"The area of the {shape.name} is {shape.area()}")

# same method call, different behavior
print_area(circle) # Circle's area method  
print_area(square) # Square's area method 

# or with a list of shapes
shapes = [Circle(2), Square(4), Circle(5)]
for shape in shapes:
    print_area(shape)

