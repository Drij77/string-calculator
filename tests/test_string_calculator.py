import pytest
from string_calculator import StringCalculator

def test_empty_string_returns_zero():
    calc = StringCalculator()
    assert calc.add("") == 0

def test_single_number_returns_number():
    calc = StringCalculator()
    assert calc.add("1") == 1

def test_two_numbers_returns_sum():
    calc = StringCalculator()
    assert calc.add("1,5") == 6

def test_multiple_numbers_returns_sum():
    calc = StringCalculator()
    assert calc.add("1,2,3,4") == 10

def test_new_lines_between_numbers():
    calc = StringCalculator()
    assert calc.add("1\n2,3") == 6

def test_custom_delimiter():
    calc = StringCalculator()
    assert calc.add("//|\n1|2|3") == 6

def test_negative_number_throws_exception():
    calc = StringCalculator()
    with pytest.raises(ValueError, match="negative numbers not allowed: -1"):
        calc.add("-1,2")

def test_multiple_negative_numbers_throws_exception():
    calc = StringCalculator()
    with pytest.raises(ValueError, match="negative numbers not allowed: -1, -2"):
        calc.add("-1,-2,3")