from core.area_calculator import AreaCalculator
from core.area_sum_outputter import AreaSumOutputter
from core.volume_calculator import VolumeCalculator
from core.volume_sum_outputter import VolumeSumOutputter
from entities.circle import Circle
from entities.square import Square
from entities.ball import Ball
from entities.cube import Cube

def main():
    shapes = [Circle(2), Square(5), Square(6)]

    areas = AreaCalculator(shapes)
    output2d = AreaSumOutputter(areas)

    output2d.output()

    shapes = [Ball(2), Cube(4)]

    volumes = VolumeCalculator(shapes)
    output3d = VolumeSumOutputter(volumes)

    output3d.output()
main()