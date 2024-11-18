from fractions import Fraction

def solution(numer1, denom1, numer2, denom2):
    num1 = Fraction(numer1, denom1)
    num2 = Fraction(numer2, denom2)
    result = num1 + num2
    arr = []
    arr.append(result.numerator)
    arr.append(result.denominator)
    return arr