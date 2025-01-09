import pytest
from stringutils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


def test_capitilize(utils):

    # Positive

    assert utils.capitilize("skypro") == "Skypro"

    # Negative

    assert utils.capitilize("") == ""
    assert utils.capitilize("hELLO") == "Hello"


@pytest.mark.parametrize("input_string, expected_output", [

    # Positive

    ("   skypro", "skypro"),
    ("skypro   ", "skypro   "),
    ("test", "test"),

    # Negative

    ("   ", ""),
    ("", "")
])
def test_trim(utils, input_string, expected_output):
    assert utils.trim(input_string) == expected_output


@pytest.mark.parametrize("input_string, delimeter, expected_output", [

    # Positive

    ("a,b,c,d", ",", ["a", "b", "c", "d"]),
    ("1:2:3", ":", ["1", "2", "3"]),
    ("a b c", " ", ["a", "b", "c"]),

    # Negative

    ("", ",", [])
])
def test_to_list(utils, input_string, delimeter, expected_output):
    assert utils.to_list(input_string, delimeter) == expected_output


@pytest.mark.parametrize("input_string, symbol, expected_output", [

    # Positive

    ("SkyPro", "S", True),

    # Negative

    ("SkyPro", "U", False),
    ("", "a", False)
])
def test_contains(utils, input_string, symbol, expected_output):
    assert utils.contains(input_string, symbol) == expected_output


@pytest.mark.parametrize("input_string, symbol, expected_output", [

    # Positive

    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),

    # Negative

    ("SkyPro", "x", "SkyPro")
])
def test_delete_symbol(utils, input_string, symbol, expected_output):
    assert utils.delete_symbol(input_string, symbol) == expected_output


@pytest.mark.parametrize("input_string, symbol, expected_output", [

    # Positive

    ("SkyPro", "S", True),

    # Negative

    ("SkyPro", "P", False),
    ("", "S", False)
])
def test_starts_with(utils, input_string, symbol, expected_output):
    assert utils.starts_with(input_string, symbol) == expected_output


@pytest.mark.parametrize("input_string, symbol, expected_output", [

    # Positive

    ("SkyPro", "o", True),

    # Negative

    ("SkyPro", "y", False),
    ("", "o", False)
])
def test_end_with(utils, input_string, symbol, expected_output):
    assert utils.end_with(input_string, symbol) == expected_output


@pytest.mark.parametrize("input_string, expected_output", [

    # Positive

    ("", True),
    ("   ", True),

    # Negative

    ("SkyPro", False)
])
def test_is_empty(utils, input_string, expected_output):
    assert utils.is_empty(input_string) == expected_output


@pytest.mark.parametrize("lst, joiner, expected_output", [

    # Positive

    ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
    (["Sky", "Pro"], ", ", "Sky, Pro"),
    (["Sky", "Pro"], "-", "Sky-Pro"),

    # Negative

    ([], ", ", "")
])
def test_list_to_string(utils, lst, joiner, expected_output):
    assert utils.list_to_string(lst, joiner) == expected_output
