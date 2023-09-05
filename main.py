from core.area_calculator import AreaCalculator
from core.area_sum_outputter import AreaSumOutputter
from entities.circle import Circle
from entities.square import Square

def main():
    shapes = [Circle(2), Square(5), Square(6)]

    areas = AreaCalculator(shapes)
    output = AreaSumOutputter(areas)

    output.output()

main()