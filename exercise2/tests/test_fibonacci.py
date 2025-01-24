'''Test Requirements:
	•	Check the output for various valid n values (e.g., 0, 1, 10).
	•	Test for invalid inputs like -1, "a", or 3.5.
	•	Ensure that edge cases (e.g., n=0 and n=1) behave as expected.
'''

import pytest
from exercise2.source.source import fibonacci


@pytest.mark.parametrize("n, expected", [(0, []), (1, [0]), (5, [0, 1, 1, 2, 3]),(20,[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181])])
def test_fibonacci_positive(n, expected):
        assert fibonacci(n) == expected


@pytest.mark.parametrize("n, expected", [("a", TypeError), (-1, ValueError)])
def test_fibonacci_negative(n, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            fibonacci(n)
