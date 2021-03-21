class Calculator:
    from math import sqrt

    def __init__(self) -> None:
        self.__current = 0

    def add(self, a: [int, float]) -> None:
        """Adds a given number to the current count."""
        self.__current += a

    def subtract(self, a: [int, float]) -> None:
        """Subtracts a given number from the current count."""
        self.__current -= a

    def multiply(self, a: [int, float]) -> None:
        """Multiplies the current count by a given number."""
        self.__current = self.__current * a

    def divide(self, a: [int, float]) -> [None, str]:
        """Divides the current count by a given number."""
        try:
            self.__current = self.__current / a
        except ZeroDivisionError:
            print("Cannot divide by 0!")

    def root(self) -> [None, str]:
        """Takes a square root of the current count."""
        try:
            self.__current = self.sqrt(self.__current)
        except ValueError:
            print("Only 0 and positive numbers have a square root!")

    @property
    def get_current(self):
        """Returns the current count"""
        return self.__current

    def reset_current(self) -> None:
        """Sets the current count to zero."""
        self.__current = 0
