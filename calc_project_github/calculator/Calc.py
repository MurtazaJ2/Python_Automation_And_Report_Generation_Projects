"""simple calculator"""


class Calculator:
    """Calculator class"""

    @staticmethod
    def addition(num1, num2=0):
        """addition function"""
        if isinstance(num1, (int, float, complex)) and isinstance(num2, (int, float, complex)):
            return num1 + num2
        else:
            return "TypeError"

    @staticmethod
    def subtraction(num1, num2):
        """subtraction function"""
        if isinstance(num1, (int, float, complex)) and isinstance(num2, (int, float, complex)):
            return num1 - num2
        else:
            return "TypeError"

    @staticmethod
    def multiplication(num1, num2):
        """multiplication function"""
        if isinstance(num1, (int, float, complex)) and isinstance(num2, (int, float, complex)):
            return num1 * num2
        else:
            return "TypeError"

    @staticmethod
    def division(num1, num2):
        """division function"""
        try:
            if isinstance(num1, (int, float, complex)) and isinstance(num2, (int, float, complex)):
                return float(f'{num1 / num2:0.09f}')
            else:
                return "TypeError"
        except ZeroDivisionError:
            return "ValueError"
