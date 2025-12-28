def has_four_lights(board: list[list[str]]) -> bool:
    # Code here
    for x in range(len(board)):
        for y in range(len(board[x])):
            current_light = board[x][y]
            if current_light != '.':
                # Check horizontal row
                if (
                    y + 3 < len(board[x]) and
                    all(board[x][i] == current_light for i in range(y, y + 4))
                ):
                    return True

                # Check vertical row
                if (
                    x + 3 < len(board) and
                    all(board[i][y] == current_light for i in range(x, x + 4))
                ):
                    return True

    return False
