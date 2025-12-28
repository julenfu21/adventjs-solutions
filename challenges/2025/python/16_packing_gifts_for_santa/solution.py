def pack_gifts(gifts: list[int], max_weight: int) -> int | None:
    # Code here
    sleigh_count = 0
    current_sleigh_weight = 0

    if gifts:
        sleigh_count += 1

    for gift in gifts:
        if gift > max_weight:
            return None

        current_sleigh_weight += gift
        if current_sleigh_weight > max_weight:
            sleigh_count += 1
            current_sleigh_weight = gift

    return sleigh_count
