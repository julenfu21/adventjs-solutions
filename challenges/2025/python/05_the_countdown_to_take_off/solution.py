from datetime import datetime


def time_until_take_off(from_time: str, take_off_time: str) -> int:
    # All your code here
    north_pole_format = "%Y*%m*%d@%H|%M|%S NP"

    from_time_datetime = datetime.strptime(from_time, north_pole_format)
    take_off_time_datetime = datetime.strptime(take_off_time, north_pole_format)

    time_difference = take_off_time_datetime - from_time_datetime
    seconds_difference = int(time_difference.total_seconds())
    return seconds_difference
