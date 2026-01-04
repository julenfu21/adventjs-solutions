def max_depth(s: str) -> int:
    # Code here
    current_depth = 0
    max_depth = 0

    for element in s:
        if element == '[':
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif element == ']':
            current_depth -= 1
            if current_depth < 0:
                return -1

    if current_depth != 0:
        return -1

    return max_depth
