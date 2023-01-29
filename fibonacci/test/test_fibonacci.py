from unittest import TestCase
from fibonacci.calculator import FibonacciCalculator

class FibonacciCalculatorTest(TestCase):
    def test_zero_and_one_return_one(self):
        assert FibonacciCalculator.calculate(0) == 1 
        assert FibonacciCalculator.calculate(1) == 1

    def test_value_greater_than_one_returns_success(self):
        assert FibonacciCalculator.calculate(5) == 8 