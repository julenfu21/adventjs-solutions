def clear_gifts(warehouse: list[list[str]], drops: list[int]) -> list[list[str]]:

    def get_lowest_empty_cell_row_index(
        warehouse: list[list[str]],
        column_index: int
    ) -> int | None:
        for row_index in range(len(warehouse) - 1, -1, -1):
            if warehouse[row_index][column_index] == '.':
                return row_index

        return None

    # Code here
    width = len(warehouse[0])

    for drop in drops:
        lowest_empty_cell_row_index = get_lowest_empty_cell_row_index(
            warehouse=warehouse, column_index=drop
        )

        if lowest_empty_cell_row_index is not None:
            # Drop gift in specified column
            warehouse[lowest_empty_cell_row_index][drop] = '#'

            # Check row and clear if necessary
            if all(cell == "#" for cell in warehouse[lowest_empty_cell_row_index]):
                warehouse.pop(lowest_empty_cell_row_index)
                warehouse.insert(0, ["." for _ in range(width)])

    return warehouse
