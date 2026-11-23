import math
import unittest

from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_zero_radius(self):
        self.assertEqual(area(0), 0)

    def test_area_unit_radius(self):
        self.assertAlmostEqual(area(1), math.pi)

    def test_area_radius_2(self):
        self.assertAlmostEqual(area(2), 12.566370614359172)

    def test_area_float_radius(self):
        self.assertAlmostEqual(area(0.5), math.pi * 0.25)

    def test_perimeter_zero_radius(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_unit_radius(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)

    def test_perimeter_radius_2(self):
        self.assertAlmostEqual(perimeter(2), 12.566370614359172)


if __name__ == "__main__":
    unittest.main()