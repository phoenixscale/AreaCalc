from core.shape_interface import ShapeInterface

class Square(ShapeInterface):
    length: int

    def __init__(self, length) -> None:
        self.length = length

    def __str__(self):
        return f"{self.length}"

    def area(self) -> int:
        return pow(self.length, 2)
