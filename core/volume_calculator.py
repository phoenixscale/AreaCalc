from core.area_calculator import AreaCalculator
from core.solid_shape_interface import SolidShapeInterface

class VolumeCalculator(AreaCalculator):
    def __init__(self, shapes: []) -> None:
        super().__init__(shapes)

    def sum(self) -> int:
        summe = 0
        for x in self.shapes:
            if isinstance(x, SolidShapeInterface):
                summe += x.volume()
            else:
                raise TypeError('You tried to generate an area for an object that has no Volume')
        return summe