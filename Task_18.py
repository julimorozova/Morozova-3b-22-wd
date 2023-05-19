class GeometricFigure:
    def __init__(self, square, perimeter):
        self.square = square
        self.perimeter = perimeter

    def get_info(self):
        print(f"Площадь - {self.square}, периметр - {self.perimeter}")


figure = GeometricFigure(23, 56)
figure.get_info()