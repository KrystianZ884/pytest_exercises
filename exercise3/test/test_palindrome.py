import pytest
import exercise3.source.source as fut

'''Test Requirements:
	•	Validate with simple palindromes like "radar", "level", and "racecar".
	•	Test with non-palindromes like "hello" and "world".
	•	Ensure the function handles case insensitivity ("RaceCar" -> True).
	•	Test with empty strings, special characters ("!!" -> True), and whitespace-only strings ("   " -> True`).
	•	Verify it raises a TypeError for invalid inputs like integers or lists.
	'''


@pytest.mark.parametrize("input, expected_output", [("radar", True), (" oko  oko ", True), ("!!", True), ("level ", True), ("  ", True),
                                                    ("", True), ("11", True), ("RacEcaR", True), ("a", True)
                                                    , ("A man, a plan, a canal: Panama", True), ("112211", True)])
def test_is_palindrome_positive(input, expected_output):
    assert fut.is_palindrome(input) == expected_output


@pytest.mark.parametrize("input, expected_output", [("hello", False), ("world", False)])
def test_is_palindrome_negative(input, expected_output):
    assert fut.is_palindrome(input) == expected_output


@pytest.mark.parametrize("input, expected_output", [(1, TypeError), ([1,2,3,4,5], TypeError), (["r", "a", "d", "a", "r"], TypeError), (-1, TypeError), ({1: "ala"}, TypeError), ((1,2), TypeError), (21.37, TypeError), (None, TypeError)])
def test_is_palindrome_error_handling(input, expected_output):
    with pytest.raises(expected_output):
        fut.is_palindrome(input)



