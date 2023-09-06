import unittest
import numpy as np
from core.area_calculator import AreaCalculator
from core.volume_calculator import VolumeCalculator
from entities.circle import Circle
from entities.square import Square
from entities.ball import Ball
from entities.cube import Cube


def test_sum_2d():
    shapes = [Circle(2), Square(5), Square(6)]
    areas = AreaCalculator(shapes)
    assert np.round(areas.sum(),3)==np.round(73.56637061435917,3)

def test_sum_3d():
    shapes = [Ball(2), Cube(4)]
    volumes = VolumeCalculator(shapes)
    assert np.round(volumes.sum(), 3)==np.round(97.51032163829112,3)

if __name__ == '__main__':
    unittest.main()