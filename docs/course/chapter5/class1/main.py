class Rectangle:
    width = 0.0
    length = 0.0

    def __init__(self, width, length) -> None:
        self.width = width
        self.length = length

    def area(self):
        a = self.width * self.length
        return a
    
    def perimeter(self):
        p = (self.width + self.length) * 2
        return p

# Create instance of the Rectangle class
rectangle = Rectangle()

# Print the attributes and computed values
print(f'The rectangle dimensions are W: {rectangle.width}, L: {rectangle.length}')
print(f'Area of the rectangle is: {rectangle.area()}')
print(f'Perimeter of the rectangle is: {rectangle.perimeter()}')
    