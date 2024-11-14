import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add_negative_and_zero(self):
        self.assertEqual(self.calc.add(-1, 0), -1)

    def test_sub_positive_numbers(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)

    def test_sub_negative_number(self):
        self.assertEqual(self.calc.subtract(-2, 1), -3)

    def test_mul_positive_numbers(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
    
    def test_mul_negative_number(self):
        self.assertEqual(self.calc.multiply(2, -3), -6)

    def test_divide_negative_number(self):
        self.assertEqual(self.calc.divide(-4, 2), -2)
    
    def test_divide_by_zero(self):
        self.assertEqual(self.calc.divide(4, 0), 'err')
    
    def test_mod_positive_numbers(self):
        self.assertEqual(self.calc.modulo(5, -2), -1)
    
    def test_mod_by_zero(self):
        self.assertEqual(self.calc.modulo(5, 0), 'err')

if __name__ == '__main__':
    unittest.main()