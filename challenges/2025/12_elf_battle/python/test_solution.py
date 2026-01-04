import pytest

from solution import elf_battle


def test_elf_battle_returns_int():
    elf1 = "A"
    elf2 = "B"

    battle_outcome = elf_battle(elf1, elf2)

    assert isinstance(battle_outcome, int)

@pytest.mark.parametrize(
    "elf1,elf2,expected_outcome", [
        pytest.param("A", "B", 0, id="test-2"),
        pytest.param("F", "B", 1, id="test-3"),
        pytest.param("AAB", "BBA", 0, id="test-4"),
        pytest.param("AFA", "BBA", 1, id="test-5"),
        pytest.param("AFAB", "BBAF", 1, id="test-6"),
        pytest.param("AA", "FF", 2, id="test-7"),
        pytest.param("AAFFFBBB", "ABBBBFFF", 1, id="test-8")
    ]
)
def test_elf_battle(elf1, elf2, expected_outcome):
    battle_outcome = elf_battle(elf1, elf2)

    assert battle_outcome == expected_outcome
