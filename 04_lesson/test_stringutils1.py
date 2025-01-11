import pytest
from stringutils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()

# Positive


def test_pos_capitalize(utils):
    assert utils.capitilize("skypro") == "Skypro"
    assert utils.capitilize("hello world") == "Hello world"


def test_pos_trim(utils):
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim(" no space ") == "no space "


def test_pos_to_list(utils):
    assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert utils.to_list("1:2:3", ":") == ["1", "2", "3"]
    assert utils.to_list("one, two, three") == ["one", " two", " three"]


def test_pos_contains(utils):
    assert utils.contains("SkyPro", "S") is True
    assert utils.contains("SkyPro", "y") is True


def test_pos_delete_symbol(utils):
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"


def test_pos_starts_with(utils):
    assert utils.starts_with("SkyPro", "S") is True
    assert utils.starts_with("123abc", "1") is True


def test_pos_end_with(utils):
    assert utils.end_with("SkyPro", "o") is True
    assert utils.end_with("EndWith", "h") is True


def test_pos_is_empty(utils):
    assert utils.is_empty("") is True
    assert utils.is_empty(" ") is True


def test_pos_list_to_string(utils):
    assert utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"

# Negative


def test_neg_capitalize(utils):
    assert utils.capitilize("") == ""
    assert utils.capitilize("123abc") == "123abc"


def test_neg_trim(utils):
    assert utils.trim("") == ""
    assert utils.trim("    ") == ""
    assert utils.trim("test") == "test"


def test_neg_to_list(utils):
    assert utils.to_list("", ",") == []
    assert utils.to_list("a b c", " ") == ["a", "b", "c"]


def test_neg_contains(utils):
    assert utils.contains("", "A") is False
    assert utils.contains("SkyPro", "U") is False


def test_neg_delete_symbol(utils):
    assert utils.delete_symbol("SkyPro", "Z") == "SkyPro"
    assert utils.delete_symbol("", "X") == ""


def test_neg_starts_with(utils):
    assert utils.starts_with("SkyPro", "P") is False
    assert utils.starts_with("abcd", "") is True


def test_neg_end_with(utils):
    assert utils.end_with("", "A") is False
    assert utils.end_with("SkyPro", "y") is False


def test_neg_is_empty(utils):
    assert utils.is_empty("SkyPro") is False
    assert utils.is_empty("    a    ") is False


def test_neg_list_to_string(utils):
    assert utils.list_to_string([], "-") == ""
    assert utils.list_to_string([1], ", ") == "1"
