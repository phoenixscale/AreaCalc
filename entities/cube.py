from core.shape_interface import ShapeInterface
from core.solid_shape_interface import SolidShapeInterface
from entities.square import Square

class Cube(Square, ShapeInterface, SolidShapeInterface):
    def __init__(self, length) -> None:
        super().__init__(length)

    def area(self) -> int:
        return super().area()
    
    def volume(self):
        return pow(self.length,3)