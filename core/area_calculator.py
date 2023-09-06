from core.shape_interface import ShapeInterface

class AreaCalculator:
    shapes: []

    def __init__(self, shapes: []) -> None:
        self.shapes = shapes

    def sum(self) -> int:
        summe = 0
        for x in self.shapes:
            if isinstance(x, ShapeInterface):
                summe += x.area()
            else:
                raise TypeError('You tried to generate an area for an object that has no shape')
        return summe      