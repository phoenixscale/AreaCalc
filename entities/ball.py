from core.shape_interface import ShapeInterface
from core.solid_shape_interface import SolidShapeInterface
from entities.circle import Circle
import numpy as np

class Ball(Circle, ShapeInterface, SolidShapeInterface):
    radius: int

    def __init__(self, radius) -> None:
        super().__init__(radius)

    def area(self) -> int:
        return super().area()

    def volume(self) -> float:
        return np.divide(4,3)*np.pi*pow(self.radius,3)