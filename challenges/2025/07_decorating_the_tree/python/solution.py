def draw_tree(height: int, ornament: str, frequency: int) -> str:
    # Code here
    TREE_ELEMENT = "*"
    WHITESPACE = " "
    TRUNK_ELEMENT = "#"

    tree_rows = []
    element_index = 1
    row_length = 2 * height - 1

    for row_index in range(1, height + 1):
        tree_elements_count_in_row = 2 * row_index - 1
        whitespaces_count_in_row = (row_length - tree_elements_count_in_row) // 2

        current_tree_row = WHITESPACE * whitespaces_count_in_row
        for _ in range(tree_elements_count_in_row):
            current_tree_row += ornament if element_index % frequency == 0 else TREE_ELEMENT
            element_index += 1

        tree_rows.append(current_tree_row)

    last_row_whitespaces_count = (row_length - len(TRUNK_ELEMENT)) // 2
    last_row = last_row_whitespaces_count * WHITESPACE + TRUNK_ELEMENT
    tree_rows.append(last_row)

    return '\n'.join(tree_rows)
