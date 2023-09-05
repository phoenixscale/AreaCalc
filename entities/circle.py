from core.shape_interface import ShapeInterface
import numpy as np

class Circle(ShapeInterface):
    radius: int

    def __init__(self, radius) -> None:
        self.radius = radius

    def __str__(self):
        return f"{self.length}"        

    def area(self) -> int:
        return  np.pi * pow(self.radius, 2)