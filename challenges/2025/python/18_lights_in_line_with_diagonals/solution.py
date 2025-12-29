def has_four_in_a_row(board: list[list[str]]) -> bool:

    def is_vertical_line(
        row_index: int, column_index: int, board: list[list[str]], current_light: str
    ) -> bool:
        if row_index + 3 < len(board) and all(
            board[i][column_index] == current_light
            for i in range(row_index, row_index + 4)
        ):
            return True

        return False

    def is_horizontal_line(
        row_index: int, column_index: int, board: list[list[str]], current_light: str
    ) -> bool:
        if column_index + 3 < len(board[row_index]) and all(
            board[row_index][i] == current_light
            for i in range(column_index, column_index + 4)
        ):
            return True

        return False

    def is_right_hand_diagonal_line(
        row_index: int, column_index: int, board: list[list[str]], current_light: str
    ) -> bool:
        if (
            row_index + 3 < len(board)
            and column_index + 3 < len(board[row_index])
            and all(
                board[i][j] == current_light
                for i, j in zip(
                    range(row_index, row_index + 4),
                    range(column_index, column_index + 4),
                )
            )
        ):
            return True

        return False

    def is_left_hand_diagonal_line(
        row_index: int, column_index: int, board: list[list[str]], current_light: str
    ) -> bool:
        if (
            row_index + 3 < len(board)
            and column_index - 3 >= 0
            and all(
                board[i][j] == current_light
                for i, j in zip(
                    range(row_index, row_index + 4),
                    range(column_index, column_index - 4, -1),
                )
            )
        ):
            return True

        return False

    def is_diagonal_line(
        row_index: int, column_index: int, board: list[list[str]], current_light: str
    ) -> bool:
        return any(
            [
                is_right_hand_diagonal_line(
                    row_index, column_index, board, current_light
                ),
                is_left_hand_diagonal_line(
                    row_index, column_index, board, current_light
                ),
            ]
        )

    # Code here
    for row_index in range(len(board)):
        for column_index in range(len(board[row_index])):
            current_light = board[row_index][column_index]
            if current_light != ".":
                if any(
                    [
                        is_vertical_line(row_index, column_index, board, current_light),
                        is_horizontal_line(
                            row_index, column_index, board, current_light
                        ),
                        is_diagonal_line(row_index, column_index, board, current_light),
                    ]
                ):
                    return True

    return False
