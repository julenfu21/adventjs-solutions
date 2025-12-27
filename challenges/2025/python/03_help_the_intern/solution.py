def draw_gift(size, symbol):
    # Code here
    if size < 2:
        return ''

    top_and_bottom_boundary = symbol * size
    body = symbol + " " * (size - 2) + symbol

    return "\n".join([
        top_and_bottom_boundary,
        *[body for _ in range(size - 2)],
        top_and_bottom_boundary
    ])
