import unittest

from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        self.assertEqual(area(10, 0), 0)

    def test_square_mul(self):
        self.assertEqual(area(10, 10), 100)

    def test_area_different_sides(self):
        self.assertEqual(area(2, 3), 6)

    def test_area_float_sides(self):
        self.assertAlmostEqual(area(2.5, 4), 10.0)

    def test_perimeter_zero_side(self):
        self.assertEqual(perimeter(10, 0), 20)

    def test_perimeter_different_sides(self):
        self.assertEqual(perimeter(2, 3), 10)

    def test_perimeter_equal_sides(self):
        self.assertEqual(perimeter(5, 5), 20)


if __name__ == "__main__":
    unittest.main()