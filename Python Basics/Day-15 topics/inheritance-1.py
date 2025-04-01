class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
    
    def diameter(self):
        print(self.radius * 2)

    def properties(self):
        print(f"Radius: {self.radius}, Colour: {self.color}")

class Shapes(Circle):
    def __init__(self, radius, color):
        super().__init__(radius, color)

circle_1 = Shapes(10, "red")
circle_1.diameter()
circle_1.properties()