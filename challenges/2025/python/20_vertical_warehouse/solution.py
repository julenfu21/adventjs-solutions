def drop_gifts(warehouse: list[list[str]], drops: list[int]) -> list[list[str]]:

    def get_lowest_empty_cell_row_index(
        warehouse: list[list[str]],
        column_index: int
    ) -> int | None:
        for row_index in range(len(warehouse) - 1, -1, -1):
            if warehouse[row_index][column_index] == '.':
                return row_index

        return None

    # Code here
    for drop in drops:
        lowest_empty_cell_row_index = get_lowest_empty_cell_row_index(warehouse, drop)
        if lowest_empty_cell_row_index is not None:
            warehouse[lowest_empty_cell_row_index][drop] = '#'

    return warehouse
