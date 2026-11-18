import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

##################################################################

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    ("   ", ""),
    ("  hello, world", "hello, world"),
    ("    Python", "Python"),
    (" Приветствие", "Приветствие"),
    ("  568", "568")
])

def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    (" ", ""),
    ("None", "None"),
    (" [q, w, e, r, t, y]", "[q, w, e, r, t, y]"),
    (" []", "[]")
])

def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

    #######################################################

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "f", False),
    ("Python", "p", False),
    ("478", "7", True),
    ("2026 год", "д", True)
])

def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("", "p", False),
    ("python", "", False),
    (" ", "k", False),
    ("   ", " ", True),
    (None, "r", False),
    ("[]", "m", False)
])

def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

################################################################################

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", "kyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("478", "78", "4"),
    ("2026 год", " год", "2026"),
    ("Hello-world", "-", "Helloworld")
])

def test_delete_symbol_positive(string, symbol, expected):
    result = string_utils.delete_symbol(string, symbol)
    assert result == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("   ", " ", "  "),
    ("SkyPro", "", "SkyPro"),
    ("[1, 2, 3]", "4", "[1, 2, 3]")
])

def test_delete_symbol_negative(string, symbol, expected):
    result = string_utils.delete_symbol(string, symbol)
    assert result == expected