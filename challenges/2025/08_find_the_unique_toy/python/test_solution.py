import pytest

from solution import find_unique_toy


def test_find_unique_toy_returns_string():
    toy = "Gift"

    first_non_repeated_letter = find_unique_toy(toy)

    assert isinstance(first_non_repeated_letter, str)

@pytest.mark.parametrize(
    "toy,expected_first_non_repeated_letter", [
        pytest.param("Gift", 'G', id="test-2"),
        pytest.param("sS", '', id="test-3"),
        pytest.param("reindeeR", 'i', id="test-4"),
        pytest.param("T", 'T', id="test-5"),
        pytest.param("aA", '', id="test-6"),
        pytest.param("z", 'z', id="test-7"),
        pytest.param("", '', id="test-8"),
        pytest.param("a", 'a', id="test-9"),
        pytest.param("aabbc", 'c', id="test-10"),
        pytest.param("AaBbCc", '', id="test-11")
    ]
)
def test_find_unique_toy(toy, expected_first_non_repeated_letter):
    first_non_repeated_letter = find_unique_toy(toy)

    assert first_non_repeated_letter == expected_first_non_repeated_letter
