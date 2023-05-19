class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_square(self):
        result = self.length * self.width
        return f"Площадь треугольника равна {result}"


rectangle = Rectangle(3, 6)
print(rectangle.get_square())