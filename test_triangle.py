import unittest

from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_area_zero_height(self):
        self.assertEqual(area(4, 0), 0)

    def test_area_base_4_height_3(self):
        self.assertEqual(area(4, 3), 6.0)

    def test_area_odd_product(self):
        self.assertEqual(area(5, 3), 7.5)

    def test_perimeter_right_triangle(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_equilateral(self):
        self.assertEqual(perimeter(2, 2, 2), 6)

    def test_perimeter_float_sides(self):
        self.assertAlmostEqual(perimeter(1.5, 2.5, 3.0), 7.0)


if __name__ == "__main__":
    unittest.main()