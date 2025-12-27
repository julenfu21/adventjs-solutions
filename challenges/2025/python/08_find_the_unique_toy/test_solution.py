import pytest

from solution import find_unique_toy


def test_find_unique_toy_returns_string():
    toy = "Gift"

    first_non_repeated_letter = find_unique_toy(toy)

    assert isinstance(first_non_repeated_letter, str)

@pytest.mark.parametrize(
    "toy,expected_first_non_repeated_letter", [
        ("Gift", 'G'),
        ("sS", ''),
        ("reindeeR", 'i'),
        ("T", 'T'),
        ("aA", ''),
        ("z", 'z'),
        ("", ''),
        ("a", 'a'),
        ("aabbc", 'c'),
        ("AaBbCc", '')
    ]
)
def test_match_gloves(toy, expected_first_non_repeated_letter):
    first_non_repeated_letter = find_unique_toy(toy)

    assert first_non_repeated_letter == expected_first_non_repeated_letter
