"""Tests for Lab 0 Question 1"""

import sys
sys.path.append(".")
import unittest
from src.q1 import is_palindrome

def test_ispalindrome() -> None:
    assert is_palindrome('a') == False
    assert is_palindrome('sas') == True
    assert is_palindrome('') == True
