from dataclasses import dataclass
from typing import Literal, Optional


def run_factory(factory: list[str]) -> str:
    @dataclass(frozen=True)
    class Location:
        row: int
        column: int

        def is_out_of_bounds(self, factory: list[str]) -> bool:
            return not (
                0 <= self.row < len(factory) and
                0 <= self.column < len(factory[self.row])
            )

    def get_next_move(
        factory: list[str],
        location: Location
    ) -> Literal['>', '<', '^', 'v']:
        return factory[location.row][location.column]

    def update_present_location(
        location: Location,
        move: Literal['>', '<', '^', 'v']
    ) -> Location:
        row = location.row
        column = location.column

        if move == '>':
            column += 1
        elif move == '<':
            column -= 1
        elif move == '^':
            row -= 1
        elif move == 'v':
            row += 1

        return Location(row=row, column=column)

    def get_location_state(
        location: Location,
        explored_locations: set[Location],
        factory: list[str]
    ) -> Optional[Literal['completed', 'loop', 'broken']]:
        location_state = None

        if location.is_out_of_bounds(factory):
            location_state = 'broken'
        elif location in explored_locations:
            location_state = 'loop'
        elif factory[location.row][location.column] == '.':
            location_state = 'completed'

        return location_state

    # Code here
    explored_locations = set()
    current_location = Location(row=0, column=0)
    final_location_state = get_location_state(
        current_location, explored_locations, factory
    )

    while not final_location_state:
        explored_locations.add(current_location)
        next_move = get_next_move(factory, current_location)
        current_location = update_present_location(current_location, next_move)
        final_location_state = get_location_state(
            current_location, explored_locations, factory
        )

    return final_location_state
