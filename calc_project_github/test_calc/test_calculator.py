"""test function of Calculator"""

from calculator import Calc


class TestCalcMethods:

    def test_addition_two_integers(self, num1, num2, num3):
        """function to test addition function"""
        result = Calc.Calculator.addition(num1, num2)
        assert result == num3
        if result == num3:
            return True, result
        else:
            return False, result

    def test_subtraction_two_integers(self, num1, num2, num3):
        """function to test subtraction function"""
        result = Calc.Calculator.subtraction(num1, num2)
        assert result == num3
        if result == num3:
            return True, result
        else:
            return False, result

    def test_multiplication_two_integers(self, num1, num2, num3):
        """function to test multiplication function"""
        result = Calc.Calculator.multiplication(num1, num2)
        assert result == num3
        if result == num3:
            return True, result
        else:
            return False, result

    def test_division_two_integers(self, num1, num2, num3):
        """function to test division function"""
        result = Calc.Calculator.division(num1, num2)
        assert result == num3
        if result == num3:
            return True, result
        else:
            return False, result
