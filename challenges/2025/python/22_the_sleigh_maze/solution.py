from collections import deque
from dataclasses import dataclass


def can_escape(maze: list[list[str]]) -> bool:

    @dataclass(frozen=True)
    class Square:
        row: int
        column: int

    def get_start_position(maze: list[list[str]]) -> Square:
        for row_index, row in enumerate(maze):
            for column_index, cell in enumerate(row):
                if cell == "S":
                    return Square(row=row_index, column=column_index)

        raise ValueError("There is no initial position.")

    def is_maze_exit(square: Square, maze: list[list[str]]) -> bool:
        return maze[square.row][square.column] == "E"

    def are_valid_coordinates(row: int, column: int, maze: list[list[str]]) -> bool:
        return (
            0 <= row < len(maze) and
            0 <= column < len(maze[0]) and
            maze[row][column] != "#"
        )

    def get_square_neighbors(square: Square, maze: list[list[str]]) -> list[Square]:
        possible_movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []

        for row_delta, column_delta in possible_movements:
            neighbor_row_index = square.row + row_delta
            neighbor_column_index = square.column + column_delta

            if are_valid_coordinates(neighbor_row_index, neighbor_column_index, maze):
                neighbors.append(
                    Square(
                        row=square.row + row_delta, column=square.column + column_delta
                    )
                )

        return neighbors

    # Code here

    # Set-up initial state
    start_position = get_start_position(maze)
    visited = {start_position}
    queue = deque([start_position])

    # Look for maze exit
    while queue:
        current_position = queue.popleft()

        if is_maze_exit(current_position, maze):
            return True

        for neighbor in get_square_neighbors(current_position, maze):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    # No maze exit found
    return False
