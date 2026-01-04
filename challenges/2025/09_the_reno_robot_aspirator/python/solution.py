from typing import Literal

def move_reno(board: str, moves: str) -> Literal['fail', 'crash', 'success']:
    # Code here
    clean_board = board.split('\n')[1:-1]

    # Get reindeer location
    reindeer_location = {'row': -1, 'column': -1}
    for row_id, row_content in enumerate(clean_board):
        for column_id, column_content in enumerate(row_content):
            if column_content == '@':
                reindeer_location['row'] = row_id
                reindeer_location['column'] = column_id
                break

    # Read movements and check result for each
    for move in moves:

        # Update reindeer location based on move
        if move == 'L':
            reindeer_location['column'] -= 1
        elif move == 'R':
            reindeer_location['column'] += 1
        elif move == 'U':
            reindeer_location['row'] -= 1
        elif move == 'D':
            reindeer_location['row'] += 1

        # Check resulting state after updating location
        current_row_id = reindeer_location['row']
        current_column_id = reindeer_location['column']

        if not (
            0 <= current_row_id < len(clean_board)
            and 0 <= current_column_id < len(clean_board[current_row_id])
        ):
            return 'crash'

        board_location = clean_board[current_row_id][current_column_id]
        if board_location == '*':
            return 'success'
        elif board_location == '#':
            return 'crash'

    return 'fail'
