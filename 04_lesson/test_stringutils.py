import pytest
from stringutils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


def test_capitilize(utils):
    assert utils.capitilize("skypro") == "Skypro"
    assert utils.capitilize("") == ""
    assert utils.capitilize("hELLO") == "Hello"


@pytest.mark.parametrize("input_string, expected_output", [
    ("   skypro", "skypro"),
    ("skypro   ", "skypro   "),
    ("   ", ""),
    ("test", "test"),
    ("", "")
])
def test_trim(utils, input_string, expected_output):
    assert utils.trim(input_string) == expected_output


@pytest.mark.parametrize("input_string, delimeter, expected_output", [
    ("a,b,c,d", ",", ["a", "b", "c", "d"]),
    ("1:2:3", ":", ["1", "2", "3"]),
    ("", ",", []),
    ("a b c", " ", ["a", "b", "c"])
])
def test_to_list(utils, input_string, delimeter, expected_output):
    assert utils.to_list(input_string, delimeter) == expected_output


@pytest.mark.parametrize("input_string, symbol, expected_output", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("", "a", False)
])
def test_contains(utils, input_string, symbol, expected_output):
    assert utils.contains(input_string, symbol) == expected_output


@pytest.mark.parametrize("input_string, symbol, expected_output", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("SkyPro", "x", "SkyPro")
])
def test_delete_symbol(utils, input_string, symbol, expected_output):
    assert utils.delete_symbol(input_string, symbol) == expected_output


@pytest.mark.parametrize("input_string, symbol, expected_output", [
    ("SkyPro", "S", True),
    ("SkyPro", "P", False),
    ("", "S", False)
])
def test_starts_with(utils, input_string, symbol, expected_output):
    assert utils.starts_with(input_string, symbol) == expected_output


@pytest.mark.parametrize("input_string, symbol, expected_output", [
    ("SkyPro", "o", True),
    ("SkyPro", "y", False),
    ("", "o", False)
])
def test_end_with(utils, input_string, symbol, expected_output):
    assert utils.end_with(input_string, symbol) == expected_output


@pytest.mark.parametrize("input_string, expected_output", [
    ("", True),
    ("   ", True),
    ("SkyPro", False)
])
def test_is_empty(utils, input_string, expected_output):
    assert utils.is_empty(input_string) == expected_output


@pytest.mark.parametrize("lst, joiner, expected_output", [
    ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
    (["Sky", "Pro"], ", ", "Sky, Pro"),
    (["Sky", "Pro"], "-", "Sky-Pro"),
    ([], ", ", "")
])
def test_list_to_string(utils, lst, joiner, expected_output):
    assert utils.list_to_string(lst, joiner) == expected_output
