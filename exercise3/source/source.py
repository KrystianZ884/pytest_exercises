'''2. Testing a Palindrome Checker

Write tests for a function is_palindrome(s) that checks whether a string is a palindrome.

Function to Test:
'''


def is_palindrome(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    return s == s[::-1]


print(is_palindrome(""))