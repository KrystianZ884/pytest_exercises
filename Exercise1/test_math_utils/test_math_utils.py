import pytest
from Exercise1.math_utils.math_utils import add, subtract, multiply, divide, is_prime


@pytest.mark.parametrize("a, b", [(1, 1), (-1, 1), (0, 1), ("a", "b"), ("a", 1), (1.5, 1)])
def test_add(a, b):
    if (isinstance(a, str) and isinstance(b, int)) or (isinstance(a, int) and isinstance(b, str)):
        with pytest.raises(TypeError):
            add(a, b)
    else:
        assert add(a, b) == a+b


@pytest.mark.parametrize("a, b", [(1, 1), (-1, 1), (0, 1), ("a", "b"), ("a", 1), (1.5, 1)])
def test_subtract(a, b):
    if isinstance(a, str) or isinstance(b, str):
        with pytest.raises(TypeError):
            subtract(a, b)
    else:
        assert subtract(a, b) == a-b


@pytest.mark.parametrize("a, b", [(1, 1), (-1, 1), (0, 1), ("a", "b"), ("a", 1), (1.5, 1)])
def test_multiply(a, b):
    if isinstance(a, str) and isinstance(b, str):
        with pytest.raises(TypeError):
            multiply(a, b)
    else:
        assert multiply(a, b) == a*b


@pytest.mark.parametrize("a, b", [(1, 1), (-1, 1), (0, 1), ("a", "b"), ("a", 1), (1.5, 1)])
def test_divide(a, b):
    if isinstance(a, str) or isinstance(b, str):
        with pytest.raises(TypeError):
            divide(a, b)
    else:
        assert divide(a, b) == a/b


def test_is_prime():
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for i in range(1, 101):
        if i in prime:
            assert is_prime(i) is True
        else:
            assert is_prime(i) is False
