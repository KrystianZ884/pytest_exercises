'''1. Testing a Fibonacci Generator

Write tests for a function fibonacci(n) that generates the first n numbers in the Fibonacci sequence.
'''


def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence