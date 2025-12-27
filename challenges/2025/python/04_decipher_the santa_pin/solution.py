def decode_santa_pin(code: str) -> str:
    # Code here
    def process_block(block: str, last_digit: int) -> str:
        current_digit = 0

        for element in block:
            if element.isdigit():
                current_digit = int(element)

            elif element == '+':
                current_digit = (current_digit + 1) % 10

            elif element == '-':
                current_digit = (current_digit - 1) % 10

            elif element == '<':
                if last_digit is None:
                    raise ValueError("No hay dígito previo para usar '<'")
                current_digit = last_digit

        return str(current_digit)


    decoded_pin = ""
    last_digit = None
    inside_block = False
    block_buffer = ""

    for element in code:
        if element == '[':
            inside_block = True
            block_buffer = ""
            continue

        if inside_block:
            if element == ']':
                result = process_block(block_buffer, last_digit)
                last_digit = int(result)
                decoded_pin += result
                inside_block = False

            else:
                block_buffer += element

    if len(decoded_pin) < 4:
        return None

    return decoded_pin
