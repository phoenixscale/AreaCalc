from core.area_calculator import AreaCalculator

class AreaSumOutputter:
    calculator: AreaCalculator

    def __init__(self, calculator: AreaCalculator) -> None:
        self.calculator = calculator

    def output(self) -> None:
        print(self.calculator.sum())