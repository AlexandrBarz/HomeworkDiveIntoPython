import unittest
from homework14_1 import check_triangle

class TestCaseName(unittest.TestCase):

    def test_method_1(self):
        self.assertEqual(check_triangle(10, 10, 10), 'Треугольник равносторонний')

        self.assertEqual(check_triangle(20, 10, 20), 'Треугольник равнобедренный')

        self.assertEqual(check_triangle(15, 20, 30), 'Треугольник разносторонний')

    def test_method_2(self):
        self.assertEqual(check_triangle(30, 15, 10), 'Треугольник не существует')


if __name__ == '__main__':
    unittest.main(verbosity=2)