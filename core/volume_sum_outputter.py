from core.volume_calculator import VolumeCalculator

class VolumeSumOutputter():
    calculator: VolumeCalculator

    def __init__(self, calculator: VolumeCalculator) -> None:
        self.calculator = calculator

    def output(self) -> None:
        print(self.calculator.sum())