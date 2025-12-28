import string


def draw_table(data: list[dict[str, str | int]], sort_by: str) -> str:

    def get_fields_max_lengths(data: list[dict[str, str | int]]) -> dict[str, int]:
        fields_max_lengths = {}

        for row in data:
            for field_name, field_value in row.items():
                str_field_value = str(field_value)

                if field_name not in fields_max_lengths:
                    fields_max_lengths[field_name] = len(str_field_value)
                else:
                    fields_max_lengths[field_name] = max(
                        fields_max_lengths[field_name], len(str_field_value)
                    )

        return fields_max_lengths

    def draw_table_divider(
        fields_max_lengths: dict[str, int],
        corner_symbol: str = "+",
        vertical_edge_symbol: str = "-",
    ) -> str:
        divider = corner_symbol

        for max_length in fields_max_lengths.values():
            divider += vertical_edge_symbol * (max_length + 2) + corner_symbol

        return divider

    def draw_table_header(
        fields_max_lengths: dict[str, int], horizontal_edge_symbol: str = "|"
    ) -> str:
        uppercase_alphabet = string.ascii_uppercase
        header_row = horizontal_edge_symbol

        for field_count, max_length in enumerate(fields_max_lengths.values()):
            header_row += (
                " "
                + uppercase_alphabet[field_count]
                + " " * max_length
                + horizontal_edge_symbol
            )

        return header_row

    def draw_table_body(
        fields_max_lengths: dict[str, int],
        data: list[dict[str, str | int]],
        horizontal_edge_symbol: str = "|",
    ) -> list[str]:
        data_rows = []

        for row in data:
            new_row = horizontal_edge_symbol

            for field_name, field_value in row.items():
                str_field_value = str(field_value)
                field_length = fields_max_lengths[field_name] - len(str_field_value) + 1
                new_row += (
                    " " + str_field_value + " " * field_length + horizontal_edge_symbol
                )

            data_rows.append(new_row)

        return data_rows

    # Code here
    data.sort(key=lambda row: row[sort_by])
    fields_max_lengths = get_fields_max_lengths(data)

    return "\n".join(
        [
            draw_table_divider(fields_max_lengths),
            draw_table_header(fields_max_lengths),
            draw_table_divider(fields_max_lengths),
            *draw_table_body(fields_max_lengths, data),
            draw_table_divider(fields_max_lengths),
        ]
    )
