class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self, length, width):
        Result = (self.length + self.width) * 2
        return Result

    def surface(self, length, width):
        area = (self.length * self.width)
        return area


perimeters = []
areas = []
for i in range(2, 10):
    Rectangle1 = Rectangle(i * 2, i)
    perim = Rectangle1.perimeter(Rectangle1.length, Rectangle1.width)
    are = Rectangle1.surface(Rectangle1.length, Rectangle1.width)
    perimeters.append(perim)
    areas.append(are)
print(perimeters)
print(areas)
