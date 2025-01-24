def add(a, b):
    """Adds two numbers."""
    return a + b


def subtract(a, b):
    """Subtracts the second number from the first."""
    return a - b


def multiply(a, b):
    """Multiplies two numbers."""
    return a * b


def divide(a, b):
    """Divides the first number by the second. Raises ValueError for division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(divide(0, 1))