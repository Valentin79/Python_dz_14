
from Matrix import add_matrix, mul_matrix, equals_matrix
import unittest

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]),
                         [[10, 10, 10], [10, 10, 10], [10, 10, 10]])

    def test_add_raises(self):
        with self.assertRaises(Exception) as excinfo:
            add_matrix([[1, 2, 3], [4, 5, 6]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]])
        self.assertTrue('Количество строк и колонок матриц не совпадают' == str(excinfo.exception))

    def test_mul(self):
        self.assertEqual(mul_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]),
                         [[30, 24, 18], [84, 69, 54], [138, 114, 90]])
        self.assertEqual(mul_matrix([[1, 2, 3], [5, 6, 7]], [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]),
                         [[38, 44, 50, 56], [98, 116, 134, 152]])

    def test_mul_raises(self):
        with self.assertRaises(Exception) as excinfo:
            mul_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3, 4], [5, 6, 7, 8]])
        self.assertTrue('Количество строк и колонок матриц не совпадают' == str(excinfo.exception))

    def test_equals_matrix(self):
        self.assertEqual(equals_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                         True)
        self.assertEqual(equals_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6]]),
                         False)


if __name__ == '__main__':
    unittest.main(verbosity=2)