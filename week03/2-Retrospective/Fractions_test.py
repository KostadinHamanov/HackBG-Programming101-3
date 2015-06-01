import unittest
from fractions import Fraction


class FractionTest(unittest.TestCase):

    def setUp(self):
        self.a = Fraction(1, 2)
        self.b = Fraction(2, 4)

    def test_is_instance(self):
        self.assertTrue(isinstance(self.a, Fraction))
        self.assertTrue(isinstance(self.b, Fraction))

    def test_gcd(self):
        self.assertEqual(self.a.numerator, 1)
        self.assertEqual(self.b.denominator, 2)

    def test_str(self):
        self.assertEqual(str(self.a), "1/2")
        self.assertEqual(str(self.b), "1/2")

    def test_repr(self):
        self.assertEqual(repr(self.a), "Fraction(1, 2)")
        self.assertEqual(repr(self.b), "Fraction(1, 2)")

    def test_equals(self):
        self.assertTrue(self.a == self.b)

    def test_addition(self):
        self.assertEqual(self.a + self.b, 1)

    def test_substraction(self):
        self.assertEqual(self.a - self.b, 0)

    def test_multiplication(self):
        self.assertEqual(self.a * self.b, 1/4)

    def test_division(self):
        self.assertEqual(self.a / self.b, 1)

if __name__ == '__main__':
    unittest.main()
