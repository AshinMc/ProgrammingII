import pytest

# Calculator function implementations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Calculator class that uses the functions
class Calculator:
    def add(self, a, b):
        return add(a, b)
    
    def subtract(self, a, b):
        return subtract(a, b)
    
    def multiply(self, a, b):
        return multiply(a, b)
    
    def divide(self, a, b):
        return divide(a, b)

# Pytest tests
def test_calculator():
    calc = Calculator()
    
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    
    assert calc.subtract(5, 2) == 3
    assert calc.subtract(2, 5) == -3
    
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(-2, 3) == -6
    
    assert calc.divide(6, 2) == 3
    assert calc.divide(5, 2) == 2.5
    
    with pytest.raises(ValueError):
        calc.divide(5, 0)