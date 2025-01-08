class Circle: 
    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, new_radius) -> None:
        self.radius = new_radius

    def get_radius(self) -> None:
        print (f"Радиус: {self.radius}")


newCircle = circle(10)

circ.get_radius()
circ.set_radius(5)
circ.get_radius()