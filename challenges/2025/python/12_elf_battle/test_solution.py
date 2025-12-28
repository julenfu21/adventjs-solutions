import pytest

from solution import elf_battle


def test_elf_battle_returns_int():
    elf1 = "A"
    elf2 = "B"

    battle_outcome = elf_battle(elf1, elf2)

    assert isinstance(battle_outcome, int)

@pytest.mark.parametrize(
    "elf1,elf2,expected_outcome", [
        ("A", "B", 0),
        ("F", "B", 1),
        ("AAB", "BBA", 0),
        ("AFA", "BBA", 1),
        ("AFAB", "BBAF", 1),
        ("AA", "FF", 2),
        ("AAFFFBBB", "ABBBBFFF", 1)
    ]
)
def test_elf_battle(elf1, elf2, expected_outcome):
    battle_outcome = elf_battle(elf1, elf2)

    assert battle_outcome == expected_outcome
