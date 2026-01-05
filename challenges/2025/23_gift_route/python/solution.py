from collections import deque


def min_steps_to_deliver(map: list[list[str]]) -> int:

    def get_start_position(map: list[list[str]]) -> tuple[int, int]:
        for row_index, row in enumerate(map):
            for column_index, cell in enumerate(row):
                if cell == 'S':
                    return row_index, column_index

        raise ValueError("There is no initial position.")

    def get_house_locations(map: list[list[str]]) -> list[tuple[int, int]]:
        house_locations = []

        for row_index, row in enumerate(map):
            for column_index, cell in enumerate(row):
                if cell == 'G':
                    house_locations.append((row_index, column_index))

        return house_locations

    def are_valid_coordinates(row: int, column: int, map: list[list[str]]) -> bool:
        return (
            0 <= row < len(map) and
            0 <= column < len(map[0]) and
            map[row][column] != '#'
        )

    def get_neighbors(
        row_index: int,
        column_index: int,
        map: list[list[str]]
    ) -> list[tuple[int, int]]:
        possible_movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []

        for row_delta, column_delta in possible_movements:
            neighbor_row_index = row_index + row_delta
            neighbor_column_index = column_index + column_delta

            if are_valid_coordinates(neighbor_row_index, neighbor_column_index, map):
                neighbors.append((neighbor_row_index, neighbor_column_index))

        return neighbors

    # Code here

    # Set-up initial state
    start_position = get_start_position(map)
    house_locations = get_house_locations(map)
    remaining_houses = len(house_locations)
    visited = {start_position: 0}
    queue = deque([start_position])
    total_steps = 0

    # Check distance to each house
    while queue and remaining_houses >= 0:
        current_position = queue.popleft()

        if current_position in house_locations:
            total_steps += visited[current_position]
            remaining_houses -= 1

        for neighbor in get_neighbors(current_position[0], current_position[1], map):
            if neighbor not in visited:
                queue.append(neighbor)
                visited[neighbor] = visited[current_position] + 1

    if remaining_houses == 0:
        return total_steps

    return -1
