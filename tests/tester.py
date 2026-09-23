import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import rectangle
import square
import circle
import triangle

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)
    
    def test_negative_mul(self):
        res = rectangle.area(-5, 7)
        self.assertEqual(res, -35)

    def test_sum(self):
        res = rectangle.perimeter(6, 7)
        self.assertEqual(res, 26)



class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_normal_area(self):
        res = square.area(5)
        self.assertEqual(res, 25)

    def test_perimeter(self):
        res = square.perimeter(5)
        self.assertEqual(res, 20)


class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_normal_area(self):
        res = circle.area(10)
        self.assertAlmostEqual(res, 314.15, places=1)

    def test_perimeter(self):
        res = circle.perimeter(10)
        self.assertAlmostEqual(res, 62.8, places=1)


class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = triangle.area(0, 5)
        self.assertEqual(res, 0)

    def test_normal_area(self):
        res = triangle.area(6, 7)
        self.assertEqual(res, 21)

    def test_perimeter(self):
        res = triangle.perimeter(5, 6, 7)
        self.assertEqual(res, 18)
