from fractions import gcd


class Fraction:

    def __init__(self, numerator, denominator):
        greatest_common_divisor = gcd(numerator, denominator)
        self.numerator = int(numerator / greatest_common_divisor)
        self.denominator = int(denominator / greatest_common_divisor)

    def __str__(self):
        if self.denominator != 1:
            return "{}/{}". format(self.numerator, self.denominator)
        else:
            return "{}". format(self.numerator)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        numerator = self.numerator * other.denominator + \
            other.numerator * self.denominator
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def __sub__(self, other):
        numerator = self.numerator * other.denominator - \
            other.numerator * self.denominator
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator,
                        self.denominator * other.denominator)

    def __truediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator

        return Fraction(numerator, denominator)

    def __eq__(self, other):
        return (self.numerator / self.denominator) == \
            other.numerator / other.denominator


def main():
    a = Fraction(1, 2)
    b = Fraction(2, 4)

    print (a == b)
    print (a + b)
    print (a - b)
    print (a * b)
    print (a / b)

if __name__ == '__main__':
    main()
