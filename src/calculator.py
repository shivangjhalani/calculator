"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""

import math

def add(a, b):
    """Add two numbers together"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers with input validation and logging."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    
    print(f"Multiplying {a} × {b}")  # Logging
    result = a * b
    print(f"Result: {result}")
    return result

def divide(a, b):
    """Divide a by b with enhanced error handling."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ValueError(f"Cannot divide {a} by zero - division by zero is undefined")
    
    print(f"Dividing {a} ÷ {b}")  # Logging
    result = a / b
    print(f"Result: {result}")
    return result

def power(a, b):
    """Raise a to the power of b with input validation and logging."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Power function requires numeric inputs")
    
    print(f"Calculating {a} ^ {b}")  # Logging
    result = a ** b
    print(f"Result: {result}")
    return result

def sqrt(a):
    """Calculate the square root of a with error handling."""
    if not isinstance(a, (int, float)):
        raise TypeError("Square root requires a numeric input")
    if a < 0:
        raise ValueError(f"Cannot calculate sqrt of negative number {a}")
    
    print(f"Calculating √{a}")  # Logging
    result = math.sqrt(a)
    print(f"Result: {result}")
    return result


# Demo when run directly
if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"4 × 3 = {multiply(4, 3)}")
    print(f"10 ÷ 2 = {divide(10, 2)}")
    print(f"2 ^ 5 = {power(2, 5)}")
    print(f"√16 = {sqrt(16)}")

