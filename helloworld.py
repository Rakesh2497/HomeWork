print("Hello, World!")

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    
if __name__ == "__main__":
    calc = Calculator()
    print("Addition: ", calc.add(5, 3))
    print("Subtraction: ", calc.subtract(5, 3))
    print("Multiplication: ", calc.multiply(5, 3))
    print("Division: ", calc.divide(5, 3))
    try:
        print("Division by zero: ", calc.divide(5, 0))
    except ValueError as e:
        print(e)

# This is a simple calculator module with basic arithmetic operations.
# It includes error handling for division by zero.
        
# The module can be run as a script to demonstrate its functionality.
# It prints "Hello, World!" and performs some sample calculations.

class Bingo:
    def __init__(self, numbers):
        self.numbers = set(numbers)
        self.called_numbers = set()

    def call_number(self, number):
        if number in self.numbers:
            self.called_numbers.add(number)
            return True
        return False

    def has_bingo(self):
        return self.numbers == self.called_numbers

if __name__ == "__main__":
    bingo_game = Bingo([1, 2, 3, 4, 5])
    print("Calling number 3:", bingo_game.call_number(3))
    print("Calling number 6:", bingo_game.call_number(6))
    print("Current called numbers:", bingo_game.called_numbers)
    print("Has Bingo?", bingo_game.has_bingo())
    for num in [1, 2, 4, 5]:
        bingo_game.call_number(num)
    print("Has Bingo after calling all numbers?", bingo_game.has_bingo())
# This is a simple Bingo game implementation.
    