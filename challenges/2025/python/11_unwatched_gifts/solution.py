def find_unsafe_gifts(warehouse: list[str]) -> int:
    # Code here
    unsafe_gift_count = 0

    for row_id, row in enumerate(warehouse):
        for col_id, col in enumerate(row):
            if col == '*':
                if (
                    (row_id - 1 >= 0 and warehouse[row_id - 1][col_id] == '#') or
                    (row_id + 1 < len(warehouse) and warehouse[row_id + 1][col_id] == '#') or
                    (col_id - 1 >= 0 and warehouse[row_id][col_id - 1] == '#') or
                    (col_id + 1 < len(warehouse[row_id]) and warehouse[row_id][col_id + 1] == '#')
                ):
                    continue
                else:
                    unsafe_gift_count += 1

    return unsafe_gift_count
