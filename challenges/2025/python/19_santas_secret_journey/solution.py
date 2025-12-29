def reveal_santa_route(routes: list[list[str]]) -> list[str]:

    def get_next_trip_segment(last_segment: str, routes: list[list[str]]) -> str | None:
        for route in routes:
            origin = route[0]
            destination = route[1]

            if origin == last_segment:
                return destination

        return None

    # Code here
    santa_route = routes[0]
    next_trip_segment = get_next_trip_segment(
        last_segment=santa_route[-1], routes=routes
    )

    while next_trip_segment is not None:
        santa_route.append(next_trip_segment)
        next_trip_segment = get_next_trip_segment(
            last_segment=santa_route[-1], routes=routes
        )

    return santa_route
