import pytest

from solution import time_until_take_off


def test_time_until_take_off_returns_int():
    from_time = "2025*12*25@00|00|00 NP"
    take_off_time = "2025*12*25@00|00|00 NP"

    seconds_difference = time_until_take_off(from_time, take_off_time)

    assert isinstance(seconds_difference, int)

@pytest.mark.parametrize(
    "from_time,take_off_time,expected_difference", [
        ("2025*12*24@23|59|30 NP", "2025*12*25@00|00|00 NP", 30),
        ("2025*12*25@00|00|00 NP", "2025*12*25@00|00|00 NP", 0),
        ("2025*12*25@00|00|12 NP", "2025*12*25@00|00|00 NP", -12),
        ("2025*12*24@00|00|00 NP", "2025*12*25@00|00|00 NP", 86400),
        ("2025*12*27@00|00|00 NP", "2025*12*25@00|00|00 NP", -172800),
        ("2030*01*01@00|00|10 NP", "2030*01*01@00|00|20 NP", 10),
        ("2030*01*01@00|01|00 NP", "2030*01*01@00|00|00 NP", -60)
    ]
)
def test_time_until_take_off(from_time, take_off_time, expected_difference):
    seconds_difference = time_until_take_off(from_time, take_off_time)

    assert seconds_difference == expected_difference
